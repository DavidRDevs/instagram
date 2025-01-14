from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import gettext as _


from posts.models import Post
from profiles.models import Follow
from .forms import RegisterForm, LoginForm


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            seguidos = Follow.objects.filter(
                follower=self.request.user.profile).values_list("following__user", flat=True)
            last_posts = Post.objects.filter(user__profile__user__in=seguidos)
        else:
            last_posts = Post.objects.all().order_by('-created_at')
        context["last_posts"] = last_posts
        return context


class LegalView(TemplateView):
    template_name = "core/legal.html"


class ContactView(TemplateView):
    template_name = "core/contacto.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class Registerview(CreateView):
    model = User
    success_url = reverse_lazy("login")
    template_name = "core/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, _(f"Usuario creado correctamente"))
        return super(Registerview, self).form_valid(form)


class LoginView(FormView):
    template_name = "core/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        contraseña = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=contraseña)
        if user is not None:
            login(self.request, user)
            messages.add_message(
                self.request, messages.SUCCESS, _(f"Bienvenido {user.username}"))
            return redirect(reverse('home'))
        else:
            messages.add_message(
                self.request, messages.ERROR, _("Usuario o contraseña no validos."))
            return super(LoginView, self).form_invalid(form)


def logout_view(request):
    logout(request)
    messages.add_message(
        request, messages.INFO, _("Se ha cerrado la sesión correctamente"))
    return redirect(reverse('login'))

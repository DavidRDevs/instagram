from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import DetailView, ListView
from .models import UserProfiles, Follow
from django.contrib import messages
from django.utils.translation import gettext as _
from django.urls import reverse

from instagram.forms import ProfileFollow, ProfileUpdateForm


@method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView, FormView):
    model = UserProfiles
    template_name = "profiles/profile_detail.html"
    context_object_name = "profile"
    form_class = ProfileFollow

    def form_valid(self, form):
        profile_pk = form.cleaned_data.get('profile_pk')
        following = UserProfiles.objects.get(pk=profile_pk)

        if Follow.objects.filter(
            follower=self.request.user.profile,
            following=following
        ).count():
            Follow.objects.filter(
                follower=self.request.user.profile,
                following=following
            ).delete()
            messages.add_message(
                self.request, messages.SUCCESS, _(f"Has dejado de seguir a {following.user.username} correctamente"))
        else:
            Follow.objects.get_or_create(
                follower=self.request.user.profile,
                following=following
            )
            messages.add_message(
                self.request, messages.SUCCESS, _(f"Has seguido a {following.user.username} correctamente"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        following = Follow.objects.filter(
            follower=self.request.user.profile, following=self.get_object()).exists()
        # Agregar contadores de seguidores y seguidos
        context['following_count'] = Follow.objects.filter(
            follower=profile).count()
        context['followers_count'] = Follow.objects.filter(
            following=profile).count()
        context['following'] = following
        context['form'] = ProfileFollow(initial={'profile_pk': profile.pk})
        return context


@method_decorator(login_required, name="dispatch")
class UpdateProfileview(UpdateView):
    model = UserProfiles
    template_name = "profiles/profile_update.html"
    context_object_name = "profile"
    form_class = ProfileUpdateForm

    def dispatch(self, request, *args, **kwargs):
        user_profile = self.get_object()
        if user_profile.user != self.request.user:
            return HttpResponseRedirect(reverse('home'))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, _(f"Perfil modificado correctamente"))
        return super(UpdateProfileview, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])


class ProfilesListView(ListView):
    model = UserProfiles
    template_name = "profiles/list_profiles.html"
    context_object_name = "profiles"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return UserProfiles.objects.all()
        else:
            return UserProfiles.objects.all().exclude(user=self.request.user)

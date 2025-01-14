from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post
from .forms import PostCreateForm, CommentCreatForm


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    template_name = "posts/posts_create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, _("Publicación creada con éxito")
        )
        return super(PostCreateView, self).form_valid(form)


class PostDetailView(DetailView, CreateView):
    model = Post
    template_name = "posts/posts_detail.html"
    context_object_name = "post"
    form_class = CommentCreatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.get_object()

        return super(PostDetailView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _("Publicación comentada con éxito")
        )
        return reverse("post_detail", args=[self.get_object().pk])


@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.add_message(
            request, messages.SUCCESS, _("Ya no te gusta esta publicación")
        )
        previous_url = request.META.get("HTTP_REFERER", "/")
    else:
        post.likes.add(request.user)
        messages.add_message(request, messages.SUCCESS, _("Te gusta esta publicación"))
        previous_url = request.META.get("HTTP_REFERER", "/")
    return HttpResponseRedirect(previous_url)


@login_required
def like_post_ajax(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        return JsonResponse(
            {
                "messaje": "Ya no te gusta esta publicación",
                "liked": False,
                "nLikes": post.likes.all().count(),
            }
        )
    else:
        post.likes.add(request.user)
        return JsonResponse(
            {
                "messaje": "Te gusta esta publicación",
                "liked": True,
                "nLikes": post.likes.all().count(),
            }
        )

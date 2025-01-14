from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', verbose_name=_("Usuario"))
    image = models.ImageField(upload_to='posts/', verbose_name=_("Imagen"))
    caption = RichTextField(max_length=500, blank=True, verbose_name=_("Descripción"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    likes = models.ManyToManyField(
        User, related_name='liked_posts', blank=True, verbose_name=_("Numero de Likes"))

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


def __str__(self):
    return f"{self.user.username} - {self.created_at}"


class Comment (models.Model):
    post = models.ForeignKey( 
        Post, verbose_name="Post al que pertenece el comentario", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(  
        User, verbose_name="Autor", on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name="Comentario", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Comentario')
        verbose_name_plural = _('Comentarios')
        ordering = ['-created_at']

def __str__(self):
    return _(f"Coméntó {self.user.username} el post {self.post}")


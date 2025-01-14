from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class UserProfiles(models.Model):
    user = models.OneToOneField(
        User,  on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(
        _('Imagen de perfil'), upload_to="profile_pictures/", blank=True, null=True)
    bio = RichTextField(_('Biografia'), max_length=500, blank=True)
    birth_date = models.DateField(
        verbose_name=_("Fecha de nacimiento"), blank=True, null=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name='Following', through='Follow')
    created_at = models.DateTimeField(
        verbose_name=_("Fecha y Hora de creación"),
        default=timezone.now,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username
    
    def follow(self, profile):
        Follow.objects.get_or_create(follower=self, following=profile)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfiles, verbose_name=_("¿Quien sigue?"),
                                 on_delete=models.CASCADE, related_name='follower_set')
    following = models.ForeignKey(UserProfiles, verbose_name=_("¿A quien sigue?"),
                                  on_delete=models.CASCADE, related_name='following_set')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("¿Desde cuando lo sigue?"))

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower} follows {self.following}'

    class Meta:
        verbose_name = _('Seguidor')
        verbose_name_plural = _('Seguidores')

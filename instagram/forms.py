from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from profiles.models import UserProfiles

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
        ]

    def save(self):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()

        from profiles.models import UserProfiles
        UserProfiles.objects.create(user=user)

        return user


class LoginForm(forms.Form):

    username = forms.CharField(label=_("Nombre de usuario"))
    password = forms.CharField(
        label=_("Contraseña"), widget=forms.PasswordInput())

class ProfileFollow(forms.Form):
    profile_pk = forms.IntegerField(label=_("Identificador del usuario"), widget=forms.HiddenInput())



class ProfileUpdateForm(forms.ModelForm):
    # Campos del usuario
    first_name = forms.CharField(max_length=30, required=False, label=_("Nombres"))
    last_name = forms.CharField(max_length=30, required=False, label=_("Apellidos"))
    
    class Meta:
        model = UserProfiles
        fields = ['profile_picture', 'bio', 'birth_date', 'first_name', 'last_name']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # Inicializa los campos del usuario con los valores actuales
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        # Guarda los campos de User además de los de UserProfiles
        profile = super(ProfileUpdateForm, self).save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile.save()
        return profile

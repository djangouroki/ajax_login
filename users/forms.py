from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm as UserCreationFormDjango
)
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class AuthenticationAjaxForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'class': 'form-control'
            }
        ),
    )


class UserCreationForm(UserCreationFormDjango):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationFormDjango.Meta):
        model = User
        fields = ("username", "email")

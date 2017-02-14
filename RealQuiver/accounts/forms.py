from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import (ModelForm, Form)
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)

from accounts.models import CustomUser


class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email', 'password',)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password1=password)
            if not user:
                raise forms.ValidationError("This user does not exist!")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password!")

            if not user.is_active:
                raise forms.ValidationError("User is not active!")

        return super(LoginForm, self).clean(*args, **kwargs)

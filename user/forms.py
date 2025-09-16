from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Users


class CreateUserForm(forms.ModelForm):
    passowrd1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = Users
        fields = "__all__"
    def clean(self):
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']

        if pass1 and pass2 and pass1 == pass2:
            return pass2

        raise ValidationError("confirm password error!!")

    def save(self, commit=True):
        # this is our user obj cause we used ModelForm
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['passowrd2'])
        if commit:
            user.save()
        return user


class ModifyUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="<a href='../password/'> change it </a>"
    )

    class Meta:
        model = Users
        fields = "__all__"

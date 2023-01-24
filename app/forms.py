from django import forms

from app.models import User, File


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        # fields = ['owner', 'file', 'mark']
        fields = ['file']

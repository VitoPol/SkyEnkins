from django import forms
from django.contrib.auth.forms import UserCreationForm
from rest_framework_simplejwt.serializers import PasswordField

from app.models import User, File


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         field_classes = {"password": PasswordField}


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        # fields = ['owner', 'file', 'mark']
        fields = ['file']

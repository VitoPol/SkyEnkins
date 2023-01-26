from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


from skyenkins import settings


class File(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='static/', validators=[FileExtensionValidator(allowed_extensions=['py'])])
    mark = models.CharField(max_length=8, choices=[("new", "новый"), ("changed", "изменено"), ("verified", "проверено")])
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

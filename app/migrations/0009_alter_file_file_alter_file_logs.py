# Generated by Django 4.1.5 on 2023-01-29 16:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_file_options_file_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'])]),
        ),
        migrations.AlterField(
            model_name='file',
            name='logs',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='changed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

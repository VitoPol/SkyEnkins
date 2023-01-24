# Generated by Django 4.1.5 on 2023-01-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_file_changed_file_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='changed',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='mark',
            field=models.CharField(choices=[('new', 'новый'), ('changed', 'изменено'), ('verified', 'проверено')], max_length=8),
        ),
    ]

import os
from time import sleep

from celery import shared_task

from django.core.files import File as dj_file
from django.core.mail import send_mail

from app.models import File, User
from skyenkins import settings


@shared_task(name="checking_files")
def checking_files():
    users_id = set()
    files = File.objects.filter(mark__in=["changed", "new"])

    for file in files:
        users_id.add(file.owner_id)
        logname = f'{file.file.name.replace(".py", ".txt")}'
        com = f'flake8 "{file.file.path}" >> static/logs/{logname}'
        print(com)
        os.system(com)
        file.mark = "verified"
        with open(f"static/logs/{logname}", "a+") as f:
            f.write("\nFile is verified. Email is sent.\n\n")
            file.logs = dj_file(f, f"{logname}")
            file.save()

    users = User.objects.filter(id__in=users_id)
    emails = []
    for user in users:
        emails.append(user.email)

    send_mail("Notification of inspection", "Your files are verified. Check it at SkyEnkins.", settings.EMAIL_HOST_USER,
              emails)

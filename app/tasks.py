import os
from time import sleep

from celery import shared_task

from django.core.files import File as dj_file

from app.models import File


#
# @shared_task
# def test(x, y):
#     sleep(3)
#     return x + y

@shared_task(name="checking_files")
def checking_files():
    # for filename in filenames:
    #     os.system(f'flake8 "{os.path.relpath("files/some_file.py")}" > logs/{filename}.txt')
    files = File.objects.filter(mark__in=["changed", "new"])
    for file in files:
        logname = f'{file.file.name.replace(".py", "").replace("static/", "static/logs/")}.txt'
        com = f'flake8 "{file.file.path}"' \
              f' > {logname}'
        print(com)
        os.system(com)
        file.mark = "verified"
        with open(f"{logname}") as f:
            file.logs = dj_file(f, f"{logname.split('/')[-1]}")
            file.save()

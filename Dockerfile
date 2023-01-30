FROM python

EXPOSE 8000

WORKDIR /django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN bash -c "pip install -r requirements.txt"

#CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 8000

#CMD bash -c "python manage.py migrate && python manage.py runserver 8000"
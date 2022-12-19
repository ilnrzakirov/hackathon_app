FROM python:3.10.5-slim

RUN mkdir /app

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt && python3 manage.py migrate

RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin1@example.com', 'admin')"

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

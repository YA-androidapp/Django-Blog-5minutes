# Django-Blog-5minutes

https://django-crud-generator.readthedocs.io/en/latest/create_blog_in_5_minutes.html

---

## Create apps

```sh
python -m venv myenv
source myenv/bin/activate

pip install django django-crud-generator
django-admin startproject myblog .
mkdir applications && touch applications/__init__.py
git clone https://github.com/contraslash/base-django base

cd applications
git clone https://github.com/contraslash/template_cdn_bootstrap
git clone https://github.com/contraslash/authentication-django authentication
django-admin startapp myblog
nano myblog/models.py
```

```py
from django.db import models # 既存

# 以下を追記
from django.contrib.auth import models as auth_models

from base import models as base_models

from . import (
    conf
)


class Post(base_models.FullSlugBaseModel):
    class Meta:
        app_label = 'myblog'

    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    url_name = conf.POST_DETAIL_URL_NAME

```

```sh
cd ..

django-crud-generator.py --model_name Post --django_application_folder applications/myblog/ --slug
nano myblog/settings.py
```

```py
INSTALLED_APPS += [
    'base',
    'applications.authentication',
    'applications.template_cdn_bootstrap',
    'applications.myblog',
]

# And define an the LOGIN URL
LOGIN_URL = "log_in"
```

```sh
nano myblog/urls.py
```

```py
# 既存
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# 以下に置換
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'authentication/',
        include(
            "applications.authentication.urls",
        )
    ),
    path(
        '',
        include(
            "applications.myblog.urls_slug",
        )
    ),
]
```

```sh
deactivate
```

## Run

```sh
python -m venv myenv
source myenv/bin/activate
python -m pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD="Passw0rd#" DJANGO_SUPERUSER_USERNAME="Admin" DJANGO_SUPERUSER_EMAIL="admin@example.net" python manage.py createsuperuser --noinput
python manage.py runserver
```

## Dozkerize

### Docker

```sh
nano myblog/settings.py
```

```py
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
import os
DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':os.getenv('DATABASE_NAME'),
      'USER':os.getenv('DATABASE_USER'),
      'PASSWORD':os.getenv('DATABASE_PASSWORD'),
      'HOST':os.getenv('DATABASE_HOST'),
      'PORT':'5432',
      'OPTIONS': {'sslmode': 'require'}
   }
}
```

```sh
nano Dockerfile
```

```Dockerfile
FROM python:3

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
```

```sh
docker build --tag myblog:latest .
```

### Docker Compose

```sh
nano docker-compose.yml
```

```yml
version: "3"

volumes:
  dbvolume:

services:
  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - dbvolume:/var/lib/postgresql/data
  web:
    image: yaand/django-blog-5minutes-web
    build: .
    command: bash -c 'python manage.py makemigrations && python manage.py migrate && DJANGO_SUPERUSER_PASSWORD="Passw0rd#" DJANGO_SUPERUSER_USERNAME="Admin" DJANGO_SUPERUSER_EMAIL="admin@example.net" python manage.py createsuperuser --noinput && python manage.py runserver 0.0.0.0:8000'
    environment:
      - DATABASE_HOST=db
      - DATABASE_NAME=postgres
      - DATABASE_USER=postgres
      - DATABASE_PASSWORD=postgres
      - DATABASE_SSL_MODE=disable
    ports:
      - "8000:8000"
    depends_on:
      - db
```

```sh
# 既存がある場合は全削除してから
# docker-compose down --rmi all --volumes --remove-orphans

docker-compose up -d --build
```

### Kubernetes

```sh
nano myblog.yaml
```

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myblog
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myblog
  template:
    metadata:
      labels:
        app: myblog
    spec:
      containers:
        - name: myblog
          image: yaand/django-blog-5minutes-web
          ports:
            - containerPort: 8000
          env:
            - name: DATABASE_HOST
              value: "*****.postgres.database.azure.com"
            - name: DATABASE_USER
              value: "postgres"
            - name: DATABASE_PASSWORD
              value: "**********"
            - name: DATABASE_NAME
              value: "postgres"
            - name: DATABASE_SSL_MODE
              value: "require"
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: "app"
                    operator: In
                    values:
                      - myblog
              topologyKey: "kubernetes.io/hostname"
---
apiVersion: v1
kind: Service
metadata:
  name: python-svc
spec:
  type: LoadBalancer
  ports:
    - port: 8000
  selector:
    app: myblog
```

```sh
kubectl config get-contexts
kubectl apply -f myblog.yml

kubectl get service myblog --watch
kubectl get pods --watch

kubectl exec myblog--*****-*****-***** -- python /code/manage.py migrate
kubectl exec myblog--*****-*****-***** -- bash -c 'DJANGO_SUPERUSER_PASSWORD="Passw0rd#" DJANGO_SUPERUSER_USERNAME="Admin" DJANGO_SUPERUSER_EMAIL="admin@example.net" python manage.py createsuperuser --noinput'
```

http://localhost:8000/post/

---

Copyright (c) 2021 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

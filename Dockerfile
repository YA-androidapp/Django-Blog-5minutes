FROM python:3

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000

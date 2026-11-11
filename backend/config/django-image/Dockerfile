FROM python:3.12-bookworm

RUN apt-get update && apt-get install python3-dev graphviz graphviz-dev -y --force-yes

WORKDIR /usr/src/app

RUN pip install --upgrade pip & pip install --upgrade setuptools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN django-admin startproject app .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
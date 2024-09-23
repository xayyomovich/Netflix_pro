FROM python:3.11-alpine

WORKDIR /netflix

COPY . /netflix

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



FROM python:3.10-slim

WORKDIR /netflix

COPY . /netflix

#pip install --upgrade pip setuptools

#pip install --no-cache-dir -r requirements.txt
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


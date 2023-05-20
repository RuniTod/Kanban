FROM python:3.10
LABEL authors="Kanban"

WORKDIR /kanban

COPY requirements.txt /kanban

RUN pip3 install --upgrade pip -r requirements.txt

COPY . /kanban
EXPOSE 5000
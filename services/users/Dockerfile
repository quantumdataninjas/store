FROM python:3.7.4-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev libffi-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd && \
    apk upgrade

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

COPY . /usr/src/app

CMD ["/usr/src/app/entrypoint.sh"]

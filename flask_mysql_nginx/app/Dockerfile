FROM python:3.14.0rc2-alpine3.22 AS builder

RUN adduser -h /home/sample -s /bin/sh -D  sample
RUN apk update

USER sample 
WORKDIR /home/sample/app
COPY --chown=sample:sample . /home/sample/app 
RUN pip install -r requirement.txt

CMD ["python3","app.py"]
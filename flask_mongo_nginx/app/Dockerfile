FROM python:3.14.0rc2-bookworm AS builder

WORKDIR /app
RUN apt update \
    && apt install gettext -y
RUN /bin/bash -c "useradd -m -s /bin/bash flask && su flask "
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 9999
ENTRYPOINT ["python3","app.py"]

FROM python:3.10.6

WORKDIR usr/src/app

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash cb && chmod 777 /opt /run


COPY . .
RUN pip install -r requirements.txt
RUN chmod 755 /usr/src/app/prestart.sh
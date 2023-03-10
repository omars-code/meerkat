FROM python:3.12.0a5-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y automake make git zsh util-linux && \
    rm -f /tmp/*

RUN pip install --upgrade pip pipenv

# set working directory
RUN mkdir -p /code/
WORKDIR /code/

# add requirements
COPY Pipfile Pipfile.lock /code/

RUN pipenv --python 3
RUN mkdir -p ~/.ssh/ && ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
RUN pipenv install --dev --deploy

# add entrypoint.sh
COPY ./.docker/entrypoint.sh /code/

EXPOSE 8000

# run server
CMD ["sh", "/code/entrypoint.sh"]

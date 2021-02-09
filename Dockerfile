FROM python:3.9.1-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y automake build-essential libffi-dev libssl-dev nodejs npm protobuf-compiler git zsh postgresql util-linux && \
    rm -f /tmp/*

RUN sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

RUN npm config set unsafe-perm true

RUN npm i -g nodemon yarn
RUN pip install --upgrade pip pipenv

# set working directory
RUN mkdir -p /code/
WORKDIR /code/

# add requirements
COPY ./requirements-dev.txt /code/requirements-dev.txt
COPY ./requirements.txt /code/requirements.txt

# install requirements
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

# add entrypoint.sh
COPY ./.docker/entrypoint.sh /code/.docker/entrypoint.sh

EXPOSE 8000

# run server
CMD ["sh", "/code/.docker/entrypoint.sh"]

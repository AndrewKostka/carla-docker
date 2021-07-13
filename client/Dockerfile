FROM ubuntu:18.04

WORKDIR /usr

RUN apt-get update \
    && apt-get install -y \
        libjpeg-turbo8 \
        libtiff5 \
        libxerces-c-dev \
        python3.7 \
        python3-pip

RUN mkdir -p ./carla
COPY --from=carlasim/carla:0.9.10 /home/carla/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg ./carla
ENV CARLA_EGG_PATH /usr/carla/carla-0.9.10-py3.7-linux-x86_64.egg

COPY --from=carlasim/carla:0.9.10 /home/carla/PythonAPI/carla/requirements.txt /tmp/requirements.carla.txt
RUN python3.7 -m pip install --no-cache-dir -r /tmp/requirements.carla.txt

COPY ./requirements.txt /tmp/requirements.client.txt
RUN python3.7 -m pip install --no-cache-dir -r /tmp/requirements.client.txt

RUN mkdir -p ./client/src
COPY ./src ./client/src

CMD [ "python3.7", "-u", "./client/src/main.py" ]

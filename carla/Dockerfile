FROM carlasim/carla:0.9.10

USER root

RUN apt-get update \
    && apt-get install -y netcat

USER carla

COPY ./maps/ /home/carla/CarlaUE4/Content/Carla/Maps

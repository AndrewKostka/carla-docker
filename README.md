# CARLA Environment in Docker

A fully dockerized [CARLA](https://github.com/carla-simulator/carla) environment.

## Requirements

Install the following dependencies:
- [Docker](https://docs.docker.com/engine/install/)
- [NVIDIA Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#getting-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

Tested on Ubuntu 20.04.2 LTS with:
- Docker 20.10.7
- Docker Compose 1.29.1
- NVIDIA Docker 2.6.0
- NVIDIA Driver 460.80

## Getting Started
This stack is managed using [docker-compose](https://docs.docker.com/compose/reference/) so getting up and running is as simple as (1) building the containers and (2) running them.

*Be warned the initial build process might take a while.*

```
docker-compose build
docker-compose up
```

## Services

This stack consists of:
1. **Carla:** an instance of [CARLA Simulator](https://github.com/carla-simulator/carla/tree/0.9.10) v0.9.10 with X11 forwarding
2. **Client:** a Python v3.7 client with access to the [CARLA Python API](https://carla.readthedocs.io/en/0.9.10/python_api/)

See `docker-compose.yml` and the respective service directories for more configuration details.

## Client Development

The Python source code for the CARLA client can be found in `client/src` with `client/src/main.py` being the designated entry point.

*Note: This directory is mapped as a volume in the client container, therefore, making changes in this directory does not require rebuilding the container.*

### Python Dependencies

1. Add any dependencies to `client/requirements.txt`
2. Rebuild the container using:
    ```
    docker-compose build client
    ```

### CARLA Maps

1. Add any custom CARLA maps to `carla/maps/`
2. Rebuild the container using:
    ```
    docker-compose build carla
    ```

## Troubleshooting

### Carla container exits immediately with code 1

Unfortunately, this solution currently doesn't support running on a headless system. It might be possible with [VirtualGL](https://virtualgl.org/vgldoc/2_2_1/) but this hasn't been tested. In the meantime, please ensure that your display supports OpenGL 4.6.0 and is using NVIDIA drivers. This can be [verified on Ubuntu](https://askubuntu.com/a/47084) by running:

```
glxinfo | grep "OpenGL version"
```

If the command above results in `Error: unable to open display`, then ensure that you have a value set for `$DISPLAY` in your environment prior to running the aforementioned command and prior to running any docker-compose up commands. The following is an example of setting the display:

```
export DISPLAY=:1
```

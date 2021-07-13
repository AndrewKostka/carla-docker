import os
import sys

try:
    sys.path.append(os.environ.get("CARLA_EGG_PATH"))
except IndexError:
    sys.exit("Error: Can't find Carla .egg")

import carla
import time

class Main(object):
    CARLA_SERVER_IP = os.environ.get("CARLA_SERVER_IP")
    CARLA_SERVER_PORT = int(os.environ.get("CARLA_SERVER_PORT"))

    def __init__(self):
        print("Connecting to Carla server at {}:{}".format(self.CARLA_SERVER_IP, self.CARLA_SERVER_PORT))
        self.client = carla.Client(self.CARLA_SERVER_IP, self.CARLA_SERVER_PORT)
        self.client.set_timeout(10.0)

    def loop(self):
        print("Loading world: {}".format("Town02"))
        self.world = self.client.load_world("Town02")

        while True:
            time.sleep(0.5)

if __name__ == '__main__':
    Main().loop()

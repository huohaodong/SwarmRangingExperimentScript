"""
体现距离与测距周期之间的关系
"""

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from matplotlib import pyplot as plt
import time
import logging
import pandas as pd
from multiprocessing import Process
import utils

logging.basicConfig(level=logging.ERROR)

URI0 = 'usb://0'
URI1 = 'radio://0/1/2M'
URI2 = 'radio://0/2/2M'
URI3 = 'radio://0/3/2M'
URI4 = 'radio://0/4/2M'
URI5 = 'radio://0/5/2M'
URI6 = 'radio://0/6/2M'
URI7 = 'radio://0/7/2M'
URI8 = 'radio://0/8/2M'
URI9 = 'radio://0/9/2M'


def move(link_uri, forward=2, back=2, velocity=0.05, height=0.2):
    cflib.crtp.init_drivers()
    with SyncCrazyflie(link_uri=link_uri, cf=Crazyflie(rw_cache="./cache")) as scf:
        with MotionCommander(crazyflie=scf, default_height=height) as mc:
            time.sleep(5)
            mc.forward(distance_m=forward, velocity=velocity)
            time.sleep(2)
            mc.back(distance_m=back, velocity=velocity)
            time.sleep(5)


if __name__ == '__main__':
    log_var = {
        'total_receive': 'uint16_t',
        'total_send': 'uint16_t',
        'total_compute': 'uint16_t'
    }
    move(link_uri=URI3)

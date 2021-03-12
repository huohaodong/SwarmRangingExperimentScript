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


def plot():
    data = pd.read_csv('../data/LAB1.csv')
    data.apply(pd.to_numeric)
    data = data - data.iloc[0]
    # plt.plot(data.diff()['total_compute'] / data['total_compute'])
    plt.plot(data['timestamp'], data['total_compute'])
    plt.xlabel('Time(ms)')
    plt.ylabel('Accumulation')
    plt.savefig('../imgs/LAB1.jpg')
    plt.show()


if __name__ == '__main__':
    log_var = {
        'total_receive': 'uint16_t',
        'total_send': 'uint16_t',
        'total_compute': 'uint16_t'
    }

    # utils.log_ranging(link_uri=URI0, log_cfg_name='TSranging', log_save_path='../data/LAB1.csv',
    #                   log_var=log_var, period_in_ms=100, keep_time_in_s=85)
    plot()

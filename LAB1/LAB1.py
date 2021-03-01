"""
体现距离与测距周期之间的关系
"""

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.positioning.motion_commander import MotionCommander
from matplotlib import pyplot as plt
import time
import logging
import numpy as np
import pandas as pd
from multiprocessing import Process

logging.basicConfig(level=logging.ERROR)

URI0 = 'usb://0'
URI1 = 'radio://0/1/2M'


def log_ranging(link_uri, period_in_ms=100, keep_time_in_s=5):
    plot_timestamp = []
    plot_compute_count = []
    cflib.crtp.init_drivers()
    with SyncCrazyflie(link_uri=link_uri, cf=Crazyflie(rw_cache="./cache")) as scf:

        log_ranging = LogConfig(name='TSranging', period_in_ms=period_in_ms)
        log_ranging.add_variable('TSranging.compute', 'uint16_t')
        log_ranging.add_variable('TSranging.distTo1', 'uint16_t')
        log_ranging.add_variable('TSranging.distTo2', 'uint16_t')
        log_ranging.add_variable('TSranging.distTo3', 'uint16_t')
        with SyncLogger(scf, log_ranging) as logger:
            end_time = time.time() + keep_time_in_s
            for log_entry in logger:
                timestamp = log_entry[0]
                data = log_entry[1]
                logconf_name = log_entry[2]
                plot_timestamp.append(timestamp)
                plot_compute_count.append(data['TSranging.compute'])
                print('编号：{0} | 测距总次数：{1} | 距离：{2} cm'.format(timestamp, data['TSranging.compute'],
                                                              data['TSranging.distTo1']))

                if time.time() > end_time:
                    break

    plot_timestamp = np.asarray(plot_timestamp)
    plot_timestamp -= plot_timestamp[0]
    plot_compute_count = np.asarray(plot_compute_count)
    plot_compute_count -= plot_compute_count[0]

    plt.xlabel('Time(ms)')
    plt.ylabel('Accumulation')
    plt.plot(plot_timestamp, plot_compute_count)
    plt.savefig('../imgs/LAB1.jpg')
    plt.show()

    df = pd.DataFrame(data={'time': plot_timestamp, 'Accumulation': plot_compute_count})
    df.to_csv('../data/LAB1.csv', index=False)
    # print(df)


def move(link_uri, forward=0.4, back=0.4, velocity=0.1, height=0.2):
    with SyncCrazyflie(link_uri=link_uri, cf=Crazyflie(rw_cache="./cache")) as scf:
        with MotionCommander(crazyflie=scf, default_height=height) as mc:
            mc.forward(distance_m=forward, velocity=velocity)
            mc.back(distance_m=back, velocity=velocity)


if __name__ == '__main__':
    log_ranging(link_uri=URI0, period_in_ms=100, keep_time_in_s=15)

"""
TABLE5数据重测
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

URI1 = 'radio://0/1/2M'
URI2 = 'radio://0/2/2M'
URI3 = 'radio://0/3/2M'
URI4 = 'radio://0/4/2M'


def log_ranging(link_uri, period_in_ms=100, keep_time_in_s=5):
    cflib.crtp.init_drivers()

    log_data = pd.DataFrame(
        columns=['timestamp', 'receive_from_1', 'receive_from_2', 'receive_from_3', 'receive_from_4',
                 'compute_from_1', 'compute_from_2', 'compute_from_3', 'compute_from_4',
                 'total_receive', 'total_send', 'total_compute', 'receive_error', 'compute_error'])

    with SyncCrazyflie(link_uri=link_uri, cf=Crazyflie(rw_cache="./cache")) as scf:

        log_ranging = LogConfig(name='TSranging', period_in_ms=period_in_ms)
        log_ranging.add_variable('TSranging.receive_from_1', 'uint16_t')
        log_ranging.add_variable('TSranging.receive_from_2', 'uint16_t')
        log_ranging.add_variable('TSranging.receive_from_3', 'uint16_t')
        log_ranging.add_variable('TSranging.receive_from_4', 'uint16_t')

        log_ranging.add_variable('TSranging.compute_from_1', 'uint16_t')
        log_ranging.add_variable('TSranging.compute_from_2', 'uint16_t')
        log_ranging.add_variable('TSranging.compute_from_3', 'uint16_t')
        log_ranging.add_variable('TSranging.compute_from_4', 'uint16_t')

        log_ranging.add_variable('TSranging.total_receive', 'uint16_t')
        log_ranging.add_variable('TSranging.total_send', 'uint16_t')
        log_ranging.add_variable('TSranging.total_compute', 'uint16_t')
        log_ranging.add_variable('TSranging.receive_error', 'uint16_t')
        log_ranging.add_variable('TSranging.compute_error', 'uint16_t')

        with SyncLogger(scf, log_ranging) as logger:
            end_time = time.time() + keep_time_in_s
            for log_entry in logger:
                timestamp = log_entry[0]
                data = log_entry[1]
                logconf_name = log_entry[2]

                temp = {'timestamp': timestamp,
                        'receive_from_1': data['TSranging.receive_from_1'],
                        'receive_from_2': data['TSranging.receive_from_2'],
                        'receive_from_3': data['TSranging.receive_from_3'],
                        'receive_from_4': data['TSranging.receive_from_4'],
                        'compute_from_1': data['TSranging.compute_from_1'],
                        'compute_from_2': data['TSranging.compute_from_2'],
                        'compute_from_3': data['TSranging.compute_from_3'],
                        'compute_from_4': data['TSranging.compute_from_4'],
                        'total_receive': data['TSranging.total_receive'],
                        'total_send': data['TSranging.total_send'],
                        'total_compute': data['TSranging.total_compute'],
                        'receive_error': data['TSranging.receive_error'],
                        'compute_error': data['TSranging.compute_error']
                        }
                log_data = log_data.append(temp, ignore_index=True)
                # print(log_data.iloc[log_data.shape[0] - 1, :])
                print(temp)
                if time.time() > end_time:
                     break

                log_data.to_csv('../data/LAB2.csv', index=False)


if __name__ == '__main__':
    log_ranging(link_uri=URI1, period_in_ms=100, keep_time_in_s=360)
    # data = pd.read_csv('../data/LAB2.csv')
    # data = data.apply(pd.to_numeric)


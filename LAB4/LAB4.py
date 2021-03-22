"""
Figure12数据重测
"""

import logging
import pandas as pd
import utils
from matplotlib import pyplot as plt
import time

logging.basicConfig(level=logging.ERROR)

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
    average_count_ring = [8218, 3428, 2107, 1386, 1035, 771, 555]
    average_count_50ms = [2738, 2623, 2572, 2505, 2398, 2320, 2219]
    average_count_100ms = [1670, 1650, 1587, 1573, 1506, 1446, 1437]
    average_count_150ms = [1160, 1148, 1127, 1127, 1091, 1063, 1074]
    legend_labels = [
        'token ring',
        'swarm ranging P=50ms',
        'swarm ranging P=100ms',
        'swarm ranging P=150ms'
    ]
    plt.plot(range(3, 10), average_count_ring)
    plt.plot(range(3, 10), average_count_50ms)
    plt.plot(range(3, 10), average_count_100ms)
    plt.plot(range(3, 10), average_count_150ms)
    plt.legend(legend_labels, framealpha=0)
    plt.xlabel('Number of drones')
    plt.ylabel('Average ranging count')
    plt.savefig('../imgs/LAB4.jpg')
    plt.show()


if __name__ == '__main__':
    log_var = {
        'total_receive': 'uint16_t',
        'total_send': 'uint16_t',
        'total_compute': 'uint16_t'
    }

    # utils.log_ranging(link_uri=URI2, log_cfg_name='TSranging', log_save_path='../data/LAB4.csv',
    #                   log_var=log_var, period_in_ms=100, keep_time_in_s=220)
    plot()

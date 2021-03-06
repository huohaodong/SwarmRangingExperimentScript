"""
Figure11数据重测
"""

import logging
import pandas as pd
import utils
from matplotlib import pyplot as plt

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
    log_dirs = [
        '../data/LAB4_50ms_3.csv', '../data/LAB4_50ms_4.csv', '../data/LAB4_50ms_5.csv', '../data/LAB4_50ms_6.csv',
        '../data/LAB4_100ms_3.csv', '../data/LAB4_100ms_4.csv', '../data/LAB4_100ms_5.csv', '../data/LAB4_100ms_6.csv',
        '../data/LAB4_150ms_3.csv', '../data/LAB4_150ms_4.csv', '../data/LAB4_150ms_5.csv', '../data/LAB4_150ms_6.csv'
    ]
    average_ranging_count = {}
    for log_dir in log_dirs:
        data = pd.read_csv(log_dir)
        data.apply(pd.to_numeric)
        data = data - data.iloc[0]
        n_uav = int(log_dir.split('_')[-1].rstrip('.csv'))  # 无人机数量
        f_uav = int(log_dir.split('_')[-2].rstrip('ms'))  # 测距信息发送频率
        if f_uav not in average_ranging_count.keys():
            average_ranging_count[f_uav] = {}

        if n_uav not in average_ranging_count[f_uav].keys():
            average_ranging_count[f_uav][n_uav] = []

        average_ranging_count[f_uav][n_uav].append(data.loc[data.shape[0] - 1, 'total_compute'] / (n_uav - 1))
    # print(average_ranging_count)

    legend_labels = [
        'swarm ranging P=50ms',
        'swarm ranging P=100ms',
        'swarm ranging P=150ms',
    ]
    for x in average_ranging_count:
        print(x)

    for k, v in average_ranging_count.items():
        plt.plot(average_ranging_count[k].keys(), average_ranging_count[k].values())

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

    utils.log_ranging(link_uri=URI4, log_cfg_name='TSranging', log_save_path='../data/LAB4_150ms_3.csv', log_var=log_var,
                      period_in_ms=100, keep_time_in_s=200)

    plot()

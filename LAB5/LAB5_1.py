"""
上下车机制实验1
周期设为50，5架无人机，座位数为3
"""

import logging
import pandas as pd
import utils
from matplotlib import pyplot as plt
import time
import numpy as np

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
URI10 = 'radio://0/10/2M'
URI11 = 'radio://0/11/2M'
URIS = [URI1, URI2, URI3, URI4, URI5, URI6, URI7, URI8, URI9, URI10, URI11]


def plot(before, after, labels=['A', 'B', 'C', 'D', 'E']):
    data = np.asarray([before, after])
    data = pd.DataFrame(data=data, dtype='float64', columns=labels)
    print(data)
    data = data / (len(labels) - 1)
    # 绘图
    data.T.plot(kind='bar')
    plt.xticks(fontproperties='Times New Roman', rotation=0)
    plt.ylabel('Average Ranging Count')
    plt.legend(['before', 'after'], framealpha=0)
    # plt.savefig('../imgs/LAB5-1.jpg')
    plt.show()


if __name__ == '__main__':
    log_var = {
        'total_receive': 'uint16_t',
        'total_send': 'uint16_t',
        'total_compute': 'uint16_t'
    }
    data1 = []
    data2 = []
    for URI in URIS:
        temp = utils.log_ranging(link_uri=URI,
                                 log_cfg_name='TSranging',
                                 log_var=log_var,
                                 period_in_ms=100,
                                 keep_time_in_s=2)
        data1.append(temp['total_compute'][temp.shape[0] - 1])

    time.sleep(180)
    for URI in URIS:
        temp = utils.log_ranging(link_uri=URI,
                                 log_cfg_name='TSranging',
                                 log_var=log_var,
                                 period_in_ms=100,
                                 keep_time_in_s=2)
        data2.append(temp['total_compute'][0])
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    result = np.asarray([data1, data2])
    result = (result - result[0])[-1]
    print(result)

    # plot(before=data1, after=data2, labels=labels)

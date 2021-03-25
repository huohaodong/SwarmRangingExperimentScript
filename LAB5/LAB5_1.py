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
# URIS = [URI1, URI2, URI3, URI4, URI5, URI6, URI7, URI8, URI9, URI10, URI11]
URIS = [URI1, URI2, URI3, URI4, URI5]


def plot(before, after, labels=['A', 'B', 'C', 'D', 'E'], img_save_path='./default.jpg'):
    data = np.asarray([before, after])
    data = pd.DataFrame(data=data, dtype='float64', columns=labels)
    print(data)
    data = data / (len(labels) - 1)
    # 绘图
    data.T.plot(kind='bar')
    plt.xticks(fontproperties='Times New Roman', rotation=0)
    plt.ylabel('Average Ranging Count')
    plt.legend(['before', 'after'], framealpha=0)
    plt.savefig(img_save_path)
    plt.show()


if __name__ == '__main__':
    # log_var = {
    #     'total_receive': 'uint16_t',
    #     'total_send': 'uint16_t',
    #     'total_compute': 'uint16_t'
    # }
    # data1 = []
    # data2 = []
    # for URI in URIS:
    #     temp = utils.log_ranging(link_uri=URI,
    #                              log_cfg_name='TSranging',
    #                              log_var=log_var,
    #                              period_in_ms=100,
    #                              keep_time_in_s=2)
    #     data1.append(temp['total_compute'][temp.shape[0] - 1])
    #
    # time.sleep(192)
    # for URI in URIS:
    #     temp = utils.log_ranging(link_uri=URI,
    #                              log_cfg_name='TSranging',
    #                              log_var=log_var,
    #                              period_in_ms=100,
    #                              keep_time_in_s=2)
    #     data2.append(temp['total_compute'][0])
    # labels = ['A', 'B', 'C', 'D', 'E']
    # result = np.asarray([data1, data2])
    # result = (result - result[0])[-1]
    # print(result)
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

    before1 = np.asarray([[29442, 30461, 30873, 29836, 28143, 29186, 28904, 26506, 17850, 9560, 2739],
                          [28408, 26336, 28707, 27299, 25902, 28546, 28494, 26501, 19557, 10028, 3831],
                          [28531, 29451, 28056, 29113, 26777, 30279, 28985, 26414, 17715, 9737, 3934],
                          [28579, 28257, 25557, 29575, 26829, 28669, 29722, 26800, 19910, 9325, 2991]]).mean(axis=0)
    # before1 = np.sort(before1)[::-1]
    after1 = np.asarray([[24980, 27120, 24847, 20560, 25140, 25283, 19535, 18103, 24232, 26027, 24825],
                         [26988, 27632, 24140, 24241, 25231, 16428, 16662, 20942, 24872, 26320, 28331],
                         [27479, 25809, 25108, 27069, 24197, 19607, 24050, 19317, 23085, 22617, 16891],
                         [23089, 28748, 22934, 22805, 27505, 22208, 21801, 16505, 25711, 25432, 27746],
                         [27073, 23548, 19353, 16620, 27695, 25429, 20724, 23340, 23828, 25304, 25932],
                         [26146, 26055, 21214, 25937, 26673, 21542, 17081, 21306, 28027, 19650, 23119],
                         [27505, 27943, 21122, 19839, 29636, 26426, 17212, 16811, 28220, 26531, 21820],
                         [26484, 27459, 24676, 24609, 25099, 26928, 24674, 16993, 25397, 19131, 18934],
                         [17586, 20565, 23955, 21667, 26076, 24902, 25323, 23460, 25180, 28850, 23326],
                         [27109, 17045, 26012, 23447, 28375, 19693, 16284, 28420, 25960, 25359, 28270],
                         [28114, 28199, 26760, 19938, 29715, 24878, 24296, 19053, 25736, 20347, 19055],
                         [21001, 25695, 26582, 28806, 16694, 16700, 27932, 24042, 23759, 24663, 24808]]).mean(axis=0)
    # after1 = np.sort(after1)[::-1]
    plot(before=before1, after=after1, labels=labels, img_save_path='../imgs/LAB5-1.jpg')

    before2 = np.asarray([[8493, 9239, 10092, 10722, 11557, 12444, 13426, 14385, 13088, 11274, 8862],
                          [8623, 9206, 10019, 10690, 11412, 12537, 13491, 14545, 13233, 11368, 8881],
                          [8615, 9356, 9988, 10723, 11528, 12666, 13613, 14618, 13204, 11256, 8769],
                          [8618, 9273, 10053, 10706, 11561, 12645, 13572, 14513, 13186, 11254, 8830],
                          [8629, 9313, 10108, 10797, 11700, 12661, 13586, 14580, 13091, 11297, 8870]]).mean(axis=0)
    after2 = np.asarray([[7293, 7617, 8144, 8454, 8990, 9931, 11032, 14679, 15739, 16693, 16763],
                         [7368, 7541, 8118, 8440, 9053, 10019, 10976, 14557, 15693, 16605, 16760],
                         [7268, 7628, 8083, 8479, 9085, 9922, 10991, 14623, 15666, 16681, 16764],
                         [7282, 7696, 8110, 8326, 9049, 9975, 10958, 14575, 15693, 16731, 16758]
                         ]).mean(axis=0)
    plot(before=before2, after=after2, labels=labels, img_save_path='../imgs/LAB5-2.jpg')

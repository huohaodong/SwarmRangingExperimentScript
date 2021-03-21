"""
上下车机制实验1
周期不同 30 60 90 120 150，5架无人机，座位数为3
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
    # 开启上下车前
    data1_1 = pd.read_csv('../data/LAB5_2_1_A.csv').apply(pd.to_numeric)
    data2_1 = pd.read_csv('../data/LAB5_2_1_B.csv').apply(pd.to_numeric)
    data3_1 = pd.read_csv('../data/LAB5_2_1_C.csv').apply(pd.to_numeric)
    data4_1 = pd.read_csv('../data/LAB5_2_1_D.csv').apply(pd.to_numeric)
    data5_1 = pd.read_csv('../data/LAB5_2_1_E.csv').apply(pd.to_numeric)

    data1_1 = (data1_1 - data1_1.iloc[0]).iloc[1000]
    data2_1 = (data2_1 - data2_1.iloc[0]).iloc[1000]
    data3_1 = (data3_1 - data3_1.iloc[0]).iloc[1000]
    data4_1 = (data4_1 - data4_1.iloc[0]).iloc[1000]
    data5_1 = (data5_1 - data5_1.iloc[0]).iloc[1000]

    # 开启上下车后
    # data1_2 = pd.read_csv('../data/LAB5_2_2_A.csv').apply(pd.to_numeric)
    # data2_2 = pd.read_csv('../data/LAB5_2_2_B.csv').apply(pd.to_numeric)
    # data3_2 = pd.read_csv('../data/LAB5_2_2_C.csv').apply(pd.to_numeric)
    # data4_2 = pd.read_csv('../data/LAB5_2_2_D.csv').apply(pd.to_numeric)
    # data5_2 = pd.read_csv('../data/LAB5_2_2_E.csv').apply(pd.to_numeric)
    #
    # data1_2 = (data1_2 - data1_2.iloc[0]).iloc[1000]
    # data2_2 = (data2_2 - data2_2.iloc[0]).iloc[1000]
    # data3_2 = (data3_2 - data3_2.iloc[0]).iloc[1000]
    # data4_2 = (data4_2 - data4_2.iloc[0]).iloc[1000]
    # data5_2 = (data5_2 - data5_2.iloc[0]).iloc[1000]

    # 整合数据
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame(dtype='float64', columns=labels)
    data = data.append({
        'A': data1_1['total_compute'] / (len(labels) - 1), 'B': data2_1['total_compute'] / (len(labels) - 1),
        'C': data3_1['total_compute'] / (len(labels) - 1), 'D': data4_1['total_compute'] / (len(labels) - 1),
        'E': data5_1['total_compute'] / (len(labels) - 1)
    }, ignore_index=True)
    # data = data.append({
    #     'A': data1_2['total_compute'] / (len(labels) - 1), 'B': data2_2['total_compute'] / (len(labels) - 1),
    #     'C': data3_2['total_compute'] / (len(labels) - 1), 'D': data4_2['total_compute'] / (len(labels) - 1),
    #     'E': data5_2['total_compute'] / (len(labels) - 1)
    # }, ignore_index=True)
    # 绘图
    data.T.plot(kind='bar')
    plt.xticks(fontproperties='Times New Roman', rotation=0)
    plt.ylabel('Average Ranging Count')
    # plt.legend(['before', 'after'], framealpha=0)
    plt.savefig('../imgs/LAB5-2.jpg')
    plt.show()


if __name__ == '__main__':
    log_var = {
        'receive_from_2': 'uint16_t',
        'receive_from_3': 'uint16_t',
        'receive_from_4': 'uint16_t',
        'receive_from_5': 'uint16_t',
        'compute_from_2': 'uint16_t',
        'compute_from_3': 'uint16_t',
        'compute_from_4': 'uint16_t',
        'compute_from_5': 'uint16_t',
        'total_receive': 'uint16_t',
        'total_send': 'uint16_t',
        'total_compute': 'uint16_t'
    }
    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_1_A.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=120)
    # utils.log_ranging(link_uri=URI2, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_1_B.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=115)
    # utils.log_ranging(link_uri=URI3, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_1_C.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI4, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_1_D.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI5, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_1_E.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_2_A.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI2, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_2_B.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI3, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_2_C.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI4, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_2_D.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    # utils.log_ranging(link_uri=URI5, log_cfg_name='TSranging', log_save_path='../data/LAB5_2_2_E.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=110)
    plot()

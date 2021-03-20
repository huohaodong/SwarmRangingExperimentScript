"""
上下车机制实验1
相同距离，相同周期，5架无人机，座位数为3
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
    data1 = pd.read_csv('../data/LAB5_1_1_A.csv')
    data2 = pd.read_csv('../data/LAB5_1_1_B.csv')
    data3 = pd.read_csv('../data/LAB5_1_1_C.csv')
    data4 = pd.read_csv('../data/LAB5_1_1_D.csv')
    data5 = pd.read_csv('../data/LAB5_1_1_E.csv')
    data1.apply(pd.to_numeric)
    data2.apply(pd.to_numeric)
    data3.apply(pd.to_numeric)
    data4.apply(pd.to_numeric)
    data5.apply(pd.to_numeric)
    data1 = (data1 - data1.iloc[0]).iloc[-1]
    data2 = (data2 - data2.iloc[0]).iloc[-1]
    data3 = (data3 - data3.iloc[0]).iloc[-1]
    data4 = (data4 - data4.iloc[0]).iloc[-1]
    data5 = (data5 - data5.iloc[0]).iloc[-1]
    print(data1)
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.Series(dtype='float64')
    data['A'] = data1['total_compute'] / (len(labels) - 1)
    data['B'] = data2['total_compute'] / (len(labels) - 1)
    data['C'] = data3['total_compute'] / (len(labels) - 1)
    data['D'] = data4['total_compute'] / (len(labels) - 1)
    data['E'] = data5['total_compute'] / (len(labels) - 1)
    data.plot(kind='bar')
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
    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_1_A.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=70)
    # utils.log_ranging(link_uri=URI2, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_1_B.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=70)
    # utils.log_ranging(link_uri=URI3, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_1_C.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=70)
    # utils.log_ranging(link_uri=URI4, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_1_D.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=70)
    # utils.log_ranging(link_uri=URI5, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_1_E.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=70)
    utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_2_A.csv', log_var=log_var,
                      period_in_ms=100, keep_time_in_s=70)
    utils.log_ranging(link_uri=URI2, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_2_B.csv', log_var=log_var,
                      period_in_ms=100, keep_time_in_s=70)
    utils.log_ranging(link_uri=URI3, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_2_C.csv', log_var=log_var,
                      period_in_ms=100, keep_time_in_s=70)
    utils.log_ranging(link_uri=URI4, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_2_D.csv', log_var=log_var,
                      period_in_ms=100, keep_time_in_s=70)
    utils.log_ranging(link_uri=URI5, log_cfg_name='TSranging', log_save_path='../data/LAB5_1_2_E.csv', log_var=log_var,
                      period_in_ms=100, keep_time_in_s=70)
    # plot()

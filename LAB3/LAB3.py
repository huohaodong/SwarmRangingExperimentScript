"""
Figure11数据重测
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


def plot():
    data1 = pd.read_csv('../data/LAB3_AB.csv')
    data2 = pd.read_csv('../data/LAB3_AC.csv')
    data3 = pd.read_csv('../data/LAB3_AD.csv')
    data4 = pd.read_csv('../data/LAB3_SWARM.csv')
    data1.apply(pd.to_numeric)
    data2.apply(pd.to_numeric)
    data3.apply(pd.to_numeric)
    data4.apply(pd.to_numeric)
    data1 = data1 - data1.iloc[0]
    data2 = data2 - data2.iloc[0]
    data3 = data3 - data3.iloc[0]
    data4 = data4 - data4.iloc[0]
    compute_from_2 = data1.loc[0:2000, 'compute_from_2']
    compute_from_3 = data2.loc[0:2000, 'compute_from_3']
    compute_from_4 = data3.loc[0:2000, 'compute_from_4']
    swarm_compute_from_2 = data4.loc[0:2000, 'compute_from_2']
    swarm_compute_from_3 = data4.loc[0:2000, 'compute_from_3']
    swarm_compute_from_4 = data4.loc[0:2000, 'compute_from_4']

    legend_labels = ['$\mathregular{P_A}$=30ms,$\mathregular{P_B}$=40ms,swarm of ABCD',
                     '$\mathregular{P_A}$=30ms,$\mathregular{P_C}$=50ms,swarm of ABCD',
                     '$\mathregular{P_A}$=30ms,$\mathregular{P_D}$=60ms,swarm of ABCD',
                     '$\mathregular{P_A}$=30ms,$\mathregular{P_B}$=40ms,pair of AB',
                     '$\mathregular{P_A}$=30ms,$\mathregular{P_C}$=50ms,pair of AC',
                     '$\mathregular{P_A}$=30ms,$\mathregular{P_D}$=60ms,pair of AD',
                     ]
    plt.plot(swarm_compute_from_2, c='tab:blue')
    plt.plot(swarm_compute_from_3, c='tab:orange')
    plt.plot(swarm_compute_from_4, c='tab:green')
    plt.plot(compute_from_2, '--')
    plt.plot(compute_from_3, '--')
    plt.plot(compute_from_4, '--')
    plt.xlabel('Time(100ms)')
    plt.ylabel('Ranging count')
    plt.legend(legend_labels, loc='upper left', framealpha=0)
    plt.savefig('../imgs/LAB3.jpg')
    plt.show()


if __name__ == '__main__':
    log_var = {'receive_from_1': 'uint16_t',
               'receive_from_2': 'uint16_t',
               'receive_from_3': 'uint16_t',
               'receive_from_4': 'uint16_t',
               'compute_from_1': 'uint16_t',
               'compute_from_2': 'uint16_t',
               'compute_from_3': 'uint16_t',
               'compute_from_4': 'uint16_t',
               'total_receive': 'uint16_t',
               'total_send': 'uint16_t',
               'total_compute': 'uint16_t'}


    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB3_AB.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=210)
    #
    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB3_AC.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=210)

    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB3_AD.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=210)
    #
    # utils.log_ranging(link_uri=URI1, log_cfg_name='TSranging', log_save_path='../data/LAB3_SWARM.csv', log_var=log_var,
    #                   period_in_ms=100, keep_time_in_s=210)

    plot()

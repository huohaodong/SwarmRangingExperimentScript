#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2019 Bitcraze AB
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.
"""
Simple example of a synchronized swarm choreography using the High level
commander.

The swarm takes off and flies a synchronous choreography before landing.
The take-of is relative to the start position but the Goto are absolute.
The sequence contains a list of commands to be executed at each step.

This example is intended to work with any absolute positioning system.
It aims at documenting how to use the High Level Commander together with
the Swarm class to achieve synchronous sequences.
"""
import threading
import time
from collections import namedtuple
from queue import Queue

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import math
import utils
# Time for one step in second
from cflib.positioning.position_hl_commander import PositionHlCommander

STEP_TIME = 1
uris = [
    'radio://0/1/2M/E7E7E7E7E7',
    'radio://0/2/2M/E7E7E7E7E7',
    # Add more URIs if you want more copters in the swarm
]
ht=0.5
record_time = 100#记录时间
velocity = 0.5
circle_center=(-0.5,0.2)#圆心
radius = 1.5#半径
radius_step = math.pi/30
sequence1 = [
    (circle_center[0], circle_center[1], ht, 140),
]
sequence2 = [
    (radius+circle_center[0], circle_center[1], ht, 5),
]
sequence2 = sequence2

seq_args = {
    uris[0]: [sequence1],
    uris[1]: [sequence2],
}
def wait_for_position_estimator(scf):
    print('Waiting for estimator to find position...')

    log_config = LogConfig(name='Kalman Variance', period_in_ms=500)
    log_config.add_variable('kalman.varPX', 'float')
    log_config.add_variable('kalman.varPY', 'float')
    log_config.add_variable('kalman.varPZ', 'float')

    var_y_history = [1000] * 10
    var_x_history = [1000] * 10
    var_z_history = [1000] * 10

    threshold = 0.001

    with SyncLogger(scf, log_config) as logger:
        for log_entry in logger:
            data = log_entry[1]

            var_x_history.append(data['kalman.varPX'])
            var_x_history.pop(0)
            var_y_history.append(data['kalman.varPY'])
            var_y_history.pop(0)
            var_z_history.append(data['kalman.varPZ'])
            var_z_history.pop(0)

            min_x = min(var_x_history)
            max_x = max(var_x_history)
            min_y = min(var_y_history)
            max_y = max(var_y_history)
            min_z = min(var_z_history)
            max_z = max(var_z_history)

            # print("{} {} {}".
            #       format(max_x - min_x, max_y - min_y, max_z - min_z))

            if (max_x - min_x) < threshold and (
                    max_y - min_y) < threshold and (
                    max_z - min_z) < threshold:
                break


def reset_estimator(scf):
    cf = scf.cf
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')
    wait_for_position_estimator(scf)


def activate_high_level_commander(scf):
    scf.cf.param.set_value('commander.enHighLevel', '1')


def activate_mellinger_controller(scf, use_mellinger):
    controller = 1
    if use_mellinger:
        controller = 2
    scf.cf.param.set_value('stabilizer.controller', str(controller))


def crazyflie_control(scf,sequence):
    log_var = {
        # 'total_receive': 'uint32_t',
        # 'total_send': 'uint32_t',
        'total_compute': 'uint32_t'
    }
    cf = scf.cf

    with PositionHlCommander(scf) as pc:
        if cf.link_uri == uris[0]: #固定点
            for ele in sequence:
                pc.go_to(ele[0], ele[1], ele[2])
                time.sleep(ele[3])
        else:   #旋转点
            for ele in sequence:
                pc.go_to(ele[0], ele[1], ele[2])
                time.sleep(ele[3])
            #设置新的config
            log_cfg = LogConfig(name='TSranging', period_in_ms=100)
            for log_var_name, log_var_type in log_var.items():
                log_cfg.add_variable(log_cfg.name + '.' + log_var_name, log_var_type)
            data1 = []
            data2 = []
            ######################记录log#########################
            with SyncLogger(scf,log_cfg) as logger:
                end_time = time.time() + 2
                while time.time() < end_time:
                    continue
                for i in range(logger._queue.qsize()):
                    log_entry = logger.next()
                    timestamp = log_entry[0]
                    data = log_entry[1]
                    logconf_name = log_entry[2]
                    temp = {}
                    temp['timestamp'] = timestamp
                    for log_var_name, log_var_type in log_var.items():
                        temp[log_var_name] = data[log_cfg.name + '.' + log_var_name]
                    data1.append(temp)
            cnt_begin= data1[-1]['total_compute']
            ###########################################

            ##########################开始转圈######################
            end_time = time.time() + record_time
            step_cnt = 0
            while time.time() < end_time:
                pc.go_to(circle_center[0]+radius*math.cos(step_cnt*radius_step),circle_center[1]+radius*math.sin(step_cnt*radius_step),ht,velocity)
                step_cnt = step_cnt + 1
            #####################记录log###################
            with SyncLogger(scf,log_cfg) as logger:
                end_time = time.time() + 2
                while time.time() < end_time:
                    continue
                for i in range(logger._queue.qsize()):
                    log_entry = logger.next()
                    timestamp = log_entry[0]
                    data = log_entry[1]
                    logconf_name = log_entry[2]
                    temp = {}
                    temp['timestamp'] = timestamp
                    for log_var_name, log_var_type in log_var.items():
                        temp[log_var_name] = data[log_cfg.name + '.' + log_var_name]
                    data2.append(temp)
            cnt_end = data2[0]['total_compute']
            ##############################################
            print(cnt_end - cnt_begin)

if __name__ == '__main__':

    cflib.crtp.init_drivers(enable_debug_driver=False)
    factory = CachedCfFactory(rw_cache='./cache')
    for uri in uris:
        with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
            with PositionHlCommander(scf) as pc:
                time.sleep(2)
    with Swarm(uris, factory=factory) as swarm:
        swarm.parallel_safe(activate_high_level_commander)
        swarm.parallel_safe(reset_estimator)
        print('Starting sequence!')
        swarm.parallel_safe(crazyflie_control,args_dict=seq_args)
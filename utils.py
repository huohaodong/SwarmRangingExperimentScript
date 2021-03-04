import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import time
import logging
import pandas as pd

logging.basicConfig(level=logging.ERROR)


def log_ranging(link_uri, log_cfg_name='TSranging', log_var={}, log_save_path="./default.csv", period_in_ms=100,
                keep_time_in_s=5):
    cflib.crtp.init_drivers()
    log_data = pd.DataFrame(columns=log_var.keys())

    with SyncCrazyflie(link_uri=link_uri, cf=Crazyflie(rw_cache="./cache")) as scf:
        log_cfg = LogConfig(name=log_cfg_name, period_in_ms=period_in_ms)
        for log_var_name, log_var_type in log_var.items():
            log_cfg.add_variable(log_cfg.name + '.' + log_var_name, log_var_type)

        with SyncLogger(scf, log_cfg) as logger:
            end_time = time.time() + keep_time_in_s
            for log_entry in logger:
                timestamp = log_entry[0]
                data = log_entry[1]
                logconf_name = log_entry[2]

                temp = {}
                temp['timestamp'] = timestamp
                for log_var_name, log_var_type in log_var.items():
                    temp[log_var_name] = data[log_cfg.name + '.' + log_var_name]

                log_data = log_data.append(temp, ignore_index=True)
                print(temp)
                if time.time() > end_time:
                    break

    log_data.to_csv(log_save_path, index=False)

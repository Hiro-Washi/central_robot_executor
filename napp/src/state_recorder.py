#!/usr/bin/env python3

import yaml
import time
from datetime import datetime
import rospy


class MemoryStore():
    def __init__(self):
        
        rospy.Service("/memory/state", , )
    def stateCB(self, msg):
    def recordStateData(robot_state, environment_state, interval=5):
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {
                'timestamp': timestamp,
                '':,
                'navi_location': ,
                'belongings': ,
                'arm_pose': ,
                'order_task_name': ,
                'order_task_stete': ,
                'my_task_state': ,
                'environment_state': environment_state
                "battery level": ,
                "centimental": ,
                "operation_mode": 
            }
            with open(data_dir+'/state.yaml', 'a') as file:
                yaml.dump(data, file)
            time.sleep(interval)

# 例として初期のロボットの状態と環境の状態を設定
initial_robot_state = {
    'position': [0, 0],
    'battery_level': 100,
    'sensor_data': {},
    'task': 'Standby'
}

initial_environment_state = {
    'obstacles': [],
    'weather': 'Sunny',
    'surrounding_objects': [],
    'ambient_sound': 'Quiet'
}

record_robot_data(initial_robot_state, initial_environment_state)


if __name__ == '__main__':
    
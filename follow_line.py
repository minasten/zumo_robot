from behaviour import *

class FollowLine(Behavior):

    def __init__(self, priority=0.3):
        super().__init__(self, priority=priority)   # One sensob, value an array of active sensors
        self.match_degree = 0.5

    def __str__(self):
        return "Follow line"

    def consider_deactivation(self):
        # Deactivate if no no line detected
        if not self.sensobs[0].get_value():
            self.active_flag = False
            self.match_degree = 0
            self.motor_recommendations = []

    def consider_activation(self):
        # Activate if detect line
        if self.sensobs[0].get_value():
            self.active_flag = True

    def sense_and_act(self):
        sensor_array = self.sensobs[0].get_value()
        new_sensor_array = [0]*6
        for i in sensor_array:
            new_sensor_array[sensor_array[i]] = 1
        if sensor_array[0]:
            self.motor_recommendations = ['L', 0.3]
        elif sensor_array[5]:
            self.motor_recommendations = ['R', 0.3]
        elif sensor_array[1]:
            self.motor_recommendations = ['l', 0.15]
        elif sensor_array[4]:
            self.motor_recommendations = ['R', 0.15]
        elif sensor_array[3] or sensor_array[2]:
            self.motor_recommendations = ['F', 0.4]


from behaviour import *

class Bull(Behavior):

    def __init__(self):
        super(Bull, self).__init__(self, priority=0.8)     #one sensob, sensob.value: percentage of red
        self.red_percentage_trigger = 15

    def __str__(self):
        return "Bull"

    def consider_deactivation(self):
        if self.sensobs.get_value() < self.red_percentage_trigger:
            self.active_flag = False
            self.match_degree = 0
            self.motor_recommendations = []

    def consider_activation(self):
        if self.sensobs.get_value() >= self.red_percentage_trigger:
            self.active_flag = True

    def sense_and_act(self):
        self.match_degree = self.sensobs.get_value()/100 * 4
        self.motor_recommendations = ['F', 0.8]

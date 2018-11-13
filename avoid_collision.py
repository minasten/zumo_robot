from behaviour import *

class AvoidCollision(Behavior):

    #If object is close - complete stop

    def __init__(self):
        super().__init__(self, priority=0.6)
        self.motor_recommendations = []
        self.stop_distance = 10

    def __str__(self):
        return "Avoid Collision"

    def consider_deactivation(self):
        if self.sensobs.get_value() > self.stop_distance:
            self.active_flag = False
            self.match_degree = 0
            self.motor_recommendations = []

    def consider_activation(self):
        if self.sensobs.get_value() <= self.stop_distance:
            self.active_flag = True

    def sense_and_act(self):
        self.match_degree = max((self.stop_distance - self.sensobs.get_value()), 0) / self.stop_distance
        self.motor_recommendations = ['S']


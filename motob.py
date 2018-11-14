#Interface between a behavior and one or more motors
from motors import *

class Motob():

    def __init__(self):
        self.motors = Motors()                      #List of the motors, settings will be determined by this class
        self.value = []                             #Holder of most recent motor recommendations

    #Receives a new recommendation, loads to the value slot and operationalizes it
    #new_rec = [function, speed] where speed is in range [-1,1]
    def update(self, new_rec):
        self.value = [new_rec]
        self.operationalize(new_rec)

    #Converts a motor recommendation into motor settings, which are sent to the corresponing motors
    def operationalize(self, new_rec):
        if new_rec in self.value:
            if new_rec[0] == "F":
                self.motors.forward(new_rec[1], 0.2)
            elif new_rec[0] == "B":
                self.motors.backward(new_rec[1], 0.2)
            elif new_rec[0] == "S":
                self.motors.stop()
            elif new_rec[0] == "L":
                self.motors.set_value([0, new_rec[1]], 0.8)
            elif new_rec[0] == "R":
                self.motors.set_value([new_rec[1], 0], 0.8)
            elif new_rec[0] == "TL":
                self.motors.left(new_rec[1], 1)
            elif new_rec[0] == "TR":
                self.motors.right(new_rec[1], 1)

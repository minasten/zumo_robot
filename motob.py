#Interface between a behavior and one or more motors
from motors import *

class Motob():

    def __init__(self):
        self.motors = Motors()
        self.value = []


    def update(self, new_rec):
        self.value = [new_rec]
        self.operationalize(new_rec)


    def operationalize(self, new_rec):
        if new_rec in self.value:
            if new_rec[0] == "F":
                self.motors.forward(new_rec[1], 1)
            elif new_rec[0] == "B":
                self.motors.backward(new_rec[1], 1)
            elif new_rec[0] == "L":
                self.motors.left(new_rec[1], 1)
            elif new_rec[0] == "R":
                self.motors.right(new_rec[1], 1)
            elif new_rec[0] == "S":
                self.motors.stop()




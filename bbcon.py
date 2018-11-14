from time import sleep as sleep
from arbitrator import *

class Bbcon:
    def __init__(self, sensobs, motobs, arbitrator, behaviours=[], active_behaviours=[]):
        self.behaviours = behaviours                    # a list of all the behavior objects used by the bbcon
        self.active_behaviours = active_behaviours      # a list of all behaviors that are currently active
        self.sensobs = sensobs                          # a list of all sensory objects used by the bbcon
        self.motobs = motobs                            # a list of all motor objects used by the bbcon
        self.arbitrator = arbitrator                    # Arbitrator will resolve actuator request produced by behaviors

    def add_behaviour(self, behaviour):                  # append a newly-created behavior onto the behaviors list
        self.behaviours.append(behaviour)

    def add_sensob(self, sensob):                        # append a newly-created sensob onto the sensobs list
        self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):             # add an existing behavior onto the active-behaviors list
        self.active_behaviours.append(behaviour)
        print("Activated " + str(behaviour))

    def deactivate_behaviour(self, behaviour):           # remove an existing behavior from the active behaviors list
        self.active_behaviours.remove(behaviour)
        print("Deactivated " + str(behaviour))

    def __str__(self):
        return str(self.behaviours + self.active_behaviours + self.sensobs + self.motobs)    #self.arbitrator

    def update_all_sensobs(self):
        for s in self.sensobs:
            #print(s)
            s.update()

    def update_all_behaviours(self):
        for b in self.behaviours:
            b.update()
            if b.active_flag and b not in self.active_behaviours:
                self.activate_behaviour(b)
            elif not b.active_flag and b in self.active_behaviours:
                self.deactivate_behaviour(b)

    def run_one_timestep(self):

        self.update_all_sensobs()
        self.update_all_behaviours()

        best_behaviour, halt = self.arbitrator.choose_action(self.active_behaviours)

        print("Active behaviours and weight: ")
        for b in self.active_behaviours:
            print(str(b) + " " + str(b.weight))

        print("Best behaviour: " + str(best_behaviour))

        #if halt:
            #print("Halt request")
            #self.motobs[0].stop

        #for i in self.motobs:
        self.motobs[0].update(best_behaviour)

        sleep(0.01)

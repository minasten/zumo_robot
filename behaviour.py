
class Behavior:

    def __init__(self, active_flag=True, priority=1):
        self.motor_recommendations = []      # List of recommendations the behavior provides to the arbitrator
        self.active_flag = active_flag       # Boolean variable indicating if behavior is currently active or inactive.
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0                # A real number in the range [0, 1]
        self.weight = 0                      # The product of the priority and the match degree

    def add_sensob(self, sensob):                        # append a newly-created sensob onto the sensobs list
        self.sensobs = sensob

    def print_sensob(self):
        print(str(self.sensobs))

    def consider_deactivation(self):         # When behavior is active, test whether it should deactivate
        pass

    def consider_activation(self):           # When behavior is inactive, test whether it should activate
        pass

    def update(self):                        # The main interface between the bbcon and the behavior
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()

        self.weight = self.priority * self.match_degree

    def sense_and_act(self):                 # Core computations performed by the behavior that use sensob readings to
        pass                                 # Produce motor recommendations (and halt requests)

    #def printMe(self):
        #for sensor in self.sensobs:
            #print(sensor.get_value())
        #print(self.priority)
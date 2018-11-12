#import bbcon
import random

class Arbitrator():

    def __init__(self):
        active_behavior = self.active_behavior


    def choose_action(self, active_behaviors, stochastic=False):
        if stochastic:
            return self.stochastic_action(active_behaviors)
        else:
            return self.deterministic(active_behaviors)


    #Arbitrator picks the behavios with the highest weight
    def deterministic(self, active_behaviors):
        highest_weight = []
        best_behavior = None
        for b in active_behaviors:
            if b.weight >= highest_weight:
                highest_weight = b.weight
                best_behavior = b
        return (best_behavior.motor_recommendations, best_behavior.halt_request)


    #Arbitrator makes a random, but biased, choice among the behaviors
    #   the random number falls within one of the corresponding behaviors weight-intervall
    def stochastic_action(self, active_behaviors):
        weights = []
        total_weight = 0
        for b in active_behaviors:
            weights.append(total_weight + b.weight)
            total_weight += b.weight

        random_number = round(random.random() * total_weight, 3)

        for i in range(len(weights)):
            if random_number < weights[i]:
                return (active_behaviors[i].motor_recommendations, active_behaviors[i].halt_request)

import random


class ProbabilityService:
    @staticmethod
    def roll_probability(probability):
        return random.randint(0, 100) < probability

import random

class Die():
    def __init__(self,side):
        self.side=side

    def roll(self):
        return random.randint(1,self.side)
"""
class will create a random walk value 

"""
from random import choice

class Randomwalk():
    def __init__(self,num_point=5000):
        self.num_point=num_point


        #All walk start point
        self.x_value=[0]
        self.y_value=[0]
        self.direction=[1,-1]
        self.distance =[1,2,3,4]

    def fill_walk(self):
        ''' calculate all the random point walk '''

        while len(self.x_value) < self.num_point:
            x_direction = choice(self.direction)
            x_distance= choice(self.distance)
            x_step=x_direction*x_distance


            y_direction = choice(self.direction)
            y_distance= choice(self.distance)
            y_step=y_direction*y_distance

            if x_step ==0 and y_step == 0:
                continue
            #claculate the new position 
            x=self.x_value[-1] + x_step
            y=self.y_value[-1] + y_step


            self.x_value.append(x)
            self.y_value.append(y)


              

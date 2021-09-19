"""
project description: this project is practice for data visulization 

name : amzad hossain rafi 
id :1530520042
email : amzad.rafi@northosouth.edu

"""

#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random_walk import Randomwalk
#set style 
plt.style.use('seaborn')






# squares =[1,4,9,16,25,36]

value= range(1,50)
squares=[x**2 for x in value]
fig , ax =plt.subplots()
ax.set_title(" squre number ",fontsize=20)          #set tital 
ax.set_xlabel("value", fontsize=14)                 #x axis value 
ax.set_ylabel("square of the value ", fontsize=14)  # y axis value 

#set axis range for each axis 
ax.axis([0,50,0,5000])                                #take tuple or list [x_start, x_finish, y_start , y_finsh]

#set size of tick label 
ax.tick_params(axis="both",labelsize=10)
# ax.plot(value,squares,linewidth=3)                  #[x, y] linewidth make the graph line more thik 
ax.scatter(value, squares,c="red", s=50)              #[x, y] s make the graph dot point more thik  c = color (tuple or string )

#save the plot
plt.savefig('image of example/ example8(save).png',bbox_inches="tight")



plt.show()





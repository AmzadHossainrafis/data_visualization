from random_walk import Randomwalk
import matplotlib.pyplot as plt



rw=Randomwalk()
rw.fill_walk()
plt.style.use('seaborn')
plt.axis()

fig , ax =plt.subplots()
ax.set_title(" squre number ",fontsize=20)          #set tital 
ax.set_xlabel("value", fontsize=14)                 #x axis value 
ax.set_ylabel("square of the value ", fontsize=14)  # y axis value 

plt.scatter(rw.x_value,rw.y_value, c='red',s=5)
plt.show()

#plt.savefig('image of example/ example9(rw).png',bbox_inches="tight")


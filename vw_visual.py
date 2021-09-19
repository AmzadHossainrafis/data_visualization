from random_walk import Randomwalk
import matplotlib.pyplot as plt


while True:
    rw=Randomwalk()
    rw.fill_walk()
    plt.style.use('seaborn')
    plt.axis()

    fig , ax =plt.subplots()
    ax.set_title(" random walk ",fontsize=20)          #set tital 
     

    plt.scatter(rw.x_value,rw.y_value, c='red',s=5)
    plt.show()


    keep=input(" make another y/n /n ")
    if keep == "n":
        break
plt.savefig('image of example/ example9(rw).png',bbox_inches="tight")


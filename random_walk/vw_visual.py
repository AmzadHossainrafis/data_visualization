from random_walk import Randomwalk
import matplotlib.pyplot as plt


while True:
    rw=Randomwalk()
    rw.fill_walk()
    plt.style.use('seaborn')
    plt.axis()

    fig, ax =plt.subplots()
    ax.set_title(" Random walk ",fontsize=20)          #set tital 
     
    point_number=range(rw.num_point)
    ax.scatter(rw.x_value,rw.y_value, c=point_number,cmap=plt.cm.Reds,edgecolors='none',s=5) #plt.cm.Reds = red #plt.cm.gray = gray 
    
    #finding start and end point 
    ax.scatter(rw.x_value[0],rw.y_value[0],c='blue',edgecolors='none',s=50)
    ax.scatter(rw.x_value[-1],rw.y_value[-1],c='green',s=50)
    

    #hide the axis 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    break


    # keep=input(" make another y/n \n ")
    # if keep == "n":
    #     break
    # 
    # plt.savefig('image of example/example10.PNG',bbox_inches="tight")


import csv 
import matplotlib.pyplot as plt
from datetime import  datetime


# import pandas as pd
# import numpy as np 


plt.style.use("seaborn")
fig,ax=plt.subplots()
ax.set_title(" daily tem ")
ax.set_ylabel(" tem value ")
ax.set_xlabel(" date ")
fig.autofmt_xdate()

file_name="data/sitka_weather_07-2018_simple.csv"

with open(file_name) as f:
    #load reader 
    reader = csv.reader(f)
    #load head  of the csv file 
    head= next(reader) #next return the next line 
    # print(head)


    # for index, col in enumerate(head):
    #     print(index,col)
    result = []
    date=[]
    low=[]
    # tem with date 
    for row in reader:
        tdate=datetime.strptime(row[2],'%Y-%m-%d')
        value=int(row[5])
        value_low=int(row[6])
        result.append(value)
        date.append(tdate)
        low.append(value_low)
    # print(result) and plt it 
    ax.plot(date,result,c="red")
    ax.plot(date,low,c="green")
    ax.tick_params(axis="both",which="major",labelsize=14)
    plt.show()
    # plt.savefig("image/result1.png")





from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

#creat a object 

die=Die(6)
#list to carry random die side  value
result=[]
for i in range(100):
    x=die.roll() #roll the die to create to outcome 
    result.append(x)

frquency=[]

for x in range(1,die.side+1):
    c=result.count(x)
    frquency.append(c)

print(frquency)


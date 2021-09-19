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
#analyse the result 
for x in range(1,die.side+1):
    c=result.count(x)
    frquency.append(c)

x_value= list(range(1,die.side+1))
data=[Bar(x=x_value,y=frquency)]
x_config= {"title": "result"}
y_config= {"title": "frequecy"}
my_layout= Layout(title="result of the rolling die ",xaxis=x_config,yaxis=y_config)
offline.plot({'data': data,'layout':my_layout},filename='d6.html')
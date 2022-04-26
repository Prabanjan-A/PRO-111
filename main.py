import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import random
import statistics

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data],["Math_score"],show_hist=False)
#fig.show()

mean = statistics.mean(data)
standard = statistics.stdev(data)
meadian = statistics.median(data)
#print(mean)
#print(standard)

def random_set (counter):
    dataSet=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

mean_list=[]
for i in range(0,1000):
    mean_set = random_set(100)
    mean_list.append(mean_set)

mean = statistics.mean(mean_list)
standard = statistics.stdev(mean_list)
print(mean)
print(standard)

fig = ff.create_distplot([mean_list],["student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean] ,y=[0,0.20] ,mode = "lines", name = "Mean"))
fig.show()
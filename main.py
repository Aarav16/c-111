import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import random
import csv
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

mean1=statistics.mean(data)

print("Mean of sample1:",mean1)


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


mean_list=[]
for i in range(0,100):
    set_of_mean=random_set_of_mean(30)
    mean_list.append(set_of_mean)
    
mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)
print("Mean of sampling distribution:",mean)
print("Standard deviation of Sampling distrubution->",std_deviation)


z_score=(mean1-mean)/std_deviation
print("the z_score is->",z_score)
#fig=ff.create_distplot([mean_list],["Reading_time"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN")) 
#fig.show()

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print("std1",first_std_deviation_start,first_std_deviation_end)
print("std2",second_std_deviation_start,second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)
fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines", name="STANDARD DEVIEATON 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines", name="STANDARD DEVIEATON 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines", name="STANDARD DEVIEATON 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines", name="STANDARD DEVIEATON 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines", name="STANDARD DEVIEATON 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines", name="STANDARD DEVIEATON 3 End"))
fig.show()


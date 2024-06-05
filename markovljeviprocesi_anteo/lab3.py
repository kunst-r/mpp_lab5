from __future__ import division
from scipy.stats import expon
from scipy.stats import ecdf
import matplotlib.pyplot as plt
import numpy as np
import csv as c
import math as m
import random as r


#stanja
#0->društvene mreže
#1->video igre
#2->glazba(Spotify)

# matrica prijelaza
# 0   0.3   0.7
# 0.5  0    0.5
# 0.6  0.4  0

#početno random stanje
state = m.floor(r.random()*3)

expons = [143, 72.42, 10.12]  #lambde za eksponencijalnu razdiobu
states = []
durations = []
duration_sum=duration_sum0=duration_sum1=duration_sum2=0
#simulacija
for i in range(10000):
    states.append(state)  #sva stanja u kojem se MP našao
    durations.append(float(expon.rvs(loc=0,scale=expons[state],size=1)))  #trajanje stanja generirano po eksp razdiobi
    duration_sum+=durations[i]
    p=r.random()
    if state==0:
        duration_sum0+=durations[i]
        if p < 0.3:
            state=1
        else:
            state=2
        continue
    if state==1:
        duration_sum1+=durations[i]
        if p < 0.5:
            state=0
        else:
            state=2
        continue
    if state==2:
        duration_sum2+=durations[i]
        if p < 0.6:
            state=0
        else:
            state=1
        continue

#empirijske vjerojatnosti
print("Vjerojatnost prvog stanja: " + str(duration_sum0/duration_sum))
print("Vjerojatnost drugog stanja: " + str(duration_sum1/duration_sum))
print("Vjerojatnost trećeg stanja: " + str(duration_sum2/duration_sum))

#pisanje u .csv file
with open('lab3_data.csv', 'w', encoding='UTF8') as f:
    writer = c.writer(f)
    for i in range(len(states)):
        line = []
        if states[i]==0:
            line.append("Drustvene mreze")
        if states[i]==1:
            line.append("Video igre")
        if states[i]==2:
            line.append("Glazba(Spotify)")
        line.append(durations[i])
        writer.writerow(line)

#graf
res = ecdf(durations)
ax = plt.subplot()
res.cdf.plot(ax)
ax.set_xlabel('Trajanja stanja')
ax.set_ylabel('ECDF')
plt.show()
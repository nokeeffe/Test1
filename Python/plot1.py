# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:26:52 2021

@author: nokeeffe
"""

import matplotlib.pyplot as plt
import datetime
import time
import random

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%X"))

x=[]
y=[]
for n in range(0,10):
    y.append(random.randint(1,20))
    x.append(datetime.datetime.now().strftime("%X"))
    time.sleep(1);
    
print(x)
print(y)

# plot
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.title("Plot Example")
plt.xlabel("Time")
plt.ylabel("Sample")
plt.show()
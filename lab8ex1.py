#aw(n) = 1
#Hanningw(n) = 0.5[1−cos(2πn/N)]
import numpy as np
import matplotlib.pyplot as plt

fig,v=plt.subplots(2)
v[0].step([-2,-1.0,1.0,2],[0,0,1,0])
y=0.5*(1-np.cos(2*np.pi/100*np.arange(100)))
v[1].plot(y)
plt.show()

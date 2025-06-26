import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


data = np.array([[-2,0],[-1,-0.5],[0,1],[1,1],[2,1],[3,0.5],[4,0]])
plt.figure()
plt.stem(data[:,0],data[:,1])
plt.grid()
m = data[:,0] + 1


plt.figure()
plt.stem(m,data[:,1])
plt.grid()
m = -data[:,0]


plt.figure()
plt.stem(m,data[:,1])
plt.grid()

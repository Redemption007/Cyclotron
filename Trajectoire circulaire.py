import numpy as np
import matplotlib.pyplot as plt

def c_traj (R, v, m, B, q) :
  #intégration numérique à faire
  
  
  
theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)  #faire le cadre ? 

ax.plot(x1, x2)
ax.set_aspect(1)  #pour mettre à l'echelle (sinon ca fait une ellipse) 

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)

plt.show()

import numpy as np
import sympy as sp
import forces
import var

def newton(v, U, des) :
  t = sp.symbols('t')
  if (des==True): a_x = forces.lorentz(v, "x")/var.m()
  if (des==False): a_x = forces.champ(U)/var.m()
  a_y = forces.lorentz(v, "y")/var.m()
  v_x = sp.Add(a_x.integrate(t), var.v0())
  v_y = a_y.integrate(t)
  x = sp.Add(v_x.integrate(t) ,-var.x0)
  y = v_y.integrate(t)
  norme = np.sqrt(v_x**2+v_y**2)
  time = sp.Add(x, var.x0).root(1)
  '''
  On rentre une fonction dedans, qui correspondra à l'accélération subie par la particule. On intègrera numériquement pour en ressortir la vitesse
  (qui sera affichée en sortie écran utilisateur dans un tableau) ainsi que la trajectoire, qui sera modélisée en sortie écran utilisateur dans un graphe.
  L'idée est de faire fonctionner la fonction zone par zone afin de ne pas surcharger la mémoire vive avec la quantité de points à afficher.
  Ainsi les précédents points seront au fur et à mesure supprimés pour garder une vitesse correcte et ne pas créer de latence dans la simulation.
  '''
  
  return x, y, norme, time

'''
Ici, un exemple de trajectoire circulaire pour pouvoir superposer les fonctions dans un premier temps et vérifier les intégrations des zones 2 et 4 (dans les dés)
  
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
'''

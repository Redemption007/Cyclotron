import numpy
from sympy import Poly
import sympy as sp
import forces
import var

#Cette fonction sert à appliquer une fonction f(t) à un tableau de valeurs, pour éviter une erreur Sympy.
def FunctionOfArray(array, f):
  toreturn = []
  for i in range(array.__len__()):
    toreturn.append(f(array[i]))
  return toreturn
#On définit la fonction qui opère la deuxième loi de Newton
def newton(v, y0, U, des) :
  #On pose t en tant que variable
  t = sp.symbols('t')
  #Si la particule est dans un dé (parties 1 et 3)
  if (des):
    #Le paramètre corrictif sert à orienter convenablement le sens de la trajectoire. En gros, vers le haut ou vers le bas.
    correction = -U
    #On somme les forces en appelant la force de Lorentz, la seule qui s'applique à la particule, la gravité étant négligeable
    a_x = forces.lorentz(v, "x")/var.m
    a_y = forces.lorentz(v, "y")/var.m
  #Si la particule n'est pas dans un dé (parties 2 et 4)
  else:
    #Le paramètre corrictif est ici inutile, puisque U est toujours orienté dans le sens de la marche dans l'espace entre les dés
    correction = U
    #On somme les forces en appelant la force du champ électrique, la seule qui s'applique à la particule, la gravité étant négligeable
    a_x = 0*t + forces.champ(U)/var.m
    a_y = 0*t
  '''
  print('\n\n\na_x = ', a_x)
  print('a_y = ', a_y)
  '''
  #Le mode opératoire est maintenant le même lors des deux cas de figure :
  #On intègre pour obtenir la vitesse en x et en y
  v_x = a_x.integrate(t) + correction*v
  v_y = a_y.integrate(t)
  '''
  print('v_x = ', v_x)
  print('v_y = ', v_y)
  '''
  #omega est la vitesse angulaire, constante puisque le cyclotron est isochrone
  omega = (var.q*var.magne)/var.m
  #F est la force de Lorentz.
  F = var.q*v*var.magne
  '''
  print('x = ', v_x.integrate(t) + correction*var.x0)
  print('y = ', v_y.integrate(t) - F/(omega**2) + y0)
  '''
  x = sp.lambdify(t, v_x.integrate(t)+ correction*var.x0, 'math') #On transforme en fonction utilisable par python la fonction Sympy qu'on avait
  y = sp.lambdify(t, v_y.integrate(t) - F/(omega**2) + y0, 'math') #De même. Le terme - F/(omega**2) est un paramètre correctif dû au cosinus valant 1 à t=0
  if (not des):
    #Si l'on n'est pas dans un dé, on cherche la racine du polynôme qu'est la trajectoire en x, auquel on a préalablement retranché l'abscisse de fin, pour que la racine corresponde en fait au t0 tel que x(t0)=abscisse du dé suivant
    duree = Poly(v_x.integrate(t) + 2*correction*var.x0).root(0)
    #Cela renvoie une fonction constante, qu'on évalue donc en n'importe quelle valeur
    duree = sp.lambdify(t, duree, 'math')(1)
  #Si on est dans un dé, la durée passé dans le dé est toujours la même, et vaut l'angle de rotation (Pi) divisé par omega
  if (des): duree = numpy.pi/omega
  #On évalue la vitesse en x à la durée finale de chaque partie (la vitesse en y étant nulle aux conditions limites de toutes les parties, v_x équivaut à la norme de v)
  norme = sp.lambdify(t, v_x, 'math')(duree)
  #Nous avons essayé de produire une image par milliseconde via la variable suivante :
  number = int(duree*1000)
  #Tableau des valeurs de t
  tarray = numpy.linspace(0, duree, number)
  '''
  print("duree est un ", type(duree))
  print("duree = ", duree)
  print("norme = ", norme)
  print("number = ", number)
  print(FunctionOfArray(tarray, x))
  '''
  '''
  On rentre une fonction dedans, qui correspondra à l'accélération subie par la particule. On intègrera numériquement pour en ressortir la vitesse
  (qui sera affichée en sortie écran utilisateur dans un tableau) ainsi que la trajectoire, qui sera modélisée en sortie écran utilisateur dans un graphe.
  L'idée est de faire fonctionner la fonction zone par zone afin de ne pas surcharger la mémoire vive avec la quantité de points à afficher.
  Ainsi les précédents points seront au fur et à mesure supprimés pour garder une vitesse correcte et ne pas créer de latence dans la simulation.
  '''
  #On retourne le tableau des abscisses, le tableau des ordonnées, ainsi que la norme de la vitesse
  return FunctionOfArray(tarray, x), FunctionOfArray(tarray, y), norme

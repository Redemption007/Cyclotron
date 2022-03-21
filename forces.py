#
import init #Fichier des valeurs initiales
from sympy import Poly
from sympy.abc import t
"""
Aide du module forces :

NOM :
    forces - Fichier de définition des forces, appelées pour l'application de la deuxième loi de Newton.

FONCTIONS :
    laplace(position_x, v, dir)
        Retourne la force de Laplace en x ou y selon la valeur de dir, calculée avec Bz, q et v, en fonction de la position_x de la particule. 
        Définition propre du rayon de courbure R, calculée avec v, m, q et Bz.

    champ(position_x, Ex, q, U)
        Retourne la force du champ, calculée avec Bz, q et v, en fonction de la position_x de la particule. 
"""
def laplace(position_x, v) :
  R = (v*init.m)/(init.q*init.Bz) #rayon de courbure
  if (dir=="x"):
    #On retourne la composante x de la force
    return Poly(force, t)
  if (dir=="y"):
    #On retourne la composante y de la force
    return Poly(force, t)
  else:
    return error
  
  """
  On définit ici l'intensité de la force de Laplace dans les dés à l'aide de plusieurs paramètres :
  - La position qui servira à savoir si la particule se trouve dans un dé ou non (x doit être entre x_1 et x_2 compris).
  - la vitesse, qui sera une variable au cours de la simulation
  - l'intensité du champ, qui pourra être modifiée en entrée utilisateur.
  - la masse de la particule, pouvant être modifiée selon des préréglages donnés (électron, proton, neutron, atomes)
  - la charge de la particule, en multiples de e.
  La fonction retournera l'unique force qui s'applique sur la particule.
  """
  return null

def champ(position_x, U) :
  if(position_x<init.x_1 or position_x>init.x_2)     #Si la particule n'est pas entre x_1 et x_2, cela signifie qu'elle est encore dans les dés
    return 0                                         #Alors le champ est nul.
  F = float(init.Ex * init.q * U)                              #Sinon, on retourne la force exercée par le champ, multipliée par la tension
                                                     #pour accélerer la particule dans le bon sens.
  print("F = ", F)                                   #Log de vérification du code. A ENLEVER A LA FIN
  return F
  """
  Selon les mêmes paramètres, ainsi que la tension (qui permettra de savoir dans quel sens est accélérée la particule), 
  on définira ici la force du champ électrique appliqué à l'interstice entre les dés conducteurs.
  La fonction retournera l'unique force s'appliquant sur la particule.
  """

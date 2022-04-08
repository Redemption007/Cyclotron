#import init #Fichier des valeurs initiales
import sympy as sp
from sympy.abc import t
import main
import var
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
def lorentz(v, dir):
  #R = (v*init.m)/(init.q*init.Bz) rayon de courbure
  F = var.q()*v*var.magne()
  if (dir=="x"):
    force = F*sp.sin((t*var.q()*var.magne())/var.m())
    #On retourne la composante x de la force
    return force
  if (dir=="y"):
    force = F*sp.cos((t*var.q()*var.magne())/var.m())
    #On retourne la composante y de la force
    return force
  else:
    return

  """
  On définit ici l'intensité de la force de Laplace dans les dés à l'aide de plusieurs paramètres :
  - La position qui servira à savoir si la particule se trouve dans un dé ou non (x doit être entre x_1 et x_2 compris).
  - la vitesse, qui sera une variable au cours de la simulation
  - l'intensité du champ, qui pourra être modifiée en entrée utilisateur.
  - la masse de la particule, pouvant être modifiée selon des préréglages donnés (électron, proton, neutron, atomes)
  - la charge de la particule, en multiples de e.
  La fonction retournera l'unique force qui s'applique sur la particule.
  """
  return

def champ(U) :
  F = float(var.elec() * var.q() * U)                    #On retourne la force exercée par le champ, multipliée par la tension
                                                     #pour accélerer la particule dans le bon sens.
  print("F = ", F)                                   #Log de vérification du code. A ENLEVER A LA FIN
  return F
  """
  Selon les mêmes paramètres, ainsi que la tension (qui permettra de savoir dans quel sens est accélérée la particule), 
  on définira ici la force du champ électrique appliqué à l'interstice entre les dés conducteurs.
  La fonction retournera l'unique force s'appliquant sur la particule.
  """

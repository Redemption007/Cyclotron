#import init #Fichier des valeurs initiales
import sympy as sp
from sympy.abc import t
import var
"""
Aide du module forces :

NOM :
    forces - Fichier de définition des forces, appelées pour l'application de la deuxième loi de Newton.

FONCTIONS :
    laplace(position_x, v, dir)
        Retourne la force de Lorentz en x ou y selon la valeur de dir, calculée avec Bz, q et v, en fonction de la position_x de la particule. 
        Définition propre du rayon de courbure R, calculée avec v, m, q et Bz.

    champ(position_x, Ex, q, U)
        Retourne la force du champ, calculée avec Bz, q et v, en fonction de la position_x de la particule. 
"""
#On définit la force de Lorentz
def lorentz(v, dir):
  #R = (v*var.m)/(var.q*var.magne) rayon de courbure inutilisé ici
  #F est la norme de la force de Lorentz. Comme on a v et B qui sont perpendiculaires, le résultat de la norme est un simple produit des deux normes
  F = var.q*v*var.magne
  #On définit la vitesse angulaire, constante car l'on sait que le cyclotron est isochrone
  omega = (var.q*var.magne)/var.m
  #Selon la direction souhaitée, on ne renverra pas la même chose
  if (dir=="x"):
    #On retourne la composante x de la force
    force = -F*sp.sin(t*omega) # échelle : en kg.cm.ms^-2 avec 1cm <=> 1 pixel <=> 1 unité et t est en ms
    return force
  if (dir=="y"):
    #On retourne la composante y de la force
    force = -F*sp.cos(t*omega) # échelle : en kg.cm.ms^-2 avec 1cm <=> 1 pixel <=> 1 unité et t est en ms
    return force
  else:
    #Ce cas n'est jamais atteint, il existe simplement pour ne pas produire d'erreur dans ce fichier mais dans le fichier d'appel, demanière à ce que l'on voit tout de suite que dir ne correspond pas à l'un des deux choix possibles.
    return

  """
  On définit ici l'intensité de la force de Lorentz dans les dés à l'aide de plusieurs paramètres :
  - La position qui servira à savoir si la particule se trouve dans un dé ou non (x doit être entre x_1 et x_2 compris).
  - la vitesse, qui sera une variable au cours de la simulation
  - l'intensité du champ, qui pourra être modifiée en entrée utilisateur.
  - la masse de la particule, pouvant être modifiée selon des préréglages donnés (électron, proton, neutron, atomes)
  - la charge de la particule, en multiples de e.
  La fonction retournera l'unique force qui s'applique sur la particule.
  """
  return

#On définit la fonction retournant la force électrique
def champ(U) :
  # On retourne la force exercée par le champ, multipliée par la tension pour accélerer la particule dans le bon sens.
  F = float(var.elec * var.q * U)*1e-4 #mise à la bonne échelle : en cm.ms^-1 avec 1cm <=> 1 pixel <=> 1 unité
  return F
  """
  Selon les mêmes paramètres, ainsi que la tension (qui permettra de savoir dans quel sens est accélérée la particule), 
  on définira ici la force du champ électrique appliqué à l'interstice entre les dés conducteurs.
  La fonction retournera l'unique force s'appliquant sur la particule.
  """

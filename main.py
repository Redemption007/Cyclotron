#déclaration des variables
import numpy as np
import trajectoire
import var
import base
#Définition de la fonction principale :
def main():

  #On définit U qui symbolisera la variation de tension
  U = 1
  #On fixe la norme de vitesse à v0
  v = var.v0
  #On fixe la première abscisse à x0
  tx = [var.x0]
  #On fixe la première ordonnée à 0
  ty = [0]
  y = 0
  #On trace le schéma du cyclotron
  base.trace(-var.x0)
  #Ainsi, tant que la particule n'a pas l'ordonnée requise pour sortir du cyclotron, on continue de boucler
  while (y>=0.0001*var.x0):
    #On appelle la deuxième loi de Newton sur l'espace entre les dés
    traj_x, traj_y, norme_v = trajectoire.newton(v, y, U, False)
    '''
    print("\ntraj_x : ", traj_x)
    print("\ntraj_y : ", traj_y)
    '''
    #On met à jour la norme de la vitesse
    v = norme_v
    #On change la direction du champ en faisant varier la tension de 1=>-1 ou de -1=>1
    U = -U
    #On appelle la deuxième loi de Newton dans les dés
    traj_x_d, traj_y_d, norme_v_d = trajectoire.newton(v, y, U, True)
    '''
    print("\ntraj_x_d = ", traj_x_d)
    print(traj_y_d)
    '''
    #On ajoute les abscisses calculées dans un seul tableau
    traj_x = np.concatenate((traj_x, traj_x_d))
    tx = np.concatenate((tx, traj_x))
    #De même pour les ordonnées
    traj_y = np.concatenate((traj_y, traj_y_d))
    ty = np.concatenate((ty, traj_y))
    #Quelle est la dernière ordonnée calculée ? C'est y = ty[-1]
    y = ty[-1]
    print("La particule se trouve en y = ", y)
  #FIN DU WHILE
  #Cette condition modélise le comportement de la particule quand elle sort du cyclotron
  if(y<=0.0001*var.x0 and tx.__len__()>0 and tx[tx.__len__()-1]>=0):
    ty = np.concatenate((ty, np.linspace(y, y, 120-var.x0)))
    ty = np.concatenate((ty, np.linspace(-var.x0, -120, 120-var.x0)))
  #Enfin, on affiche les points
  for i in range(ty.__len__()-1):
    print("Going to : x = ", tx[i], ' and y = ', ty[i])
    base.goto(tx[i], ty[i])

#On appelle finalement la fonction qu'on vient de définir, pour lancer le programme
main()










'''
    Une fois cela fait, connaissant la vitesse initiale et les conditions initiales, on peut utiliser la deuxième
    loi de Newton pour déterminer la trajectoire à tracer.
    Ceci retournera 3 variables : une équation horaire de position selon chaque composante x et y, ainsi que la norme de la vitesse à la fin
    On calculera ces fonctions en un nombre donnée de points (dont il nous faut déterminer le nombre) pour arriver jusqu'au récepteur.
    
    IDEE : Faire une boucle avec comme condition d'arrêt que x soit égal à x_récepteur
    RISQUE DE BOUCLE INFINIE ! Prévoir le cas.
    On tracera dans le même temps la courbe de la vitesse : courbe en escalier, la norme est constante dans les dés,
    et augmente dans l'espace entre ces derniers.
'''
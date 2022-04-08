#déclaration des variables
import trajectoire
import base
import var
'''
#B
Bx=0
By=0
Bz=1,5 #T champ magnétique
#E
Ex=0
Ey=5*10**3 #V
Ez=0 #champ électrique
m = 1,67*10**-27 #masse de la particule (kg)
q = 1,6*10**-19 #quantité de charge de la particule (C)
'''

#Définition de la fonction principale :
def main():
  base.trace(var.x0)
  '''
    forces.laplace et force.champ sont les fonctions appelées dans la seconde loi de Newton
    On trace le schéma des dés et du recepteur. On positionne le crayon en x0, y0, et on fixe la couleur, le trait.
    Une fois cela fait, connaissant la vitesse initiale et les conditions initiales, on peut utiliser la deuxième
    loi de Newton pour déterminer la trajectoire à tracer.
    Ceci retournera 3 variables : une équation horaire de position selon chaque composante x et y, ainsi que la norme de la vitesse à la fin
    On calculera ces fonctions en un nombre donnée de points (dont il nous faut déterminer le nombre) pour arriver jusqu'au récepteur.
    
    IDEE : Faire une boucle avec comme condition d'arrêt que x soit égal à x_récepteur
    RISQUE DE BOUCLE INFINIE ! Prévoir le cas.
    On tracera dans le même temps la courbe de la vitesse : courbe en escalier, la norme est constante dans le dés,
    et augmente dans l'espace entre ces derniers.
  '''
  y = 0
  U = 1
  v = var.v0()
  while (y>=5*var.x0):
    traj_x, traj_y, norme_v, time = trajectoire.newton(v, U, False)
    U = -U
    v = norme_v
    #Process
    traj_x, traj_y, norme_v, time = trajectoire.newton(v, U, False)
    y_fin = traj_y.eval(time)

# Cyclotron
Modélisation 2, Année L2 2022


# Données d’entrée :
On considère un cyclotron destinée à la
médecine nucléaire et à la recherche. Il est
de forme circulaire et composé de deux
”dees” comme représenté ci-contre. Les
particules sont injectées au centre avec une
vitesse initiale, elles effectuent un certain
nombre de tours en suivant une trajectoire en spirale durant lesquels elles sont
accélérées et lorsqu’elles atteignent l’énergie
nécessaire, elles sont extraites du cyclotron.
La trajectoire des particules est obtenue à l’aide de forces électromagnétiques. A
chaque passage dans les zones 2 et 4, les particules sont accélérées en ligne droite
tandis que dans les zones 1 et 3, leur trajectoire est circulaire uniforme.
# Le programme :
• Calcul dans la zone 2 et 4 de la force que peut subir une particule
chargée de charge q lorsqu’elle est soumise à un champ électrique
E : FC = q × E

• Zone 1 et 3 : calcul de
  ⊲ la vitesse v des particules en fonction de leur rayon de courbure
R, de leur charge q, du champ magnétique ~B et de sa masse m telle
que : v = q| B|R
m
  ⊲ la force que peut subir une particule chargée de charge q et
de vitesse v lorsqu’elle est soumise à un champ magnétique B :\
FL = qv ∧ B (force de Lorentz)

• Calcul du nombre total de tours que doivent effectuer les particules pour atteindre une énergie cinétique E.
# Données d’entrée :
    B(Bx=0,By=0,Bz=1,5T),
    E(Ex=0,Ey=5·103V,Ez=0),
    m = 1,67·10−27kg,
    q = 1,6·10−19C.

### Etude :
    • Etude de l’accélération de particules soumises à des champs électriques et magnétique
    
# Structure du code :

- fichiers des fonctions générales
> forces ;\
> accélération et trajectoire ;

- fichier des variations (fonctions bonus)
> de phase ;\
> d'amplitude ;\
> de champ ;\
> de potentiel ;\
> de vitessse initiale ;\
> de masse ;

- fichier main :
> contient la position initiale ;\
> tracé de la trajectoire ;\
> options modifiables ;\
> appel aux fichiers et modules ;\
> affichage en sortie ;

# Modules :
- [Sympy](https://docs.sympy.org/latest/index.html) (résolution des équations)
- [tkinter](http://tkinter.fdex.eu/) (graphisme, modélisation)
- modules de données personnalisés (fonctions principale ou optionnelles)

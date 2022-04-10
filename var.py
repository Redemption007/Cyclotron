'''
L'idée est de disposer de boutons réglables avec la souris à côté de la modélisation, pour voir l'influence des différents paramètres sur le système.
Il y aura ainsi soint un continuum de valeurs possibles, soit seulement certaines valeurs prédéfinies (dans le cas de la masse par exemple).
Au total, 6 paramètres seront variables, et ils resteront figés pour toute la simulation dès que celle-ci sera lancée.
Il faudra alors arrêter la modélisation et la reprendre de 0 pour mettre à jours les réglages voulus.
'''
#variable réglant l'intensité du champ électromagnétique dans les dés.
magne = 1.5 #T (Tesla)
#variable réglant le potentiel des dés.
elec = 5e3 #V.m^-1 (Volt par mètre) ATTENTION, FAUTE SUR LE SUJET OU SEULS LES VOLTS SONT INDIQUÉS
#variable réglant la vitesse initiale de la particule. Une vitesse nulle donne un processus interminable, une vitesse trop haute donne des erreurs flagrantes. Cette vitesse rend le processus (très) long mais les erreurs sont moins flagrantes.
v0 = 3e6 #cm.ms^-1
#variable de position initiale de la particule. La multiplier par 2 donne l'espacement entre les dés
x0 =-40 #cm ou pixel
#variable réglant la masse de la particule.
m = 1.67e-27 #kg
#variable réglant la charge de la particule.
q = 1.6e-19 #C (Coulomb)

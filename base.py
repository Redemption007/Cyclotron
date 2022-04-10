import turtle
#On met un titre à notre fenêtre parce que c'est zoli
turtle.title("Accélérateur de particules")
turtle.bgcolor("#80aee0")

#space conseillé : 40

#On définit une fonction spéciale pour tracer un dé
def des(r):
  turtle.color("#e1ed24", "#e1ed24")
  turtle.circle(r, 180)
  turtle.left(90)
  turtle.forward(2*r)
  return

#On définit la fonction pour tracer l'espace convenablement et avoir la bonne orientation
def espace(space):
  turtle.up()
  turtle.forward(2*space)
  turtle.right(90)
  turtle.forward(5.1*2*space)
  turtle.left(90)
  turtle.down()
  return

#Enfin, la fonction principale qui va s'occuper des étapes intermédiaires ainsi que moduler l'espace qu'on souhaite
def trace(space):
  turtle.clear()
  turtle.up()
  turtle.home()
  turtle.hideturtle()
  turtle.forward(space)
  turtle.right(90)
  turtle.forward(5.2*space)
  turtle.left(90)
  turtle.down()
  turtle.begin_fill()
  des(5.1*space)
  turtle.right(90)
  turtle.end_fill()
  espace(space)
  turtle.begin_fill()
  des(5*space)
  turtle.end_fill()
  turtle.up()
  turtle.setpos(-space, 0)
  turtle.showturtle() #On remontre la tortue (curseur) parce que voir ce curseur, c'est voir la position exacte de la particule
  return

#Cette fonction sert à tracer la courbe des particules en reliant par des droites les différents points. Les variations étant au pixel près, cela revient au même que si l'on traçait les courbes
def goto(x, y):
  turtle.color("#FF0000", "#FF0000")
  turtle.down()
  turtle.setpos(x, y)

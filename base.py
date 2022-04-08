import turtle
turtle.title("Accélérateur de particules")
turtle.bgcolor("#80aee0")

#space conseillé : 40

def des(r):
  turtle.color("#e1ed24", "#e1ed24")
  turtle.circle(r, 180)
  turtle.left(90)
  turtle.forward(2*r)
  return

def espace(space):
  turtle.up()
  turtle.forward(space)
  turtle.right(90)
  turtle.forward(5.1*2*space)
  turtle.left(90)
  turtle.down()
  return
	
def trace(space):
  turtle.clear()
  turtle.up()
  turtle.home()
  turtle.forward(space/2)
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
  turtle.done()
  return
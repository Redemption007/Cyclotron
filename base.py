import turtle.Turtle() as tur
turtle.title("Accélérateur de particules")
turtle.bgcolor("#80aee0")
def des():
	turtle.color("#e1ed24", "#e1ed24")
	tur.circle(50, 180)
def espace(space):
	tur.forward(100)
	tur.left(90)
	tur.forward(space)
	tur.left(90)
	tur.forward(100)
	tur.left(90)
	tur.forward(space)
	
def trace(space):
	turtle.up()
	turtle.home()
	

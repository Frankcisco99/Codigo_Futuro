import turtle

pantalla = turtle.Screen()
pantalla.title("Pong Game")
pantalla.setup(600,400)
pantalla.bgcolor("black")


#paleta izquierda
paleta_izq = turtle.Turtle()
paleta_izq.color("white")
paleta_izq.shape("square")
paleta_izq.shapesize(stretch_len=1,stretch_wid=5)
paleta_izq.penup()
paleta_izq.goto(-250,0)

#paleta derecha
paleta_der = turtle.Turtle()
paleta_der.color("white")
paleta_der.shape("square")
paleta_der.shapesize(stretch_len=1,stretch_wid=5)
paleta_der.penup()
paleta_der.goto(250,0)

#balon
balon = turtle.Turtle()
balon.color("white")
balon.shape("circle")
balon.penup()
balon.goto(0,0)
balon.speed(40)
balon.dx = 5
balon.dy = -5

#Puntaje
score_izq = 0
score_der = 0
score = turtle.Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, 160)
score.write(f"Player1 {score_izq}  -  Player2 {score_der}", align="center", font=("Verdana",24,"normal"))


def mover_paleta_izq_up():
    y = paleta_izq.ycor()
    y = y + 20
    paleta_izq.sety(y)
    
def mover_paleta_der_up():
    y = paleta_der.ycor()
    y = y + 20
    paleta_der.sety(y)

def mover_paleta_izq_down():
    y = paleta_izq.ycor()
    y = y - 20
    paleta_izq.sety(y)
    
def mover_paleta_der_down():
    y = paleta_der.ycor()
    y = y - 20
    paleta_der.sety(y)
    
pantalla.listen()
pantalla.onkeypress(mover_paleta_izq_up, "w")
pantalla.onkeypress(mover_paleta_der_up, "Up")
pantalla.onkeypress(mover_paleta_izq_down, "s")
pantalla.onkeypress(mover_paleta_der_down, "Down")


while True:
    pantalla.update()
    
    balon.setx(balon.xcor() + balon.dx)
    balon.sety(balon.ycor() + balon.dy)
    
    #Logica balon
    if balon.ycor() > 150:
        balon.sety(150)
        balon.dy *= -1
        
    if balon.ycor() < -150:
        balon.sety(-150)
        balon.dy *= -1
    
    if balon.xcor() > 255:
        
        score_izq += 1
        score.clear()
        score.write(f"Player1 {score_izq}  -  Player2 {score_der}", align="center", font=("Verdana",24,"normal"))
        balon.goto(0,0)
        balon.dy *= -1
        
    if balon.xcor() < -255:
        
        score_der += 1
        score.clear()
        score.write(f"Player1 {score_izq}  -  Player2 {score_der}", align="center", font=("Verdana",24,"normal"))
        balon.goto(0,0)
        balon.dy *= -1
    
    #Logica Paletas
    if paleta_izq.ycor() >= 145:
        paleta_izq.sety(145)
    if paleta_izq.ycor() <= -145:
        paleta_izq.sety(-145)
    if paleta_der.ycor() >= 145:
        paleta_der.sety(145)
    if paleta_der.ycor() <= -145:
        paleta_der.sety(-145)

    #Logica Colision
    if 230<balon.xcor()<240 and abs(balon.ycor() - paleta_der.ycor()) <= 40:     
        balon.setx(230)
        balon.dx *= -1
        
    if -240<balon.xcor()<-230 and abs(balon.ycor() - paleta_izq.ycor()) <= 40:
        balon.setx(-230)
        balon.dx *= -1 

turtle.done()
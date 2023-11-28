import turtle, random

mål = turtle.Turtle()
mål.shape("square")
mål.shapesize(0.5)
bg = turtle.Screen()

mål.penup()
mål.speed(0)
mål.goto(random.randint(-300, 300), random.randint(-200, 200))
träffar = 0
missar = 0

def klick(x,y):
    global träffar, missar
    
    if mål.xcor()-5 <= x <= mål.xcor()+5 and mål.ycor()-5 <= y <= mål.ycor()+5:
        träffar += 1
        mål.hideturtle()
        mål.goto(random.randint(-300,300), random.randint(-200,200))
        mål.showturtle()
    else:
        missar += 1

bg.onscreenclick(klick)
bg.listen()

turtle.done()

print(f"Du fick {träffar} träffar, och {missar} missar.")
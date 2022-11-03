    # This program draws initials using the turtle.py module
    # 11/02/2022
    # CTI-110 P4LAB1b_Apichell.py
    # Colby Apichell




import turtle

#turtle settings
screen = turtle.Screen()
screen.bgcolor('lightgreen')
turtle.pencolor('purple')
turtle.pensize(10)
turtle.shape('turtle')

#make first initial


for i in range(1):
    turtle.right(180)
for i in range(3):
    turtle.forward(100)
    turtle.right(90)

for i in range(1):
    turtle.left(90)
    turtle.penup()

for i in range(1):
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(100)
    
#exit block

turtle.done()
turtle.exitonclick()
 

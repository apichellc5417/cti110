    # This program draws a square and traingle using a for loop
    # 11/02/2022
    # CTI-110 P4LAB1a_Apichell.py
    # Colby Apichell




import turtle

#turtle settings
screen = turtle.Screen()
screen.bgcolor('white')
turtle.pencolor('black')
turtle.pensize(1)
turtle.shape('turtle')

#square portion


for i in range(4):
    turtle.forward(100)
    turtle.right(90)


#triangle portion

#turn the turt
for i in range(1):
    turtle.left(180)

# lay down some lines in sequence unsing range function

for i in range(2):
    turtle.forward(100)
    turtle.right(120)

for i in range(1):
    turtle.forward(100)
    
#exit block

turtle.done()
turtle.exitonclick()
 

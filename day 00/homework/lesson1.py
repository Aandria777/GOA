from turtle import *


#we want to paint a house 

#step 1: draw a square 
speed(30)
width(7)

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90) 
#end of squre 

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120) 
forward(200)
end_fill()

penup()
goto(0,140)
pendown()


right(240)
forward(65)
left(90)
forward(65)

penup()
goto(140, 200)
pendown()

right(180)
forward(60)
left(90)
forward(60)


exitonclick()
from turtle import *

#we want to paint a house

#step 1: draw a square
shape("turtle")
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
 #end of squar

#drawing a door

forward(70)
color("black")
begin_fill()
left(90)
forward(120)  #height of the door
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


#drawing a widow
color("black")
left(120)
forward(70)
right (90)
forward(60)
right(90)
forward(70)
right(90)
forward(60)



#drawing a second window

right(90)
forward(200)
right(90)
forward(60)
right(90)
forward(70)
right(90)
forward(60)
right(90)
forward(35)
right(90)
forward(60)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(70)
left(90)
forward(25)
left(90)
forward(165)
left(90)
forward(60)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(70)



exitonclick()
import turtle 
turtle.bgcolor('black') 
turtle.color('yellow')
turtle.width(10)
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.color('orange')
turtle.end_fill()
# Kreis mit 100 Pixel Radius
turtle.circle(100)
# Kreisausschnitt mit 50 Pixel Radius und 90 Grad (sprich ein ¼ Kreis)
turtle.circle(50,90)
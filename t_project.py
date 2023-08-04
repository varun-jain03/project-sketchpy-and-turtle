import turtle


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

colors = ["red","dark red"]
for i in range(400):
    t.forward(i + 1)
    t.right(90)
    t.pencolor(colors[i % 2])
turtle.done()
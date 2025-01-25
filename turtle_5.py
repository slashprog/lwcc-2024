import turtle

t = turtle.Turtle()
t.speed(0)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 10 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
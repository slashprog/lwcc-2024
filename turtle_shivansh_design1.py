import turtle
t = turtle.Turtle()
t.left(90)
for i in range(24):
    t.forward(100)
    t.backward(100)
    t.right(15)
t.backward(200)
turtle.done()
import turtle

def sierpinski(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order-1, size/2)
        t.forward(size/2)
        sierpinski(t, order-1, size/2)
        t.backward(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        sierpinski(t, order-1, size/2)
        t.left(60)
        t.backward(size/2)
        t.right(60)

t = turtle.Turtle()
sierpinski(t, 3, 200)
turtle.done()
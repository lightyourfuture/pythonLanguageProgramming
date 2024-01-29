import turtle
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)
def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    for i in range(3):
        koch(t, 4, 300)
        t.right(120)
    wn.exitonclick()
    
main()
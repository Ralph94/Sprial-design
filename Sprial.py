import turtle

mw = turtle.Screen()
mw.title("Sprial design < ^ >")
mw.bgcolor("black")
turtle.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/brush.gif")

# Brush
player = turtle.Turtle()
player.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/brush.gif")
player.speed(0)

for i in range(10):
    for colours in ["red","green", "gray", "white"]:
        player.color(colours)
        player.pensize("2")
        player.left(12)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)
        player.forward(200)
        player.left(90)










"""
mw = turtle.Screen()
mw.title("Sprial design < ^ >")

turtle.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/brush.gif")


# Brush
player = turtle.Turtle()
player.color("purple","black")
player.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/brush.gif")
player.speed(0)

forw = 1


while True:

    player.forward(forw)

    player.left(125)

    player.left(2)

    player.right(2)

    player.right(5)

    forw += 6

    player.forward(forw)

    player.left(125)

    player.left(2)

    player.right(2)

    player.right(5)

    player.left(1)

    forw += 6

    player.forward(forw)

    player.left(115)

    player.left(2)

    player.right(2)

    player.right(5)

    player.left(1)

    forw += 6
"""

turtle.mainloop()
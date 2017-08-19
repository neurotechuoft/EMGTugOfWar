import turtle
from player import Player


def draw_zigzag(turtle):
    turtle.goto(-60, 20)
    turtle.forward(120)
    turtle.goto(-60, 0)
    turtle.forward(120)
    turtle.goto(-60, -20)
    turtle.forward(120)


if __name__ == '__main__':
    set_window = turtle.Screen()
    turtle = turtle.Turtle()
    draw_zigzag(turtle)
    sayan = Player("sayan")

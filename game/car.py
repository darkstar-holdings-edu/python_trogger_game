from turtle import Turtle
import random

CAR_COLORS = (
    "black",
    "blue",
    "green",
    "purple",
    "orange",
    "red",
)


class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(CAR_COLORS))
        self.penup()

    def move_forward(self, distance: int) -> None:
        self.setx(self.xcor() - distance)

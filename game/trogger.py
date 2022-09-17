from turtle import Turtle

TROGGER_MOVE_DISTANCE = 20


class Trogger(Turtle):
    starting_position: tuple[int, int]

    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()

        self.starting_position = position

        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)

        self.move_home()

    def move_home(self) -> None:
        self.setposition(self.starting_position)

    def move_forward(self) -> None:
        if self.ycor() < abs(self.starting_position[1]):
            self.sety(self.ycor() + TROGGER_MOVE_DISTANCE)

    def move_backward(self) -> None:
        if self.ycor() > self.starting_position[1]:
            self.sety(self.ycor() - TROGGER_MOVE_DISTANCE)

    def move_left(self) -> None:
        if self.xcor() > -280:
            self.setx(self.xcor() - TROGGER_MOVE_DISTANCE)

    def move_right(self) -> None:
        if self.xcor() < 280:
            self.setx(self.xcor() + TROGGER_MOVE_DISTANCE)

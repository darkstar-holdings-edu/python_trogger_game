from turtle import Turtle


class ScoreBoard(Turtle):
    level: int = 1

    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()

        self.penup()
        self.hideturtle()
        self.setposition(position)
        self.update()

    def update(self) -> None:
        self.clear()
        self.write(
            f"Level: {self.level}",
            align="left",
            font=("Courier", 24, "normal"),
        )

    def game_over(self) -> None:
        self.home()
        self.write(
            "Game Over!",
            align="center",
            font=("Courier", 24, "normal"),
        )

from .car import Car
import random


class CarManager:

    board_size: tuple[int, int]
    cars: list[Car]
    move_speed: int = 10
    _spawner_y_min: int
    _spawner_y_max: int
    _spawner_x: int
    _reaper_x: int

    def __init__(self, board_width: int, board_height: int) -> None:
        self.cars = []

        self.board_size = (board_width, board_height)
        self._spawner_y_max = int(board_height / 2 - 100)
        self._spawner_y_min = int(self._spawner_y_max - 425)
        self._spawner_x = int(board_width / 2)
        self._reaper_x = self._spawner_x * -1

    def spawn_car(self) -> None:
        """Random chance of spawning a car."""
        if random.choices(
            [True, False], [self.move_speed, 100 - self.move_speed], k=1
        )[0]:
            y_cor = random.randint(self._spawner_y_min, self._spawner_y_max)

            car = Car()
            car.setposition(self._spawner_x, y_cor)
            self.cars.append(car)

    def move_cars(self) -> None:
        """Moves all the spawned cars forward"""
        if len(self.cars) == 0:
            self.spawn_car()

        for car in self.cars:
            car.move_forward(distance=self.move_speed)
            if car.xcor() <= self._reaper_x:
                car.hideturtle()

        self.cars = list(
            filter(lambda car: car.xcor() > self._reaper_x, self.cars)
        )

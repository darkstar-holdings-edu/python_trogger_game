from turtle import Screen
import time
from game import Trogger, ScoreBoard, CarManager


def main() -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    trogger = Trogger(position=(0, -280))
    car_manager = CarManager(board_width=600, board_height=600)

    scoreboard = ScoreBoard(position=(-275, 270))

    screen.listen()
    screen.onkey(key="Up", fun=trogger.move_forward)
    screen.onkey(key="Down", fun=trogger.move_backward)
    screen.onkey(key="Right", fun=trogger.move_right)
    screen.onkey(key="Left", fun=trogger.move_left)

    game_running = True
    while game_running:
        car_manager.spawn_car()
        car_manager.move_cars()
        screen.update()

        for car in car_manager.cars:
            if car.distance(trogger) <= 20:
                game_running = False
                break

        if trogger.ycor() > 225:
            trogger.move_home()
            scoreboard.level += 1
            car_manager.move_speed += 10
            scoreboard.update()

        time.sleep(0.1)

    scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()

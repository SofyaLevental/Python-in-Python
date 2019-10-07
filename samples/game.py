from samples.objects import Snake
from samples.publisher import Publisher
from samples.subscriber import Subscriber
from samples.utils import Vector, START_CELL
from samples.visualization import Window, Timer


class Game:
    TIME_INTERVAL_BETWEEN_SNAKE_MOVEMENTS = 50
    TIME_INTERVAL_TO_SHOW_MESSAGE = 1200
    NUMBER_OF_CELLS = 20
    CELL_WIDTH = 25
    window = Window(CELL_WIDTH, NUMBER_OF_CELLS)
    python = Snake(START_CELL)

    @staticmethod
    def start():
        food = Game.python.create_food(Game.NUMBER_OF_CELLS)
        timer = Timer()
        Subscriber.subscribe_for_commands(Game.on_message)

        while Game.window.is_in_game():
            timer.delay(Game.TIME_INTERVAL_BETWEEN_SNAKE_MOVEMENTS)
            Publisher.listen_to_keyboard_events()
            Game.python.move(Game.NUMBER_OF_CELLS)
            if Game.python.has_collision():
                Game.window.show_message("You Lost!", "Your Score is: " + Game.python.get_score())
                timer.delay(Game.TIME_INTERVAL_TO_SHOW_MESSAGE)
                Game.python.reset(START_CELL)
            else:
                if Game.python.get_head().is_on_cube(food.get_position()):
                    food = Game.python.create_food(Game.NUMBER_OF_CELLS)
                else:
                    Game.python.remove_tail()
                Game.window.redraw_window(Game.python, food)

    @staticmethod
    def on_message(client, userdata, message):
        key = str(message.payload.decode("utf-8"))
        if key == 'Q':
            Game.window.quit_game()
        else:
            switcher = {
                'L': Vector(-1, 0),
                'R': Vector(1, 0),
                'U': Vector(0, -1),
                'D': Vector(0, 1)
            }
            Game.python.update_direction(switcher.get(key))

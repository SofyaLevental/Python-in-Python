from samples.objects import Snake
from samples.publisher import Publisher
from samples.subscriber import Subscriber
from samples.utils import Cell, Vector
from samples.visualization import Window, Timer


class Game:
    PYTHON = Snake(Cell(10, 10))

    @staticmethod
    def start():
        cells = 20
        food = Game.PYTHON.create_food(cells)
        timer = Timer()
        Subscriber.subscribe_for_commands(Game.on_message)
        window = Window(500, cells)

        while True:
            timer.delay(50)
            Publisher.listen_to_keyboard_events()
            Game.PYTHON.move(cells)
            if Game.PYTHON.has_collision():
                window.show_message("You Lost!", "Your Score is: " + Game.PYTHON.get_score())
                timer.delay(1200)
                Game.PYTHON.reset(Cell(10, 10))
            else:
                if Game.PYTHON.get_head().is_on_cube(food.get_position()):
                    food = Game.PYTHON.create_food(cells)
                else:
                    Game.PYTHON.remove_tail()
                window.redraw_window(Game.PYTHON, food)

    @staticmethod
    def on_message(client, userdata, message):
        key = str(message.payload.decode("utf-8"))
        if key == 'Q':
            Window.quit_game()
        else:
            switcher = {
                'L': Vector(-1, 0),
                'R': Vector(1, 0),
                'U': Vector(0, -1),
                'D': Vector(0, 1)
            }
            Game.PYTHON.update_direction(switcher.get(key))

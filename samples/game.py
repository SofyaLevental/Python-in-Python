from samples.objects import Snake
from samples.publisher import Publisher
from samples.subscriber import Subscriber
from samples.utils import Cell, Vector
from samples.visualization import Window, Popup, Timer

python = Snake(Cell(10, 10))


def main():
    cells = 20
    food = python.create_food(cells)
    timer = Timer()
    Subscriber.subscribe_for_commands(on_message)
    window = Window(500, cells)

    while True:
        timer.delay()
        Publisher.listen_to_keyboard_events()
        python.move(cells)
        if python.has_collision():
            Popup.show("You Lost!", "Your Score is: " + python.get_score())
            python.reset(Cell(10, 10))
        else:
            if python.get_head().is_on_cube(food.position):
                food = python.create_food(cells)
            else:
                python.remove_tail()
            window.redraw_window(python, food)


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
        python.update_direction(switcher.get(key))


main()

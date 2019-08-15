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
        if python.get_head().position.i == food.position.i and python.get_head().position.j == food.position.j:
            food = python.create_food(cells)
        else:
            body = python.get_body()
            del body[-1]
            python.set_body(body)
        window.redraw_window(python, food)

        for index in range(len(python.get_body())):
            if python.get_body()[index].position in list(
                    map(lambda cube: cube.position, python.get_body()[index + 1:])):
                Popup.show("You Lost!", "Your Score: " + str(len(python.get_body())))
                python.reset(Cell(10, 10))
                break


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

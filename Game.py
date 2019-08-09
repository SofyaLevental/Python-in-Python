import pygame


class Game:
    def __init__(self):
        pass


class Cube:
    def __init__(self, position, x_direction=1, y_direction=0, color=(255, 0, 0)):
        self.position = position
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.color = color

    def move(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.position = (self.position[0] + x_direction, self.position[1] + y_direction)

    def draw(self, window, eyes=False):
        upper_left_corner = [self.position[0] * cell_width + 1, self.position[1] * cell_width + 1]
        down_right_corner = [(self.position[0] + 1) * cell_width, (self.position[1] + 1) * cell_width]
        rect = (self.position[0] * cell_width + 1, self.position[1] * cell_width + 1, cell_width - 1, cell_width - 1)
        pygame.draw.rect(window, self.color, rect)
        if eyes:
            half_cell_width = cell_width // 2
            cube_center = (self.position[0]*cell_width+1+half_cell_width, self.position[1]*cell_width+1+half_cell_width)
            radius = 3
            left_eye_middle = (cube_center[0]-6,cube_center[1])
            right_eye_middle = (cube_center[0]+6,cube_center[1])
            pygame.draw.circle(window, (0,0,0), left_eye_middle, radius)
            pygame.draw.circle(window, (0,0,0), right_eye_middle, radius)


class Snake:
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.head = Cube(position)
        self.body.append(self.head)
        self.x_direction = 1
        self.y_direction = 0

    def move(self):
        first_cell = 0
        last_cell = cells - 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.update_direction(-1, 0)
                elif keys[pygame.K_RIGHT]:
                    self.update_direction(1, 0)
                elif keys[pygame.K_UP]:
                    self.update_direction(0, -1)
                elif keys[pygame.K_DOWN]:
                    self.update_direction(0, 1)

        for i, cube in enumerate(self.body):
            position = cube.position[:]
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0], turn[1])
                self.remove_tail_from_turns(i, position)
            else:
                if cube.x_direction == -1 and cube.position[0] == first_cell:
                    cube.position = (last_cell, cube.position[1])
                elif cube.x_direction == 1 and cube.position[0] == last_cell:
                    cube.position = (first_cell, cube.position[1])
                elif cube.y_direction == -1 and cube.position[1] == first_cell:
                    cube.position = (cube.position[0], last_cell)
                elif cube.y_direction == 1 and cube.position[1] == last_cell:
                    cube.position = (cube.position[0], first_cell)
                else:
                    cube.move(cube.x_direction, cube.y_direction)

    def draw(self, window):
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw(window, True)
            else:
                cube.draw(window)

    def remove_tail_from_turns(self, i, position):
        if i == len(self.body) - 1:
            self.turns.pop(position)

    def update_direction(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.turns[self.head.position[:]] = [self.x_direction, self.y_direction]


def main():
    global width, cells, cell_width, python
    width = 500
    cells = 20
    cell_width = width // cells
    window = pygame.display.set_mode((width, width))
    python = Snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        python.move()
        redraw_window(window)


def redraw_window(window):
    window.fill((0, 0, 0))
    python.draw(window)
    draw_grid(window)
    pygame.display.update()


def draw_grid(window):
    x = 0
    y = 0
    for i in range(cells):
        x = x + cell_width
        y = y + cell_width
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, width))


main()

import pygame
import math

import mazeGenerator



# rysuje koniec labiryntu oraz pozycje gracza
def drawPos():
    n_fn = maze.finish_cell.x
    m_fn = maze.finish_cell.y
    x_fn = x_0 + radius * (abs(n_fn) + 2 * m_fn) * offset
    y_fn = y_0 - 3 * radius * n_fn / 2
    pygame.draw.circle(screen, 0xFF0000, (x_fn, y_fn), radius * (3 / 5))

    n_pl = maze.player_cell.x
    m_pl = maze.player_cell.y
    x_pl = x_0 + radius * (abs(n_pl) + 2 * m_pl) * offset
    y_pl = y_0 - 3 * radius * n_pl / 2
    pygame.draw.circle(screen, 0x9B04C9, (x_pl, y_pl), radius * (2 / 5))

    pygame.display.update()

    pygame.draw.circle(screen, 0x000000, (x_pl, y_pl), radius * (2 / 5))


def changePos(k1, k2):
    if (k1 == pygame.K_UP and k2 == pygame.K_RIGHT) or (k2 == pygame.K_UP and k1 == pygame.K_RIGHT):

        print("NE")

        if mazeGenerator.NE not in maze.player_cell.walls:
            for c in maze.neighbours(maze.player_cell):
                if maze.player_cell.wall_to(c) == mazeGenerator.NE:
                    maze.player_cell = c
                    break

    elif k1 == pygame.K_RIGHT and k2 == pygame.K_RIGHT:

        print("E")

        if mazeGenerator.E not in maze.player_cell.walls:
            for c in maze.neighbours(maze.player_cell):
                if maze.player_cell.wall_to(c) == mazeGenerator.E:
                    maze.player_cell = c
                    break

    elif (k1 == pygame.K_DOWN and k2 == pygame.K_RIGHT) or (k2 == pygame.K_DOWN and k1 == pygame.K_RIGHT):

        print("SE")

        if mazeGenerator.SE not in maze.player_cell.walls:
            for c in maze.neighbours(maze.player_cell):
                if maze.player_cell.wall_to(c) == mazeGenerator.SE:
                    maze.player_cell = c
                    break

    elif (k1 == pygame.K_DOWN and k2 == pygame.K_LEFT) or (k2 == pygame.K_DOWN and k1 == pygame.K_LEFT):

        print("SW")

        if mazeGenerator.SW not in maze.player_cell.walls:
            for c in maze.neighbours(maze.player_cell):
                if maze.player_cell.wall_to(c) == mazeGenerator.SW:
                    maze.player_cell = c
                    break

    elif k1 == pygame.K_LEFT and k2 == pygame.K_LEFT:

        print("W")

        if mazeGenerator.W not in maze.player_cell.walls:
            for c in maze.neighbours(maze.player_cell):
                if maze.player_cell.wall_to(c) == mazeGenerator.W:
                    maze.player_cell = c
                    break

    elif (k1 == pygame.K_UP and k2 == pygame.K_LEFT) or (k2 == pygame.K_UP and k1 == pygame.K_LEFT):

        print("NW")

        if mazeGenerator.NW not in maze.player_cell.walls:
            for c in maze.neighbours(maze.player_cell):
                if maze.player_cell.wall_to(c) == mazeGenerator.NW:
                    maze.player_cell = c
                    break

    else:
        print("Nie prawidłowy input")

    drawPos()

try:
    import pyautogui

    (width, height) = pyautogui.size()
    mon_width = int(width * (92 / 100))
    mon_height = int(height * (92 / 100))
except:
    mon_width = 1280
    mon_height = 720


# preferowany rozmiar między 10, a 40
while True:
    size = int(input("Podaj rozmiar labiryntu(10-30): "))
    if 10 <= size <= 30:
        break

# parametry okna i komorek labiryntu
thick = 2
colour = 0x458693
offset = 7 / 8

maze = mazeGenerator.Maze.generate(size)

radius_w = mon_width / (4 * size - 2)
radius_h = mon_height / (3 * size - 1)

radius = int(min(radius_h, radius_w))
win_width = int((4 * size - 2) * radius * offset + radius * ((math.sqrt(3) - 1) / 2))
win_height = (size * 3 - 1) * radius

pygame.init()
screen = pygame.display.set_mode((win_width, win_height))
print("Radius:", radius, "width:", win_width, "height:", win_height)

(x_0, y_0) = (radius, win_height / 2)

Drawed = False
exit = False
key1 = 0
key2 = 0

while not exit:
    if not Drawed:
        for cell in maze.cells_queue:
            n = cell.x
            m = cell.y
            x_k = x_0 + radius * (abs(n) + 2 * m) * offset
            y_k = y_0 - 3 * radius * n / 2

            if mazeGenerator.NE in cell.walls:
                # NE
                pygame.draw.line(screen, colour,
                                 (int(x_k + radius * math.cos(math.pi / 6)),
                                  int(y_k - radius * math.sin(math.pi / 6))),
                                 (int(x_k), int(y_k - radius)), thick)

            if mazeGenerator.NW in cell.walls:
                # NW
                pygame.draw.line(screen, colour, (int(x_k), int(y_k - radius)), (
                    int(x_k + radius * math.cos(150 * 2 * math.pi / 360)),
                    int(y_k - radius * math.sin(150 * 2 * math.pi / 360))), thick)

            if mazeGenerator.W in cell.walls:
                # W
                pygame.draw.line(screen, colour, (int(x_k + radius * math.cos(150 * 2 * math.pi / 360)),
                                                  int(y_k - radius * math.sin(150 * 2 * math.pi / 360))), (
                                     int(x_k + radius * math.cos(210 * 2 * math.pi / 360)),
                                     int(y_k - radius * math.sin(210 * 2 * math.pi / 360))), thick)

            if mazeGenerator.SW in cell.walls:
                # SW
                pygame.draw.line(screen, colour, (int(x_k + radius * math.cos(210 * 2 * math.pi / 360)),
                                                  int(y_k - radius * math.sin(210 * 2 * math.pi / 360))), (
                                     int(x_k + radius * math.cos(270 * 2 * math.pi / 360)),
                                     int(y_k - radius * math.sin(270 * 2 * math.pi / 360))), thick)

            if mazeGenerator.SE in cell.walls:
                # SE
                pygame.draw.line(screen, colour, (int(x_k + radius * math.cos(270 * 2 * math.pi / 360)),
                                                  int(y_k - radius * math.sin(270 * 2 * math.pi / 360))), (
                                     int(x_k + radius * math.cos(330 * 2 * math.pi / 360)),
                                     int(y_k - radius * math.sin(330 * 2 * math.pi / 360))), thick)

            if mazeGenerator.E in cell.walls:
                # E
                pygame.draw.line(screen, colour, (int(x_k + radius * math.cos(330 * 2 * math.pi / 360)),
                                                  int(y_k - radius * math.sin(330 * 2 * math.pi / 360))), (
                                     int(x_k + radius * math.cos(30 * 2 * math.pi / 360)),
                                     int(y_k - radius * math.sin(30 * 2 * math.pi / 360))), thick)

            pygame.display.update()
            pygame.time.wait(int(150 / size))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        drawPos()

        Drawed = True

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if key1 == 0:
                key1 = event.key
                print(key1)
            elif key2 == 0:
                key2 = event.key
                print(key2)
                changePos(key1,key2)
                key1 = 0
                key2 = 0

        if event.type == pygame.QUIT:
            exit = True

pygame.quit()

import mazeGenerator
import pygame
import math

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
    size = int(input("Podaj rozmiar labiryntu(10-40): "))
    if 10 <= size <= 40:
        break

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

while not exit:
    if not Drawed:
        for cell in maze.cells_queue:
            n = cell.x
            m = cell.y
            x_k = x_0 + radius * (abs(n) + 2 * m) * offset
            y_k = y_0 - 3 * radius * n / 2
            cell = maze.get_cell(n, m)

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

        Drawed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
pygame.quit()

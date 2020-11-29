import random
import pygame
import time


def generate(s):
    white = (255, 250, 250)
    red = (255, 0, 0)

    visited = []
    queue = []
    x = 1
    y = 1

    # Ustawiamy parametry okna dla pygame
    # s = int(input("Podaj rozmiar labiryntu\n"))

    if (s % 2 == 0): s += 1

    screen = pygame.display.set_mode((s * 20, s * 20))
    pygame.display.set_caption("Project Labyrinth")

    # Tworzymy przestrzeń w której ma powstać labirynt
    grid = {(x, y): 1 for x in range(1, s + 1) for y in range(1, s + 1)}

    def CheckNeighbours():  # Funkcja sprawdza ile mamy wolnych sąsiednich kratek
        if (x + 2, y) not in visited and (x + 2, y) in grid:
            neighb.append("E")
            if (x + 2, y) not in queue:
                queue.append((x + 2, y))

        if (x, y + 2) not in visited and (x, y + 2) in grid:
            neighb.append("S")
            if (x, y + 2) not in queue:
                queue.append((x, y + 2))

    # Funkcje Draw* rysują nam ścieżkę

    def DrawRight():
        pygame.draw.rect(screen, white, ((x - 1) * 20 - 20, y * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.001)

    def DrawDown():
        pygame.draw.rect(screen, white, (x * 20 - 20, (y - 1) * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.001)

    def DrawPosition():
        pygame.draw.rect(screen, red, (x * 20 - 20, y * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.03)

        pygame.draw.rect(screen, white, (x * 20 - 20, y * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.001)

    # Ustawiamy parametry dla pierwszej komórki
    DrawPosition()
    neighb = []
    CheckNeighbours()

    # Rozpoczynamy główną pętle
    exit = False
    while not exit:
        while len(queue) > 0:

            if len(
                    neighb) > 0:  # Dla sprawdzonych "sąsiadów" wybieramy losowo jeden wolny, tworzymy ścieżkę oraz zaznaczamy jako odwiedzony
                random_neighb = (random.choice(neighb))

                queue.append((x, y))

                if random_neighb == "E":
                    x = x + 2
                    DrawRight()

                if random_neighb == "S":
                    y = y + 2
                    DrawDown()

                x, y = queue.pop()

            x, y = queue.pop(0)  # Przechodzimy do pierwszej pozycji w naszej kolejce

            # Zaznaczamy pozycję oraz oznaczamy ją jako odwiedzoną
            DrawPosition()
            visited.append((x, y))

            neighb = []
            CheckNeighbours()  # Sprawdzamy dla danej pozycji wolnych "sąsiadów"

            for event in pygame.event.get():  # Pętla for pozwala nam opuścić program w dowolnym momencie
                if event.type == pygame.QUIT:
                    exit = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

    pygame.quit()

# generate()
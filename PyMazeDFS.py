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
    #s = int(input("Podaj rozmiar labiryntu\n"))

    if (s % 2 == 0): s += 1

    screen = pygame.display.set_mode((s * 20, s * 20))
    pygame.display.set_caption("Project Labyrinth")

    # Tworzymy przestrzeń w której ma powstać labirynt
    grid = {(x, y): 1 for x in range(1, s + 1) for y in range(1, s + 1)}

    def CheckNeighbours():  # Funkcja sprawdza ile mamy wolnych sąsiednich kratek
        if (x + 2, y) not in visited and (x + 2, y) in grid:
            neighb.append("E")

        if (x - 2, y) not in visited and (x - 2, y) in grid:
            neighb.append("W")

        if (x, y + 2) not in visited and (x, y + 2) in grid:
            neighb.append("N")

        if (x, y - 2) not in visited and (x, y - 2) in grid:
            neighb.append("S")

    # Funkcje Draw* rysują nam ścieżkę
    def DrawLeft():
        pygame.draw.rect(screen, white, ((x + 1) * 20 - 20, y * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.001)

    def DrawRight():
        pygame.draw.rect(screen, white, ((x - 1) * 20 - 20, y * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.001)

    def DrawUp():
        pygame.draw.rect(screen, white, (x * 20 - 20, (y - 1) * 20 - 20, 20, 20))
        pygame.display.update()
        time.sleep(.001)

    def DrawDown():
        pygame.draw.rect(screen, white, (x * 20 - 20, (y + 1) * 20 - 20, 20, 20))
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
    queue.append((x, y))
    visited.append((x, y))
    pygame.draw.rect(screen, white, (0, 0, 20, 20))
    pygame.display.update()

    # Rozpoczynamy główną pętle
    exit = False
    while not exit:
        while len(queue) > 0:

            neighb = []
            CheckNeighbours()  # Sprawdzamy dla aktualnej pozycji czy istnieją wolni "sąsiedzi"

            if len(neighb) > 0:  # Jeżeli istnieją to wybieramy losowo jedną kratkę oraz rysujemy ścieżkę
                random_neighb = (random.choice(neighb))

                if random_neighb == "E":
                    x = x + 2
                    DrawRight()

                elif random_neighb == "W":
                    x = x - 2
                    DrawLeft()

                elif random_neighb == "N":
                    y = y + 2
                    DrawUp()

                elif random_neighb == "S":
                    y = y - 2
                    DrawDown()

                DrawPosition()
                queue.append((x, y))
                visited.append((x, y))  # Zaznaczamy nową pozycję jako odwiedzoną

            else:  # Jeżeli natomiast wolni "sąsiedzi" nie istnieją cofamy się do poprzedniej odwiedzonej kratki
                x, y = queue.pop()

            for event in pygame.event.get():  # Pętla for pozwala nam w dowolnym momencie opuścić program
                if event.type == pygame.QUIT:
                    exit = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
    pygame.quit()

#generate()
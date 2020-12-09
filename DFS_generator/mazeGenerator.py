#
#                        2 2 2                             0 1 2
#                       1 1 1 1                           0 1 2 3
#   Współrzędna x:     0 0 0 0 0     Współrzędna y:      0 1 2 3 4
#                      -1-1-1-1                           0 1 2 3
#                       -2-2-2                             0 1 2
#
#   Każda komóka posiada 2 współrzędne (x,y) gdzie x to numer wiersza, a y to numer komórki w tym wierszu
#   dla labiryntu o rozmiarze <size> (ilość pierścieni licząc komórkę środkową) x,y moga przyjmować wartosci z ponizszych przedzialow:
#   x € <-(size-1), size-1>
#   y € <0, 2(size-1) - abs(x)>
#   każda z komórek ma ściane w kierunku NE, E, SE, SW, W, NW

import random

NE, E, SE, SW, W, NW = ("ne", "e", "se", "sw", "w", "nw")


class Cell:

    # Zna: wspólrzedne x, y; sciany

    def __init__(self, x, y, walls):
        self.x = x
        self.y = y
        self.walls = set(walls)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        else:
            return False

    def __str__(self):
        return 'Cell(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.walls) + ')'

    # sprawdza czy komórka z wszystkich stron otoczona jest ścianami
    def is_fully_walled(self):
        return len(self.walls) == 6

    # usuwa ścianę przez którą komórki się łączą (jest przejście)
    def connect(self, other):
        self.walls.remove(self.wall_to(other))
        other.walls.remove(other.wall_to(self))

    # dla 2 podanych komórek zwraca ścianę którą się stykają
    def wall_to(self, other):
        if other.x - self.x == 1 and ((self.x >= 0 and other.y == self.y) or (self.x < 0 and other.y - self.y == 1)):
            return NE

        elif other.x == self.x and other.y - self.y == 1:
            return E

        elif other.x - self.x == -1 and ((self.x > 0 and other.y - self.y == 1) or (self.x <= 0 and other.y == self.y)):
            return SE

        elif other.x - self.x == -1 and (
                (self.x > 0 and other.y == self.y) or (self.x <= 0 and other.y - self.y == -1)):
            return SW

        elif other.x == self.x and other.y - self.y == -1:
            return W

        elif other.x - self.x == 1 and ((self.x >= 0 and other.y - self.y == -1) or (self.x < 0 and other.y == self.y)):
            return NW

class Maze:

    # Zna: rozmiar, listę komórek, kolejnosc komórek przy generowaniu, początkowa komorke, koncowo komorke, pozycje gracza

    def __init__(self, size=15):
        self.size = size
        self.cells = []
        self.cells_queue = []

        for x in range(1 - self.size, self.size):
            for y in range(0, 2 * (self.size - 1) - abs(x) + 1):
                self.cells.append(Cell(x, y, [NE, E, SE, SW, W, NW]))

    # dla podanych współrzędnych zwraca komórkę z listy komórek
    def get_cell(self, new_x, new_y):
        x = new_x
        y = new_y
        cell_index = 0
        if 1 - self.size <= x <= self.size - 1 and 0 <= y <= 2 * (self.size - 1) - abs(x):

            for n in range(1 - self.size, x):
                cell_index += 2 * (self.size - 1) - abs(n) + 1

            cell_index += y
            return self.cells[cell_index]
        else:
            return None

    # dla podanej komórki zwraca wszystkie możliwe komórki z którymi się styka bokiem
    def neighbours(self, cell):
        x = cell.x
        y = cell.y

        if x > 0:
            for (new_x, new_y) in [(x + 1, y), (x, y + 1), (x - 1, y + 1), (x - 1, y), (x, y - 1), (x + 1, y - 1)]:
                neighbour = self.get_cell(new_x, new_y)
                if neighbour is not None:
                    yield neighbour
        elif x < 0:
            for (new_x, new_y) in [(x + 1, y + 1), (x, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y)]:
                neighbour = self.get_cell(new_x, new_y)
                if neighbour is not None:
                    yield neighbour
        else:
            for (new_x, new_y) in [(x + 1, y), (x, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]:
                neighbour = self.get_cell(new_x, new_y)
                if neighbour is not None:
                    yield neighbour

    # losuje poczatek i koniec labiryntu
    def start_end(self):
        self.start_cell = random.choice(self.cells)
        self.player_cell = self.start_cell
        while True:
            self.finish_cell = random.choice(self.cells)
            if self.finish_cell != self.start_cell:
                break

    # tworzy losowy labirynt
    def randomize(self):

        cell_stack = []
        current_cell = random.choice(self.cells)
        visited_cells = 1
        self.cells_queue.append(current_cell)

        # print(current_cell, "numer komorki: " + str(visited_cells))     #zwraca kolejne komórki które są odwiedzane podczas tworzenia

        while visited_cells < len(self.cells):
            neighbours = [c for c in self.neighbours(current_cell) if c.is_fully_walled()]
            if len(neighbours):
                neighbour = random.choice(neighbours)
                current_cell.connect(neighbour)
                cell_stack.append(current_cell)
                visited_cells += 1
                current_cell = neighbour
                self.cells_queue.append(current_cell)
                # print(current_cell, "numer komorki: " + str(visited_cells))
            else:
                current_cell = cell_stack.pop()

    # generuje labirynt
    @staticmethod
    def generate(size):
        maze = Maze(size)
        maze.randomize()
        maze.start_end()
        return maze

# Genereting maze with Prim Algorithm
from pprint import pprint
import random

DIM = 7
START_CELL = (0, 0)

size = 2*DIM - 1

grid = [[0 for _ in range(size)] for _ in range(size)]
for x in range(0, size, 2):
    for y in range(0, size, 2):
        grid[x][y] = 1


def walls_of_cell(cell):
    walls = set()
    row = cell[0]
    col = cell[1]

    if row-1>0:
        walls.add((row-1, col))
    if row+1<size:
        walls.add((row+1, col))
    if col-1>0:
        walls.add((row, col-1))
    if col+1<size:
        walls.add((row, col+1))

    return walls


def cells_of_wall(wall):
    row = wall[0]
    col = wall[1]
    if row % 2 == 0:
        return {(row, col-1), (row, col+1)}
    else:
        return {(row-1, col), (row+1, col)}


def make_passage(wall):
    row = wall[0]
    col = wall[1]
    grid[row][col] = 1


visited_cells = {START_CELL}
walls_to_check = walls_of_cell(START_CELL)

while walls_to_check:
    wall = random.sample(walls_to_check, 1)[0]
    unvisited_cell = cells_of_wall(wall) - visited_cells
    if unvisited_cell:
        cell = unvisited_cell.pop()
        make_passage(wall)
        visited_cells.add(cell)
        walls_to_check.update(walls_of_cell(cell))

    walls_to_check.remove(wall)

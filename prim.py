# Genereting maze with Prim Algorithm
from pprint import pprint
import random
import pygame

def hania_prim(s):
    START_CELL = (0, 0)
    grid_size = 10
    white =(255, 255, 255)
    black =(0, 0, 0)
    
    size = 2 * s - 1
    
    # Create a grid with ones in place of cells/nodes
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(0, size, 2):
        for y in range(0, size, 2):
            grid[x][y] = 1
    
    
    # Get walls which are around cell
    def walls_of_cell(cell):
        walls = set()
        row = cell[0]
        col = cell[1]
    
        if row - 1 > 0:
            walls.add((row - 1, col))
        if row + 1 < size:
            walls.add((row + 1, col))
        if col - 1 > 0:
            walls.add((row, col - 1))
        if col + 1 < size:
            walls.add((row, col + 1))
    
        return walls
    
    
    # Get which two cells the wall divides
    def cells_of_wall(wall):
        row = wall[0]
        col = wall[1]
        # Even row -> wall divides cells which are in one row
        if row % 2 == 0:
            return {(row, col - 1), (row, col + 1)}
        # Odd row -> wall divides cells which are in one column
        else:
            return {(row - 1, col), (row + 1, col)}
    
    
    # Change a wall (0) to passage (1)
    def make_passage(wall):
        row = wall[0]
        col = wall[1]
        grid[row][col] = 1
    
    
    visited_cells = {START_CELL}
    walls_to_check = walls_of_cell(START_CELL)
    
    # Prim's algorithm implementation
    while walls_to_check:
        wall = random.sample(walls_to_check, 1)[0]  # Random.sample returns single-element list in this case
        unvisited_cell = cells_of_wall(wall) - visited_cells
        if unvisited_cell:
            cell = unvisited_cell.pop()  # Univisited cell is a single-element set
            make_passage(wall)
            visited_cells.add(cell)
            walls_to_check.update(walls_of_cell(cell))
    
        walls_to_check.remove(wall)

    def Draw(a,b):
        if grid[a][b] == 1:
            pygame.draw.rect(screen,white,[a*grid_size,b*grid_size,grid_size,grid_size])
        elif grid[a][b]==0:
            pygame.draw.rect(screen,black,[a*grid_size,b*grid_size,grid_size,grid_size])
    
        pygame.display.update()
        pygame.time.delay(10)

    screen = pygame.display.set_mode((size * grid_size, size * grid_size))

    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        for i in range(size):
            for j in range(size):
                Draw(j,i)
   
    pygame.quit()



    
import pygame

import DFS_generator.mazeGenerator as mazeGenerator


def changePos(k1, k2, maze):
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


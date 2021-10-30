import pygame
from pygame.locals import * 
import random
import sys

from MazeGenerator import Maze

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 380
WINDOW_WIDTH = 380

def drawGrid(maze):
    block_width = WINDOW_WIDTH // maze.numCols()
    block_height = WINDOW_HEIGHT // maze.numRows()

    for x in range(0, WINDOW_WIDTH, block_width):
        for y in range(0, WINDOW_HEIGHT, block_height):
            rect = pygame.Rect(x, y, block_width, block_height)
            if maze.accessMatrix(x // block_width, y // block_height):
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                pygame.draw.rect(SCREEN, WHITE, rect)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    maze = Maze(10, 10)
    maze.kruskal()

    while(1):
        drawGrid(maze)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    maze = Maze(10, 10)
                    maze.kruskal()

        pygame.display.update()

    return 0

if __name__ == '__main__':
    sys.exit(main())

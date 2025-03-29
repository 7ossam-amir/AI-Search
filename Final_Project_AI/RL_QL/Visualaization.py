import pygame
import time

 
CELL_SIZE = 20 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def init_display(maze):
  
    pygame.init()
    maze_height, maze_width = len(maze), len(maze[0])
    screen = pygame.display.set_mode((maze_width * CELL_SIZE, maze_height * CELL_SIZE))
    pygame.display.set_caption("Maze Solver Visualization")
    return screen

def draw_maze(screen, maze, start, goal):
 
    screen.fill(WHITE)
    maze_height, maze_width = len(maze), len(maze[0])
    for x in range(maze_height):
        for y in range(maze_width):
            color = WHITE if maze[x][y] == 1 else BLACK
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
  
    pygame.draw.rect(screen, RED, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (goal[1] * CELL_SIZE, goal[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

def update_position(screen, maze, position, color, start, goal, episode=None, step_type=None, delay=0):
    draw_maze(screen, maze, start, goal)
    x, y = position
    pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    if delay > 0:
        pygame.time.delay(delay)



def visualize_path(screen, path):
 
    for x, y in path:
        pygame.draw.rect(screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        time.sleep(0.05)

def close_display():
 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

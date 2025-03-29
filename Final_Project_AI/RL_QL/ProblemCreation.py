import numpy as np
import random

problem_width = 15
problem_height = 15
maze = np.ones((problem_height, problem_width), dtype=int)
obstacles_ratio = 0.25
number_blocked_blocks = int(problem_width * problem_height * obstacles_ratio)
blocked_blocks = random.sample([(x, y) for x in range(problem_height) for y in range(problem_width)], number_blocked_blocks)

for x, y in blocked_blocks:
    maze[x, y] = 0

start_state = (0, 0)
goal_state = (problem_height - 1, problem_width - 1)
maze[start_state] = 1
maze[goal_state] = 1

action_values = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def actions(state):
    return list(action_values.keys())


def do_action(state, action):
    x, y = state
    dx, dy = action_values[action]
    nx, ny = x + dx, y + dy
    if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1]:
        return (nx, ny)   
    return state  

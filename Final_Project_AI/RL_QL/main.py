import pygame
import numpy as np
from ProblemCreation import maze, start_state, goal_state, actions, do_action, action_values
from Visualaization import init_display, draw_maze, visualize_path, close_display
from QL import Q_L
from Evaluation import evaluation  

def extract_path(q_table, start_state, goal_state, action_values):
    path = [start_state]
    current_state = start_state

    while current_state != goal_state:
        x, y = current_state
        action_index = np.argmax(q_table[x, y]) 
        action = list(action_values.keys())[action_index]
        next_state = do_action(current_state, action)
        path.append(next_state)
        current_state = next_state
    return path


def main():
    screen = init_display(maze)
    draw_maze(screen, maze, start_state, goal_state)
    trained_q_table = Q_L(
        maze, start_state, goal_state, actions, 
        screen=None,
        iterations=1000, alpha=0.1, gamma=0.9, epsilon=0.2
    )
    evaluation_result = evaluation(trained_q_table, maze, start_state, goal_state, action_values)
    print(evaluation_result)
    optimal_path = extract_path(trained_q_table, start_state, goal_state, action_values)
    print("Optimal Path:", optimal_path)
    visualize_path(screen, optimal_path)
    close_display()

if __name__ == "__main__":
    main()

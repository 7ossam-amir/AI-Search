import numpy as np
from ProblemCreation import maze, start_state, goal_state, actions, do_action, action_values
from Visualaization import init_display, draw_maze, update_position, visualize_path, close_display
from QL import Q_L, q_table  

def evaluation(q_table, maze, start_state, goal_state, action_values):
    current_state = start_state
    reward_for_evaluation =0
    reward = 0
    steps =0
    max_steps = maze.shape[0]*maze.shape[1] -(0.25*maze.shape[0]*maze.shape[1])
    correct_steps = 0   

    while current_state != goal_state:
        #bageb el action mn el q table el leh a3la reward 
        x ,y = current_state
        action_index = np.argmax(q_table[x,y])
        action = list(action_values.keys())[action_index]
        next_state = do_action(current_state, action)
        #h7seb el reward el wsltelo l7d dlw2ty
        if next_state == goal_state:    
            reward = 100
        elif maze[next_state] == 0:
            reward = -10
        else :
            reward = -1

        reward_for_evaluation += reward
        steps += 1

        # check if the agent chose the optimal step or not 
        agent_action_index = np.argmax(q_table[x, y])
        if agent_action_index == action_index:
            correct_steps += 1
            
        current_state = next_state

        if(steps > max_steps):
            accuracy = (correct_steps / steps) * 100
            return("failed to get the optimal and accuracy is:",accuracy, reward_for_evaluation, steps)

    accuracy = (correct_steps / steps) * 100
    return("succeeded to get the optimal and accuracy is:", accuracy, reward_for_evaluation, steps)
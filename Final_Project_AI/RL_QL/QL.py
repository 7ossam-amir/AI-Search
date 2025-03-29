import numpy as np
import random
from ProblemCreation import do_action, action_values,goal_state


def reward_func(state, goal_state, maze):
    if state == goal_state:
        return 100  
    elif maze[state[0], state[1]] == 0:
        return -10 
    return -1

def q_table(maze, n_actions):
    return np.zeros((*maze.shape, n_actions))

def update_q_value(state, action, reward, next_state, q_table, actions_dict, alpha, gamma):
    x, y = state
    nx, ny = next_state
    if next_state == goal_state:
        next_max = 0  
        q_table[nx, ny, :] = reward  
    else:
        next_max = np.max(q_table[nx, ny])  
    action_index = list(actions_dict.keys()).index(action)
    q_table[x, y, action_index] += alpha * (reward + gamma * next_max - q_table[x, y, action_index])



def Q_L(maze, start_state, goal_state, actions_function, screen=None, iterations=1000, alpha=0.1, gamma=0.9, epsilon=0.2, update_freq=50):
    q_table_data = q_table(maze, len(action_values))
    for episode in range(iterations):
        current_state = start_state
        while current_state != goal_state:
            if random.uniform(0, 1) < epsilon:
                action = random.choice(list(action_values.keys()))
            else:
                action = list(action_values.keys())[np.argmax(q_table_data[current_state[0], current_state[1]])]
            next_state = do_action(current_state, action)
            reward = reward_func(next_state, goal_state, maze)
            update_q_value(current_state, action, reward, next_state, q_table_data, action_values, alpha, gamma)
            current_state = next_state
        if screen and episode % update_freq == 0:
            print(f"Episode {episode}: Visualizing...")
    return q_table_data




def Q_L2(maze, start_state, goal_state, actions_function, iterations=1000, alpha=0.1, gamma=0.9, epsilon=0.2):
    q_table_data = q_table(maze, len(action_values))
    rewards_per_episode = []
    exploration_counts = []
    exploitation_counts = []

    for episode in range(iterations):
        current_state = start_state
        total_reward = 0
        exploration_count = 0
        exploitation_count = 0

        while current_state != goal_state:
            if random.uniform(0, 1) < epsilon:
                action = random.choice(list(action_values.keys()))
                exploration_count += 1
            else:
                q_values = q_table_data[current_state[0], current_state[1]]
                action_index = np.argmax(q_values)
                action = list(action_values.keys())[action_index]
                exploitation_count += 1

            next_state = do_action(current_state, action)
            reward = reward_func(next_state, goal_state, maze)
            update_q_value(current_state, action, reward, next_state, q_table_data, action_values, alpha, gamma)

            current_state = next_state
            total_reward += reward
            # if current_state == goal_state:
            #     break  
        rewards_per_episode.append(total_reward)
        exploration_counts.append(exploration_count)
        exploitation_counts.append(exploitation_count)
    return q_table_data, rewards_per_episode, exploration_counts, exploitation_counts

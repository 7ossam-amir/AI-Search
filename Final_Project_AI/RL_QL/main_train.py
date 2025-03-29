import numpy as np
from ProblemCreation import maze, start_state, goal_state, actions, action_values
from QL import Q_L2
import matplotlib.pyplot as plt

def plot_training_metrics(rewards, exploration_counts, exploitation_counts):
    plt.figure(figsize=(10, 5))
    plt.plot(rewards, label="Total Reward per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Training Rewards")
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 5))
    episodes = list(range(len(exploration_counts)))
    plt.plot(episodes, exploration_counts, label="Exploration Count")
    plt.plot(episodes, exploitation_counts, label="Exploitation Count")
    plt.xlabel("Episode")
    plt.ylabel("Count")
    plt.title("Exploration vs Exploitation")
    plt.legend()
    plt.grid()
    plt.show()

def plot_q_value_heatmap(q_table):
    max_q_values = np.max(q_table, axis=2)  
    max_q_values[max_q_values < 1e-3] = 0  
    plt.figure(figsize=(8, 8))
    plt.imshow(max_q_values, cmap="viridis", origin="upper", interpolation='nearest')
    plt.colorbar(label="Max Q-Value")
    plt.title("Q-Value Heatmap After Training")
    plt.xlabel("Y-axis (Width)")
    plt.ylabel("X-axis (Height)")
    plt.show()


def main_training():
    trained_q_table, rewards, exploration_counts, exploitation_counts = Q_L2(
        maze, start_state, goal_state, actions, iterations=1000, alpha=0.1, gamma=0.9, epsilon=0.2
    )

    plot_training_metrics(rewards, exploration_counts, exploitation_counts)
    plot_q_value_heatmap(trained_q_table)

if __name__ == "__main__":
    main_training()

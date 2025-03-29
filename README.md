Maze Navigation using Q-Learning
Project Overview

This project implements a Q-Learning algorithm to train an agent to navigate through a dynamically generated maze. The agent starts at the top-left corner (0,0) and aims to reach the bottom-right corner (14,14) while maximizing rewards and avoiding obstacles.
Key Features

    Dynamic Maze Generation: 15×15 grid with 25% randomly distributed obstacles

    Q-Learning Implementation:

        Reward system: +100 for goal, -10 for obstacles, -1 for valid moves

        Exploration rate (ε) of 0.2

    Visualization: Real-time path visualization using Pygame

    Performance Metrics: Tracks optimal path, accuracy, rewards, and steps

Requirements

    Python 3.x

    Pygame library

    NumPy

Installation

    Clone the repository:
    bash
    Copy

    git clone https://github.com/7ossam-amir/AI-Search

    Navigate to the project directory:
    bash
    Copy

    cd AI-Search

    Install required packages:
    bash
    Copy

    pip install -r requirements.txt

Usage

Run the main script to start the Q-Learning process:
bash
Copy

python maze_qlearning.py

Results

The implementation demonstrates:

    Successful maze navigation learning

    Q-table improvement through training

    Visualization of the optimal path (as shown in project figures)

References

    Q-Learning Algorithm: From explanation to implementation

    Pygame Library

Project Link

GitHub Repository: https://github.com/7ossam-amir/AI-Search

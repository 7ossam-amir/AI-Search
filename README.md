 Maze Navigation using Q-Learning

## Project Overview
This project implements a Q-Learning algorithm to train an agent to navigate through a dynamically generated maze. The agent starts at the top-left corner (0,0) and aims to reach the bottom-right corner (14,14) while maximizing rewards and avoiding obstacles.

## Git Flow Structure
We follow the Git Flow workflow for development:

main (production-ready releases)
│
└── develop (integration branch for features)
│
├── feature/* (new features)
├── release/* (pre-release branches)
├── hotfix/* (critical bug fixes)
└── docs/* (documentation updates)
Copy


## File Structure

AI-Search/
├── src/ # Source code
│ ├── maze_qlearning.py # Main Q-Learning implementation
│ ├── maze_generator.py # Maze generation logic
│ └── visualization.py # Pygame visualization module
│
├── tests/ # Test cases
│ ├── test_maze.py # Maze generation tests
│ └── test_qlearning.py # Q-Learning algorithm tests
│
├── docs/ # Documentation
│ ├── design.md # System design
│ └── results/ # Evaluation results
│
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
└── README.md # This file
Copy


## Key Features
- **Dynamic Maze Generation**: 15×15 grid with 25% randomly distributed obstacles
- **Q-Learning Implementation**: 
  - Reward system: +100 for goal, -10 for obstacles, -1 for valid moves
  - Exploration rate (ε) of 0.2
- **Visualization**: Real-time path visualization using Pygame
- **Performance Metrics**: Tracks optimal path, accuracy, rewards, and steps

## Development Workflow
1. Create a feature branch from `develop`:
   ```bash
   git checkout -b feature/new-feature develop

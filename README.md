# Tiny_RL_Projects

Here are some tiny RL projects I did for fun. I will keep updating this repo. There will be some projects on RL Q-learning, DQN, Policy Gradient, Actor-Critic, etc.

1. Q-learning: This project is about Q-learning. I implemented Q-learning algorithm to solve the maze problem. There I **did not** use OpenAI Gym environment. The grid size and number of blocks, i.e. complexity of the environment can be modified. The agent starts at the bottom and the goal is to reach the bottom row. The agent can move in four directions: left, right, up, and down. The agent will stay in the same sate if it bumps into walls or the blocks. The agent will receive a reward of -1 for each step, -100 bumping into the blocks and a reward of 10 getting to the top row.

This can be a good practice for Q-learning algorithm. The Q-table is initialized with zeros. The agent will explore the environment and update the Q-table.

2. 
import numpy as np
import matplotlib.pyplot as plt

# Define the grid
grid = np.array([
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
])

# Define the start and goal
start = (0, 0)
goal = (4, 4)

# Define the potential field
potential_field = np.zeros_like(grid, dtype=np.float32)
potential_field[goal] = 100  # Set the goal potential
potential_field[grid == 1] = -100  # Set the obstacle potential

# Define the Q-table
Q = np.zeros_like(grid, dtype=np.float32)

# Define the learning parameters
alpha = 0.5
gamma = 0.9
epsilon = 0.1
n_episodes = 1000

# Define the actions (up, down, left, right)
actions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# Q-Learning with APF
for episode in range(n_episodes):
    state = start
    while state != goal:
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(len(actions))  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit
        next_state = (state[0] + actions[action][0], state[1] + actions[action][1])
        reward = potential_field[next_state]
        Q[state][action] = Q[state][action] + alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])
        state = next_state

# Visualize the policy
plt.imshow(grid, cmap='Greys')
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == 0:
            action = np.argmax(Q[(i, j)])
            if action == 0: plt.arrow(j, i, 0, -0.3, color='r', head_width=0.1)
            if action == 1: plt.arrow(j, i, 0, 0.3, color='r', head_width=0.1)
            if action == 2: plt.arrow(j, i, -0.3, 0, color='r', head_width=0.1)
            if action == 3: plt.arrow(j, i, 0.3, 0, color='r', head_width=0.1)
plt.show()

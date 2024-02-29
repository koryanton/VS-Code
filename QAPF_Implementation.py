import numpy as np
import matplotlib.pyplot as plt

# Define grid size and obstacles
GRID_SIZE = 10
obstacles = [(2, 3), (3, 5), (5, 7)]  # Coordinates of obstacles

# Define start and goal positions
start_pos = (0, 0)
goal_pos = (GRID_SIZE - 1, GRID_SIZE - 1)

# Initialize Q-values
Q = np.zeros((GRID_SIZE, GRID_SIZE, 4))  # 4 actions: up, down, left, right

# Define parameters
epsilon = 0.6
alpha = 0.5
gamma = 0.9

# Define action mapping (up, down, left, right)
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Initialize plot
plt.figure(figsize=(8, 8))

# Function to plot obstacles
def plot_obstacles():
    for obstacle in obstacles:
        plt.fill_between([obstacle[1], obstacle[1] + 1], obstacle[0], obstacle[0] + 1, color='gray')

# Function to plot agent
def plot_agent(agent_pos):
    plt.plot(agent_pos[1] + 0.5, agent_pos[0] + 0.5, 'ro', markersize=10)

# Function to plot goal
def plot_goal(goal_pos):
    plt.plot(goal_pos[1] + 0.5, goal_pos[0] + 0.5, 'go', markersize=10)

# Function to update Q-values based on Q-learning algorithm
def update_Q(agent_pos, action, reward, next_agent_pos):
    max_next_Q = np.max(Q[next_agent_pos[0], next_agent_pos[1]])
    current_Q = Q[agent_pos[0], agent_pos[1], action]
    Q[agent_pos[0], agent_pos[1], action] = (1 - alpha) * current_Q + alpha * (reward + gamma * max_next_Q)

# Function to choose action using epsilon-greedy policy
def choose_action(agent_pos):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(4)  # Choose random action
    else:
        return np.argmax(Q[agent_pos[0], agent_pos[1]])

# Function to check if a position is valid (within grid and not obstacle)
def is_valid_pos(pos):
    return 0 <= pos[0] < GRID_SIZE and 0 <= pos[1] < GRID_SIZE and pos not in obstacles

# Function to calculate artificial potential field
def calculate_potential_field(agent_pos):
    potential_field = np.zeros((GRID_SIZE, GRID_SIZE))
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) != agent_pos:
                distance = np.linalg.norm(np.array(agent_pos) - np.array((i, j)))
                potential_field[i, j] = 1 / distance
    return potential_field

# Main loop
agent_pos = start_pos
num_episodes = 10000

for _ in range(num_episodes):
    while agent_pos != goal_pos:
        # Choose action
        action = choose_action(agent_pos)
        
        # Move agent
        next_agent_pos = (agent_pos[0] + actions[action][0], agent_pos[1] + actions[action][1])
        if is_valid_pos(next_agent_pos):
            agent_pos = next_agent_pos
        
        # Calculate reward
        if agent_pos == goal_pos:
            reward = 100
        elif agent_pos in obstacles:
            reward = -10
        else:
            reward = 0
        
        # Update Q-values
        update_Q(agent_pos, action, reward, next_agent_pos)
        
        # Plot grid world
        plt.clf()
        plt.xlim(0, GRID_SIZE)
        plt.ylim(0, GRID_SIZE)
        plot_obstacles()
        plot_goal(goal_pos)
        plot_agent(agent_pos)
        plt.title('Q-learning Artificial Potential Field')
        plt.pause(0.01)

# Show final plot
plt.show()

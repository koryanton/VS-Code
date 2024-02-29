import numpy as np
import random
import matplotlib.pyplot as plt

newState = np.array([[1, 2, 1, 5],
                     [1, 3, 2, 6],
                     [2, 4, 3, 7],
                     [3, 4, 4, 8],
                     [5, 6, 1, 9],
                     [5, 7, 2, 10],
                     [6, 8, 3, 11],
                     [7, 8, 4, 12],
                     [9, 10, 5, 13],
                     [9, 11, 6, 14],
                     [10, 12, 7, 15],
                     [11, 12, 8, 16],
                     [13, 14, 9, 13],
                     [13, 15, 10, 14],
                     [14, 16, 11, 15],
                     [15, 16, 12, 16]])

Q = np.zeros((16, 4))
tao = 0.99
ata = 0.2
beta = 0.4
s = 0
s_history = [s]
i = 1

Q_history = []

while i <= 5000:
    total_exp = 0
    for a in range(4):
        total_exp += np.exp(Q[s, a] / tao)

    P = [np.exp(Q[s, a] / tao) / total_exp * 100 for a in range(4)]

    ran = 100 * random.random()

    if ran <= P[0]:
        a = 0
    elif ran > P[0] and ran <= (P[0] + P[1]):
        a = 1
    elif ran > (P[0] + P[1]) and ran <= (P[0] + P[1] + P[2]):
        a = 2
    else:
        a = 3

    newS = int(newState[s, a]) - 1  # Adjust index to Python's 0-based indexing

    if newS == 11:
        r = 20
    elif newS == 6 or newS == 13:
        r = -10
    else:
        r = 0

    maxQ = np.max(Q[newS, :])
    Q[s, a] = (1 - ata) * Q[s, a] + ata * (r + beta * maxQ)
    s_history.append(newS)

    if newS == 11:
        path = [x+1 for x in s_history]
        print("-------------------------------")
        print("The goal has been reached! The path is:")
        print(path)
        print("")
        print("Return to Start position now")
        s_history = [0]
        path = [0]
        s = 0
    else:
        s = newS
    tao *= 0.999
    if tao < 0.01:
        tao = 0.01

    i += 1

    Q_history.append(Q.copy())

# Extract Q-values for plotting
Q_9_1 = [Q_history[j][8, 0] for j in range(len(Q_history))]
Q_9_2 = [Q_history[j][8, 1] for j in range(len(Q_history))]
Q_9_3 = [Q_history[j][8, 2] for j in range(len(Q_history))]
Q_9_4 = [Q_history[j][8, 3] for j in range(len(Q_history))]



# Plotting Q-values
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(Q_history) + 1), Q_9_1, label='Q(9,1)')
plt.plot(range(1, len(Q_history) + 1), Q_9_2, label='Q(9,2)')
plt.plot(range(1, len(Q_history) + 1), Q_9_3, label='Q(9,3)')
plt.plot(range(1, len(Q_history) + 1), Q_9_4, label='Q(9,4)')
plt.xlabel('Iterations')
plt.ylabel('Q-values')
plt.title('Q-values history curve')
plt.legend()
plt.grid(True)


# Extract x and y coordinates from s_history
x_coords = [state % 4 for state in s_history]  
y_coords = [state // 4 for state in s_history]  

# Plot the path taken
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
plt.title('Path Taken ')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
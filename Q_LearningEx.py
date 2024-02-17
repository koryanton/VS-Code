import numpy as np
import random
import matplotlib.pyplot as plt

newState = np.array([[1,  2,  1,  5 ],
                     [1,  3,  2,  6 ],
                     [2,  4,  3,  7 ],
                     [3,  4,  4,  8 ],
                     [5,  6,  1,  9 ],
                     [5,  7,  2,  10],
                     [6,  8,  3,  11],
                     [7,  8,  4,  12],
                     [9,  10, 5,  13],
                     [9,  11, 6,  14],
                     [10, 12, 7,  15],
                     [11, 12, 8,  16],
                     [13, 14, 9,  13],
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

    newS = int(newState[s, a])

    if newS == 12:
        r = 20
    elif newS == 7 or newS == 14:
        r = -10
    else:
        r = 0

    maxQ = np.max(Q[newS, :])
    Q[s, a] = (1 - ata) * Q[s, a] + ata * (r + beta * maxQ)
    s_history.append(newS)

    if newS == 12:
        print("-------------------------------")
        print("The goal has been reached! The path is:")
        print(s_history)
        print("")
        print("Return to Start position now")
        s_history = [0]
        s = 0
    else:
        s = newS
    tao *= 0.999
    if tao < 0.01:
        tao = 0.01

    i += 1

Q_history = []
for _ in range(len(Q_history)):
    Q_history.append(Q)

Q_9_1 = np.zeros(len(Q_history))
Q_9_2 = np.zeros(len(Q_history))
Q_9_3 = np.zeros(len(Q_history))
Q_9_4 = np.zeros(len(Q_history))

for i in range(len(Q_history)):
    Q_9_1[i] = Q_history[i][8, 0]
    Q_9_2[i] = Q_history[i][8, 1]
    Q_9_3[i] = Q_history[i][8, 2]
    Q_9_4[i] = Q_history[i][8, 3]

plt.plot(Q_9_1)
plt.plot(Q_9_2)
plt.plot(Q_9_3)
plt.plot(Q_9_4)
plt.show()

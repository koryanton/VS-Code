import numpy as np
import matplotlib.pyplot as plt

# Probability that the robot can be at P_n coming from P_n-1
p_of_x_t_from_P_n =[
#   [ P0 , P1 , P2, P3 ] 
    [0.2, 0.7, 0.1, 0.0],
    [0.0, 0.2, 0.7, 0.1],
    [0.0, 0.0, 0.2, 0.7],
    [0.0, 0.0, 0.0, 0.2]]
# Probability the robot is at 𝑃n coming from 𝑃n-1 * bel_star p_of_x_t_from_P_n[i][ii] * bel[i]
x_t_for_P_n = [
#   [ P0 , P1 , P2, P3 ] 
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0]]

# Measurement z_t[wall_facing_wall,door_facing_wall, wall_facing_door, door_facing_door] }
#z_t =[ P0 , P1 , P2, P3] 
p_z_t_door = [0.25,0.7,0.25,0.7]
p_z_t_wall = [0.75,0.3,0.75,0.3]
labels = ['P0', 'P1', 'P2', 'P3']
bel = [0.25, 0.25, 0.25, 0.25]
# Belief star current and previous  bel = normal * z_t[P_n] * x_t_from_P_n[i][ii] 
bel_star = [0.0, 0.0, 0.0, 0.0]
x_t_from_P_n_sum = 0
#bel_sum = 
bel_sum = 1
# Normal = 
normal = 0
#print(z_t[0])

def plot_graph(labels,vector):
    plt.bar(labels, bel_star)
    plt.xlabel('States')
    plt.ylabel('bel(x_0)')
    plt.title('Bar Plot from a Vector')
    plt.show()
    return 0

def update_states(prev_state, prev_belief, prob_matrix):
    for i in range(4):
        for j in range(4):
            prev_state[i][j] = round(prev_belief[i] * prob_matrix[i][j],3)
    for row in x_t_for_P_n:
        print(row)
    return 0


print('\nInitial belief values at x0  \n\n  P0 ,  P1 ,  P2,   P3\n' + str(bel))
print('\nStates P0 to P3 at time t = 1, given p(x_t = p_n|u_1 = 1, x_n-1 = p_n)\
       \n\n  P0 ,  P1 ,   P2,   P3')

update_states(x_t_for_P_n, bel, p_of_x_t_from_P_n )
# for i in range(4):
#     for j in range(4):
#         x_t_for_P_n[i][j] = round(bel[i] * p_of_x_t_from_P_n[i][j],3)

# for row in x_t_for_P_n:
#     print(row)

i = 3
for row in x_t_for_P_n:
    row_sum = 0
    for element in row:
        row_sum += element
    bel_star[i] = round(row_sum,3)
    i -= 1
bel = bel_star
print( '\nBelStar:' + str(bel_star)+ '\n')

print('\nControl update of Bayes filter \n\n\t   P0 ,   P1 ,    P2,    P3' )

for i in range(4):
    bel_star[i] =  bel[i]*p_z_t_door[i]
bel_sum = sum(bel_star)
normal = round(1/bel_sum,3)
bel = bel_star

for i in range(4):
    bel_star[i] =  round(bel[i]*normal,3)

print( 'BelStar: ' + str(bel_star)+ '\n'+ 'Normal: ' + str(normal)+ '\n')

plot_graph(labels,bel_star)

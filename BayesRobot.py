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
base_belief = [0.25,0.25,0.25,0.25]
p_z_t_door = [0.25,0.7,0.25,0.7]
p_z_t_wall = [0.75,0.3,0.75,0.3]
# Labels for outputs
labels = 'P0     P1     P2     P3'
states = ['P0','P1','P2','P3']
bel = [0.0, 0.0, 0.0, 0.0]
# Belief star current and previous  bel = normal * z_t[P_n] * x_t_from_P_n[i][ii] 
bel_star = [0.0, 0.0, 0.0, 0.0]
States = ' ' 
bel_sum = 0
normal = 0
n = 3
# Function to plot graphs
def plot_graph(labels,Bel,Bel_Star,States):
    plt.figure(figsize=(6, 4))  # Adjust the figure size as needed
    plt.subplot(211)  # 1st subplot (1 row, 3 columns, 1st position)
    plt.bar(labels, Bel_Star)
    plt.title('Bel_Star')

    plt.subplot(212)  # 2nd subplot (1 row, 3 columns, 2nd position)
    plt.bar(labels,Bel)
    plt.title('Bel')
    plt.xlabel(States)
    plt.tight_layout()
    plt.show()
    return 0
# Main Bayes filter algorithm 
def update_states(prev_state, prev_belief, updated_belief, prob_matrix, n = n):
    # Initial belief conditions
    prev_belief = base_belief
    for i in range(n):
        # Prints initial conditions data
        States = (str(states[i]) +  ' to ' + str(states[i+1]))
        print('\nStates: ' + States + ' at time = ' + str(i) + \
        '\nGiven p(x_t = p_n|u_1 = 1, x_n-1 = p_n)\n')
        print('\nInitial belief values at x_' + str(i) + '\n\nBel:\n' + str(labels))
        # Step for measurement given the current state
        measurement = p_z_t_wall if (i+1) % 2 == 0 else p_z_t_door
        #Calculates summation of each state given the current belief
        for i in range(4):
            for j in range(4):
                prev_state[i][j] = prob_matrix[i][j] * prev_belief[i]
        y0 = prev_belief
        # Calculates and updates Belief and Belief Star
        for i in range(4):
            row_sum = 0
            for j in range(4):
                #Transponds the matrix to find the summation of all states P0 to P3 at time = n
                row_sum += prev_state[j][i] 
            updated_belief[i] = round(row_sum,3)
        print(str(np.around(prev_belief,3))+'\n\n'+str(np.around(prev_state,3)))
        prev_belief = updated_belief
        y1 = updated_belief

        # Updates Belief given the measurement (z_n)
        for i in range(4):
            updated_belief[i] =  prev_belief[i] * measurement[i]
        bel_sum = sum(updated_belief)
        normal = round(1/bel_sum,3)

        print('\nControl update of Bayes filter \n')        
        #Calculates Belief Star
        for i in range(4):
            updated_belief[i] =  round(prev_belief[i]*normal,3)
        # prev_belief = updated_belief
    
        print( 'BelStar: ' + '\n  ' + str(labels) + '\n' + str(updated_belief)+ \
            '\n\n'+ 'Normal: ' + str(normal)+ '\n')
        normal = 0
        plot_graph(states,y1,y0,States)

update_states(x_t_for_P_n, bel, bel_star, p_of_x_t_from_P_n, n)

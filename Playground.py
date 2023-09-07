import matplotlib.pyplot as plt
import numpy as np
  
# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

# b = [1,2,3]

# c = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# for i in range(3):
#     for j in range(3):
#         c[i][j] = (a[i][j]*b[i])
#         # c[i][j] = a[j][i]
# for row in c:
#     print(str(row))
# print('\nMatrix sum\n')

# for i in range(3):
#     row_sum = 0
#     for j in range(3):
#         row_sum += c[i][j]
#     b[i] = round(row_sum,3)
# print(b)



# Create some sample data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create subplots with 1 row and 3 columns
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
plt.subplot(311)  # 1st subplot (1 row, 3 columns, 1st position)
plt.plot(x, y1)
plt.title('Sine Function')

plt.subplot(312)  # 2nd subplot (1 row, 3 columns, 2nd position)
plt.plot(x, y2)
plt.title('Cosine Function')

plt.subplot(313)  # 3rd subplot (1 row, 3 columns, 3rd position)
plt.plot(x, y3)
plt.ylim(-5, 5)  # Set y-axis limits for the third subplot
plt.title('Tangent Function')

plt.tight_layout()  # Adjust subplot spacing for a cleaner layout
plt.show()
# print(np.around(prev_state,3))
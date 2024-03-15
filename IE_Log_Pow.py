import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Load the image
image = cv2.imread('fourierspectrum.pgm', cv2.IMREAD_GRAYSCALE)

# Define gamma values for power-law transformation
gamma_values = [0.5, 1, 2]

# Function to perform log transformation
def log_transformation(image):
    start_time = time.time()
    transformed_image = np.log1p(image.astype(np.float32))
    runtime = time.time() - start_time
    return transformed_image, runtime

# Function to perform power-law (gamma) transformation
def power_law_transformation(image, gamma):
    start_time = time.time()
    transformed_image = np.power(image / 255.0, gamma) * 255.0
    runtime = time.time() - start_time
    return transformed_image, runtime

# Create subplots
fig, axs = plt.subplots(2, len(gamma_values) + 1, figsize=(15, 6))

# Display original image
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original Image')

# Display log transformation and plot runtime
log_transformed, log_runtime = log_transformation(image)
axs[1, 0].imshow(log_transformed, cmap='gray')
axs[1, 0].set_title('Log Transformed')
axs[1, 0].text(0.5, -0.2, f'Runtime: {log_runtime:.6f} sec', ha='center', transform=axs[1, 0].transAxes)

# Display power-law transformation for different gamma values and plot runtime
for i, gamma in enumerate(gamma_values):
    power_law_transformed, power_law_runtime = power_law_transformation(image, gamma)
    axs[0, i+1].imshow(power_law_transformed, cmap='gray')
    axs[0, i+1].set_title(f'Power-law (gamma={gamma})')
    axs[0, i+1].text(0.5, -0.2, f'Runtime: {power_law_runtime:.6f} sec', ha='center', transform=axs[0, i+1].transAxes)
    
    # Display histogram for power-law transformation
    axs[1, i+1].hist(power_law_transformed.flatten(), bins=256, range=[0,256], color='gray', alpha=0.7)
    axs[1, i+1].set_title(f'Hist. (gamma={gamma})')

# Hide axes
for ax in axs.flatten():
    ax.axis('off')

# Adjust layout
plt.tight_layout()
plt.show()

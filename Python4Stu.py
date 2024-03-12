import pandas as pd 
import numpy as np
import cv2
import matplotlib.pylab as plt


# Load the original color image
img_cv2 = cv2.imread('messi5.jpg')

# Convert the image to 8-bit (256 levels per channel)
original_image_8bit = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

# List to store modified images
modified_images = []

# Define the desired number of colors
desired_color_levels = [6, 3]

# Create a figure and subplots
fig, axs = plt.subplots(1, len(desired_color_levels) + 1, figsize=(12, 4))

# Display the original image
axs[0].imshow(original_image_8bit)
axs[0].set_title('Original Image')
axs[0].axis('off')

# Iterate over desired number of color levels
for i, num_levels in enumerate(desired_color_levels):
    # Quantize the image to the desired number of color levels
    quantized_image = np.uint8(np.floor_divide(original_image_8bit, 256 // (2 ** num_levels)) * (256 // (2 ** num_levels)))

    # Display the quantized image in subplot
    axs[i+1].imshow(quantized_image)
    axs[i+1].set_title(f'{2 ** num_levels} Colors')
    axs[i+1].axis('off')

plt.tight_layout()
plt.show()
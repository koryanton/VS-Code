import pandas as pd 
import numpy as np
import cv2
import matplotlib.pylab as plt

# # SAMPLING
labels = ['512x512', '256x256', '128x128', '64x64','32x32','1024x1024']
res_factor = 1

# img_mpl = plt.imread('rose.jpg')
img_cv2 = cv2.imread('rose.jpg')
# print(img_cv2.shape)

fig, axs = plt.subplots(2, 3,figsize=(10,10))
for i, ax in enumerate(axs.flat):
    res_factor = 1 if i == 5 else res_factor/2
    ax.imshow(img_cv2)
    ax.axis('off')
    ax.imshow(cv2.resize(img_cv2,None,fx=res_factor, fy=res_factor))
    ax.set_title(labels[i])
    
plt.tight_layout()
plt.savefig('roses.jpg')
# Check your folder for saved image
plt.show()

# QUANTIZATION

img_cv2 = cv2.imread('rose.jpg', cv2.IMREAD_GRAYSCALE)
gray_level = 256
fig, axs = plt.subplots(2, 4, figsize=(12, 8))
for i, ax in enumerate(axs.flat):
    new_image = (img_cv2 // gray_level) * gray_level
    ax.imshow(new_image, cmap='gray')
    ax.axis('off')
    ax.set_title('Gray Level: ' + str(int(gray_level)))
    gray_level = gray_level/2

plt.tight_layout()
plt.savefig('roses_gray.jpg')
# Check your folder for saved image
plt.show()

# COLOR QUANTIZATION

img_cv2 = cv2.imread('starry_night.jpg')
original_image_8bit = cv2.cvtColor(img_cv2 , cv2.COLOR_BGR2RGB)
modified_images = []
desired_color_levels = [6, 3]
fig, axs = plt.subplots(1, len(desired_color_levels) + 1, figsize=(12, 4))

# Original image
axs[0].imshow(original_image_8bit)
axs[0].set_title('Original Image')
axs[0].axis('off')

# Loop for desired number of color levels
for i, num_levels in enumerate(desired_color_levels):
    # Quantize the image to the desired number of color levels
    quantized_image = np.uint8(np.floor_divide(original_image_8bit, 256 // (2 ** num_levels)) * (256 // (2 ** num_levels)))

    # Display the quantized image in subplot
    axs[i+1].imshow(quantized_image)
    axs[i+1].set_title(f'{2 ** num_levels} Colors')
    axs[i+1].axis('off')


plt.tight_layout()
plt.savefig('starry_quantized.jpg')
plt.show()

# Machine Vision Project_1 code by Eric L Saldana, March 11 2024
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# 1) Implement log transformation and power law transformation using loops and matrix manipulation. 
# Compare their run time. You may use the image (fourierspectrum.pgm or university.png) to test the algorithms. 
# Try different gamma values to show the effect.


image = cv2.imread('university.png', cv2.IMREAD_GRAYSCALE)
gamma_values = [0.5, 1, 2]

# Log transformation
def log_transformation(image):
    start_time = time.time()
    transformed_image = np.log1p(image.astype(np.float32))
    runtime = time.time() - start_time
    return transformed_image, runtime

# Power-law transformation
def power_law_transformation(image, gamma):
    start_time = time.time()
    transformed_image = np.power(image / 255.0, gamma) * 255.0
    runtime = time.time() - start_time
    return transformed_image, runtime


fig, axs = plt.subplots(2, len(gamma_values) + 1, figsize=(15, 6))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original Image')

log_transformed, log_runtime = log_transformation(image)
axs[1, 0].imshow(log_transformed, cmap='gray')
axs[1, 0].set_title('Log Transformed')
axs[1, 0].text(0.5, -0.2, f'Runtime: {log_runtime:.6f} sec', ha='center', transform=axs[1, 0].transAxes)

# Power-law transformation with gamma values 
for i, gamma in enumerate(gamma_values):
    power_law_transformed, power_law_runtime = power_law_transformation(image, gamma)
    axs[0, i+1].imshow(power_law_transformed, cmap='gray')
    axs[0, i+1].set_title(f'Power-law (gamma={gamma})')
    axs[0, i+1].text(0.5, -0.2, f'Runtime: {power_law_runtime:.6f} sec', ha='center', transform=axs[0, i+1].transAxes)
    
    # power-law transformation histogram
    axs[1, i+1].hist(power_law_transformed.flatten(), bins=256, range=[0,256], color='gray', alpha=0.7)
    axs[1, i+1].set_title(f'Hist. (gamma={gamma})')

# Adjust layout
plt.figure(1)
plt.tight_layout()
plt.subplots_adjust(hspace = 0.4)


# 2) Apply the histogram equalization to university.png image with contrast issue. 
# Draw the histogram of the input and output images.

image = cv2.imread('university.png', cv2.IMREAD_GRAYSCALE)

# Histogram equalization & histograms
equalized_image = cv2.equalizeHist(image)
hist_input = cv2.calcHist([image], [0], None, [256], [0,256])
hist_output = cv2.calcHist([equalized_image], [0], None, [256], [0,256])

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Input Image')
axs[1, 0].plot(hist_input, color='black')
axs[1, 0].set_title('Input Histogram')

# Display output
axs[0, 1].imshow(equalized_image, cmap='gray')
axs[0, 1].set_title('Equalized Image')
axs[1, 1].plot(hist_output, color='black')
axs[1, 1].set_title('Equalized Histogram')

# Adjust layout
plt.figure(2)
plt.tight_layout()


# 3) Apply the histogram equalization to sat_map.png image using RGB and HSI color models. 
# Compare the results of applying the filter on the I component ONLY using the HSI model 
# and that on each RGB components using the RGB model. Provide the difference image for comparison.

img = cv2.imread('sat_map.png')

# Image 2 RGB & HSI
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# (I) extraction
intensity_ch = img_hsi[:, :, 2]

# Histogram equalization to (I) & replace
eq_I_ch = cv2.equalizeHist(intensity_ch)
eq_img_hsi = np.copy(img_hsi)
eq_img_hsi[:, :, 2] = eq_I_ch

# Convert back to RGB
eq_img_rgb_hsi = cv2.cvtColor(eq_img_hsi, cv2.COLOR_HSV2RGB)

#  RGB channel equalization and merge
eq_img_rgb_r = cv2.equalizeHist(img[:, :, 0])
eq_img_rgb_g = cv2.equalizeHist(img[:, :, 1])
eq_img_rgb_b = cv2.equalizeHist(img[:, :, 2])
eq_img_rgb = cv2.merge([eq_img_rgb_r, eq_img_rgb_g, eq_img_rgb_b])

# Compute difference images for comparison
diff_img_hsi = np.abs(eq_img_rgb_hsi.astype(np.float32) - img_rgb.astype(np.float32)).astype(np.uint8)
diff_image_rgb = np.abs(eq_img_rgb.astype(np.float32) - img_rgb.astype(np.float32)).astype(np.uint8)

# Plotting
titles = ['Original', 'Equalized (HSI I)', 'Difference (HSI I)',
          'Original RGB', 'Equalized (RGB)', 'Difference (RGB)']
values = [img_rgb, eq_img_rgb_hsi, diff_img_hsi, img_rgb, eq_img_rgb, diff_image_rgb ]
plt.figure(figsize=(10, 6))


for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(values[i])
    plt.title(titles[i])
    plt.axis('off')
    
plt.figure(3)
plt.tight_layout()
plt.subplots_adjust(bottom = 0.02)


# 4) Remove the noise in the noisy_atrium.png image by using the average filters in spatial domain. 
# Test your algorithm with the 3x3 to 5x5 and 7x7 filter sizes. Compare your results.

img = cv2.imread('noisy_atrium.png', cv2.IMREAD_GRAYSCALE)

# Average filter
filtered_images_avg = []
kernel_sizes = [3, 5, 7]

for kernel_size in kernel_sizes:
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)
    filtered_image_avg = cv2.filter2D(img, -1, kernel)
    filtered_images_avg.append(filtered_image_avg)

# Remove the noise in the noisy_atrium.png image by using the median filters in spatial domain. 
# Test your algorithm with the 3x3 to 5x5 and 7x7 filter sizes. Compare your results with the average
# and median filters results.

# Median filter 
filtered_images_median = []

for kernel_size in kernel_sizes:
    filtered_image_median = cv2.medianBlur(img, kernel_size)
    filtered_images_median.append(filtered_image_median)

# Plotting  
plt.figure(figsize=(10,8))

for i, filtered_image_avg in enumerate(filtered_images_avg, start=1):
    plt.subplot(len(filtered_images_avg), 2, i*2-1)
    plt.imshow(filtered_image_avg, cmap='gray')
    plt.title(f'Average filter\n({kernel_sizes[i-1]}x{kernel_sizes[i-1]})')
    plt.axis('off')

for i, filtered_image_median in enumerate(filtered_images_median, start=1):
    plt.subplot(len(filtered_images_median), 2, i*2)
    plt.imshow(filtered_image_median, cmap='gray')
    plt.title(f'Median filter \n({kernel_sizes[i-1]}x{kernel_sizes[i-1]})')
    plt.axis('off')

plt.figure(4)
plt.tight_layout()
plt.show()



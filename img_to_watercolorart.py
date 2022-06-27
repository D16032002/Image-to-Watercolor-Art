import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading the image
image = cv2.imread('Dog.jpg')
plt.figure(figsize=[10,10])
plt.title("Image")
plt.axis('off')
plt.imshow(image[:,:,::-1])
plt.show()

#Resizing the image
image_resized = cv2.resize(image, None, fx=0.5, fy=0.5)

#Removing the Impurities
image_cleared = cv2.medianBlur(image_resized, 3)
image_cleared = cv2.medianBlur(image_resized, 3)
image_cleared = cv2.medianBlur(image_resized, 3)

#Edge Preserving Filtering to maintain constant color spread across the image
image_cleared = cv2.edgePreservingFilter(image_resized, sigma_s=5)

#Bilateral Image Filtering using Gaussian kernel to focue more on the intense pictures and preserve corners
image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

for i in range(2):
    image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

for i in range(3):
    image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)

#Tuning the art- Sharpening the image
gaussian_mask = cv2.GaussianBlur(image_filtered, (7,7), 2)
image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)

#Displaying the image
plt.figure(figsize=[30,30])

plt.subplot(131)
plt.imshow(image[:,:,::-1])
plt.title("Original Image")
plt.axis('off')

plt.subplot(132)
plt.imshow(image_cleared[:,:,::-1])
plt.title("Clear Impurities")
plt.axis('off')

plt.subplot(133)
plt.imshow(image_sharp[:,:,::-1])
plt.title("Final Image")
plt.axis('off')

plt.show()






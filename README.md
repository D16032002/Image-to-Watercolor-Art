# Image-to-Watercolor-Art
This program uses Computer Vision to convert an image to its watercolor art form.

Required Libraries:
opencv-python == 4.5.3.56
numpy == 1.21.1
matplotlib == 3.4.2

Step 1: Reading and resizing the image

Step 2: Removing the impurities using median blur (thrice) and edge preserving filters.

Step 3: Bilateral Image Filtering with the Gaussian kernel of the image which will focus on the more intense picture and preserve the corners as well.

Step 4: Sharpening the image to remove the blur introduced due to Bilateral Image filtering and get a clearer output.

Step 5: Displaying the original, filtered (or cleared) and output images.

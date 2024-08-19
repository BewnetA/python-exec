
# Import the necessary packages
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

#Load the image and show it
image = cv2.imread("beach.png")
cv2_imshow(image)

# Masking allows us to focus only on parts of an image that interest us.
# A mask is the same size as our image, but has only two pixel values, 0 and 255.
# Pixels with a value of 0 are ignored in the orignal image,
# and mask pixels with a value of 255 are allowed to be kept.
# For example, let's construct a mask with a 150x150 square at the center of it
# and mask our image.
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)
cv2_imshow(mask)

# Apply out mask -- notice how only the center rectangular
# region of the pill is shown
masked = cv2.bitwise_and(image, image, mask = mask)
cv2_imshow(masked)

# Now, let's make a circular mask in the middle with a radius of 100 pixels
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2_imshow(image)
cv2_imshow(mask)
cv2_imshow(masked)
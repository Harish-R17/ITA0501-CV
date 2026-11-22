
import cv2
import numpy as np

img = cv2.imread('input1.jpg', 0)

# Convert image to binary
_, binary = cv2.threshold(
    img, 127, 255, cv2.THRESH_BINARY
)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(
    binary, kernel, iterations=1
)

cv2.imshow('Original Image', binary)
cv2.imshow('Erosion Image', erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

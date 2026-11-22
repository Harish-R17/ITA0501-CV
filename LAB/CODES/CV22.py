
import cv2
import numpy as np

img = cv2.imread('input.jpg', 0)

if img is None:
    print("Image not found!")
    exit()

_, binary = cv2.threshold(
    img, 127, 255, cv2.THRESH_BINARY
)

kernel = np.ones((5, 5), np.uint8)

closing = cv2.morphologyEx(
    binary, cv2.MORPH_CLOSE, kernel
)

cv2.imshow('Original Image', binary)
cv2.imshow('Closing Image', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

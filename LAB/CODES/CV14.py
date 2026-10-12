
import cv2
import numpy as np

img = cv2.imread('input.jpg')

rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([
    [100, 100],
    [400, 100],
    [100, 400],
    [400, 400]
])

# Destination points
pts2 = np.float32([
    [50, 50],
    [350, 50],
    [50, 350],
    [350, 350]
])

matrix = cv2.getPerspectiveTransform(
    pts1, pts2
)

result = cv2.warpPerspective(
    img, matrix, (cols, rows)
)

cv2.imshow('Original Image', img)
cv2.imshow('Perspective Transformation', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

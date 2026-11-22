
import cv2

# Read the image
img = cv2.imread('input1.jpg')

if img is None:
    print("Image not found!")
    exit()

# Get image dimensions
H, W = img.shape[:2]

# Select ROI size based on image dimensions
w = min(200, W // 2)
h = min(200, H // 2)

# Crop ROI from the top-left area
x, y = 0, 0
roi = img[y:y+h, x:x+w]

# Copy original image
result = img.copy()

# Calculate destination position (bottom-right corner)
dest_x = W - w
dest_y = H - h

# Paste ROI into destination
result[dest_y:dest_y+h, dest_x:dest_x+w] = roi.copy()

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Cropped ROI', roi)
cv2.imshow('Copied and Pasted Image', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

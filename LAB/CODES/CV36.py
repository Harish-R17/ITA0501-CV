
import cv2
import numpy as np

def background_subtraction(image_path):

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define background color range
    lower = np.array([0, 0, 180])
    upper = np.array([180, 50, 255])

    # Create background mask
    mask = cv2.inRange(hsv, lower, upper)

    # Remove background
    result = cv2.bitwise_and(
        img, img, mask=cv2.bitwise_not(mask)
    )

    cv2.imshow('Original Image', img)
    cv2.imshow('Background Mask', mask)
    cv2.imshow('Background Removed', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

background_subtraction('input.jpg')

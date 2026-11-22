
import cv2
import numpy as np

def foreground_subtraction(image_path):

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define foreground color range
    lower = np.array([0, 100, 100])
    upper = np.array([10, 255, 255])

    # Create foreground mask
    mask = cv2.inRange(hsv, lower, upper)

    # Remove foreground
    result = cv2.bitwise_and(
        img, img, mask=cv2.bitwise_not(mask)
    )

    cv2.imshow('Original Image', img)
    cv2.imshow('Foreground Mask', mask)
    cv2.imshow('Foreground Subtracted', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

foreground_subtraction('input.jpg')


import cv2
import numpy as np

def create_colored_boxes(height, width):

    img = np.ones(
        (height, width, 3), dtype=np.uint8
    ) * 255

    box_h = height // 10
    box_w = width // 10

    # Top-left: Black
    img[0:box_h, 0:box_w] = (0, 0, 0)

    # Top-right: Blue
    img[0:box_h, width-box_w:width] = (255, 0, 0)

    # Bottom-left: Green
    img[height-box_h:height, 0:box_w] = (0, 255, 0)

    # Bottom-right: Red
    img[height-box_h:height,
        width-box_w:width] = (0, 0, 255)

    cv2.imshow('Colored Boxes', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

h = int(input("Enter image height: "))
w = int(input("Enter image width: "))

create_colored_boxes(h, w)

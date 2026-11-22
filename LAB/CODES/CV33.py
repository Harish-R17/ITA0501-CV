
import cv2
import numpy as np

def create_rectangle(height, width):

    img = np.ones(
        (height, width, 3), dtype=np.uint8
    ) * 255

    cv2.rectangle(
        img,
        (width//4, height//4),
        (3*width//4, 3*height//4),
        (0, 0, 255),
        3
    )

    cv2.imshow('Rectangle Image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

h = int(input("Enter image height: "))
w = int(input("Enter image width: "))

create_rectangle(h, w)

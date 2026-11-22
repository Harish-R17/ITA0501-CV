
import cv2

def add_text(image_path, text):

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    cv2.putText(
        img,
        text,
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow('Image with Text', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

text = input("Enter text: ")

add_text('input.jpg', text)

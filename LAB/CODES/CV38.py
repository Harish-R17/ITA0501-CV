
import cv2

def count_faces(image_path):

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(
        img, cv2.COLOR_BGR2GRAY
    )

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        'haarcascade_frontalface_default.xml'
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    count = len(faces)

    for (x, y, w, h) in faces:

        cv2.rectangle(
            img, (x, y), (x+w, y+h),
            (0, 255, 0), 2
        )

    print("Total Number of Faces:", count)

    cv2.putText(
        img,
        "Faces: " + str(count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow('Face Counting', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

count_faces('input1.jpg')

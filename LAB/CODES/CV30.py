
import cv2

img = cv2.imread('input1.jpg')

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY
)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_smile.xml'
)

faces = face_cascade.detectMultiScale(
    gray, 1.1, 5
)

for (x, y, w, h) in faces:

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 15)
    )

    for (sx, sy, sw, sh) in smiles:

        cv2.rectangle(
            roi_color,
            (sx, sy),
            (sx+sw, sy+sh),
            (0, 255, 0), 2
        )

        cv2.putText(
            roi_color,
            'Smile',
            (sx, sy-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (0, 255, 0), 2
        )

cv2.imshow('Smile Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

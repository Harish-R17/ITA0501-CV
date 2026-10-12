
import cv2
import time

cap = cv2.VideoCapture('video.mp4')

if not cap.isOpened():
    print("Video not found!")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

print("Original FPS:", fps)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Normal Video', frame)
    if cv2.waitKey(max(1, int(1000/fps))) & 0xFF == ord('q'):
        break

    cv2.imshow('Slow Motion', frame)
    if cv2.waitKey(max(1, int(3000/fps))) & 0xFF == ord('q'):
        break

    cv2.imshow('Fast Motion', frame)
    if cv2.waitKey(max(1, int(250/fps))) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

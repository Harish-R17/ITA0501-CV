
import cv2

# Load YOLO model
net = cv2.dnn.readNetFromDarknet(
    'yolov3.cfg',
    'yolov3.weights'
)

with open('coco.names', 'r') as f:
    classes = f.read().strip().split('\n')

# Vehicle classes
vehicle_classes = ['car', 'motorcycle', 'bus', 'truck']

cap = cv2.VideoCapture('input2.mp4')

if not cap.isOpened():
    print("Video not found!")
    exit()

layer_names = net.getUnconnectedOutLayersNames()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    height, width = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frame, 1/255.0, (416, 416),
        swapRB=True, crop=False
    )

    net.setInput(blob)
    outputs = net.forward(layer_names)

    boxes = []
    confidences = []
    labels = []

    for output in outputs:
        for detection in output:

            scores = detection[5:]
            class_id = scores.argmax()
            confidence = scores[class_id]

            if (classes[class_id] in vehicle_classes
                    and confidence > 0.5):

                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                labels.append(classes[class_id])

    indices = cv2.dnn.NMSBoxes(
        boxes, confidences, 0.5, 0.4
    )

    if len(indices) > 0:
        for i in indices.flatten():

            x, y, w, h = boxes[i]

            cv2.rectangle(
                frame, (x, y), (x+w, y+h),
                (0, 255, 0), 2
            )

            cv2.putText(
                frame, labels[i],
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2
            )

    cv2.imshow('Vehicle Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

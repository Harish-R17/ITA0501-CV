
import cv2

# Load YOLOv3 model
net = cv2.dnn.readNetFromDarknet(
    r"C:\Users\bssre\Downloads\yolov3.cfg",
    r"C:\Users\bssre\Downloads\yolov3.weights"
)

# Load COCO class names
with open(r"C:\Users\bssre\Downloads\coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Read input image
img = cv2.imread("input1.jpg")

if img is None:
    print("Image not found!")
    exit()

# Get image dimensions
height, width = img.shape[:2]

# Convert image into blob
blob = cv2.dnn.blobFromImage(
    img, 1/255.0, (416, 416),
    swapRB=True, crop=False
)

net.setInput(blob)

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [
    layer_names[i - 1]
    for i in net.getUnconnectedOutLayers().flatten()
]

# Perform object detection
outputs = net.forward(output_layers)

boxes = []
confidences = []
class_ids = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = scores.argmax()
        confidence = scores[class_id]

        # Detect watch (COCO class ID  watch =  78)
        if classes[class_id] == "clock" and confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Remove duplicate boxes
indexes = cv2.dnn.NMSBoxes(
    boxes, confidences, 0.5, 0.4
)

# Draw detection boxes
if len(indexes) > 0:
    for i in indexes.flatten():
        x, y, w, h = boxes[i]

        cv2.rectangle(
            img, (x, y), (x + w, y + h),
            (0, 255, 0), 2
        )

        cv2.putText(
            img, "Clock",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 255, 0), 2
        )

    print("Clock detected!")
else:
    print("No clock detected!")

# Display output
cv2.imshow("YOLOv3 Object Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

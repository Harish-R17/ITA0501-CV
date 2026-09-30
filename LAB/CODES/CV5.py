import cv2
import matplotlib.pyplot as plt
def analyze_histogram(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    colors = ("b", "g", "r")
    channel_names = ("Blue", "Green", "Red")
    plt.figure(figsize=(10, 5))
    for i, (color, name) in enumerate(zip(colors, channel_names)):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=name)
    plt.title("Color Histogram")
    plt.xlabel("Color Intensity Level (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()
analyze_histogram("input.jpg")

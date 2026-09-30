import cv2
image = cv2.imread("input.jpg")
if image is None:
    print("Error: Could not read the image.")
else:
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)
    cv2.imwrite("blurred.jpg", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

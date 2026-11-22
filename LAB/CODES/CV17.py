
import cv2

img = cv2.imread('input.jpg')

if img is None:
    print("Image not found!")
    exit()

watermarked = img.copy()

# Add watermark text
cv2.putText(
    watermarked,
    'MY WATERMARK',
    (50, img.shape[0] - 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# Blend original and watermark
result = cv2.addWeighted(
    img, 0.7, watermarked, 0.3, 0
)

cv2.imshow('Original Image', img)
cv2.imshow('Watermarked Image', result)

cv2.imwrite('watermarked.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

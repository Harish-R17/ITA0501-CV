
import cv2
import easyocr

def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video not found!")
        return

    # Initialize OCR reader
    reader = easyocr.Reader(['en'])

    extracted_text = set()
    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Process every 30th frame
        if frame_count % 30 == 0:

            gray = cv2.cvtColor(
                frame, cv2.COLOR_BGR2GRAY
            )

            results = reader.readtext(gray)

            for result in results:

                text = result[1]

                extracted_text.add(text)

                print("Extracted Text:", text)

            cv2.imshow('Video Text Extraction', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

    # Save extracted text
    with open('extracted_text.txt', 'w') as file:

        for text in sorted(extracted_text):
            file.write(text + '\n')

    print("Text extraction completed!")
    print("Saved in extracted_text.txt")

extract_text_from_video('video.mp4')

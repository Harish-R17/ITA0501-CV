
import cv2

def reverse_video(input_file, output_file):

    cap = cv2.VideoCapture(input_file)

    if not cap.isOpened():
        print("Video not found!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if not frames:
        print("No frames found!")
        return

    writer = cv2.VideoWriter(
        output_file,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps if fps > 0 else 25,
        (width, height)
    )

    for frame in reversed(frames):
        writer.write(frame)

    writer.release()

    print("Reverse video created successfully!")

reverse_video('video.mp4', 'reverse_video.mp4')

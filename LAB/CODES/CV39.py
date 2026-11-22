
import cv2

def reverse_slow_motion(input_file, output_file):

    cap = cv2.VideoCapture(input_file)

    if not cap.isOpened():
        print("Video not found!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames = []

    # Read all video frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("No frames found!")
        return

    # Reduce FPS to create slow motion
    output_fps = fps / 2 if fps > 0 else 12.5

    writer = cv2.VideoWriter(
        output_file,
        cv2.VideoWriter_fourcc(*'mp4v'),
        output_fps,
        (width, height)
    )

    # Write frames in reverse order
    for frame in reversed(frames):

        writer.write(frame)

        cv2.imshow('Reverse Slow Motion', frame)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    writer.release()
    cv2.destroyAllWindows()

    print("Reverse slow-motion video created successfully!")

reverse_slow_motion(
    'input2.mp4',
    'reverse_slow_motion.mp4'
)

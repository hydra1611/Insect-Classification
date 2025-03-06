import cv2

def live_video_stream(camera_index=0):
    """
    Continuously captures and displays video from the USB webcam.

    Parameters:
    - camera_index (int): Index of the camera (0 for default USB webcam).
    """
    cap = cv2.VideoCapture(camera_index)  # Open webcam
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()  # Read frame
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Live Video Feed", frame)  # Display frame

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release camera
    cv2.destroyAllWindows()  # Close window

# Example usage:
live_video_stream()

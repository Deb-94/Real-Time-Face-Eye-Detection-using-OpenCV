import cv2
import time

def main():
    # 1. Load pre-trained Haar Cascade models for face and eye detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
    )

    # 2. Start webcam (0 = default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit, 's' to save screenshot.")

    while True:
        # 3. Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # 4. Convert to grayscale (Haar cascades work on grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 5. Detect faces in the frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        # 6. For each detected face, draw rectangle and detect eyes
        for (x, y, w, h) in faces:
            # Draw rectangle around face (blue)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Region of interest (ROI) for eyes inside the face
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Detect eyes in the face region
            eyes = eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=3
            )

            # Draw rectangles around eyes (green)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(
                    roi_color,
                    (ex, ey),
                    (ex + ew, ey + eh),
                    (0, 255, 0),
                    2
                )

        # 7. Show face count on the frame
        text = f"Faces detected: {len(faces)}"
        cv2.putText(
            frame,
            text,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        # 8. Display the frame
        cv2.imshow("Face & Eye Detection", frame)

        # 9. Handle key events
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            # Quit the loop
            break
        elif key == ord('s'):
            # Save screenshot with timestamp
            filename = f"screenshot_{int(time.time())}.png"
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")

    # 10. Release camera and close window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

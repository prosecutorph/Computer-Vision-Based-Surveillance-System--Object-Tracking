import cv2

# Set up the camera
camera = cv2.VideoCapture(0)

# Capture and display the frames from the camera
while True:
    # Capture the frame
    _, frame = camera.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply motion detection
    motion = cv2.GaussianBlur(gray, (21, 21), 0)
    motion = cv2.absdiff(gray, motion)
    motion = cv2.threshold(motion, 25, 255, cv2.THRESH_BINARY)[1]

    # Find contours in the motion map
    contours, _ = cv2.findContours(motion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a rectangle around the contours
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Camera", frame)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to quit
        break

# Clean up
camera.release()
cv2.destroyAllWindows()

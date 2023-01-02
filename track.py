import pymotion as pm
import cv2

# Set up the camera
camera = cv2.VideoCapture(0)

# Create an OpenCV background subtractor
subtractor = cv2.createBackgroundSubtractorMOG2()

# Capture and display the frames from the camera
while True:
    # Capture the frame
    _, frame = camera.read()

    # Apply the background subtractor to the frame
    mask = subtractor.apply(frame)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        # Draw a rectangle around the contour
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

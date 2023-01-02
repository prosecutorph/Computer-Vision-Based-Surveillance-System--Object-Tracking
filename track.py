import cv2
import numpy as np

# Set up the camera
camera = cv2.VideoCapture(0)

# Capture the first frame
_, frame = camera.read()
prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Set up the feature points
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
features = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(frame)

# Define the parameters for the Lucas-Kanade optical flow algorithm
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Capture and display the frames from the camera
while True:
    # Capture the frame
    _, frame = camera.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the optical flow
    new_features, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, gray, features, None, **lk_params)

    # Select the good points
    good_features = features[np.expand_dims(status, axis=1) == 1]
    new_features = new_features[np.expand_dims(status, axis=1) == 1]


    # Draw the tracks
    for i, (new, old) in enumerate(zip(new_features, good_features)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
        frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)

    # Display the frame
    cv2.imshow("Camera", frame)

    # Update the previous frame and the feature points
    prev_gray = gray
    features = new_features

    # Check if the 'q' key has been pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the camera and destroy the windows
camera.release()
cv2.destroyAllWindows()

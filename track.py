import cv2
import datetime

# Set up the camera
camera = cv2.VideoCapture(0)

# Get the width and height of the frame
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# fourcc = cv2.VideoWriter_fourcc(*'H263')

# Make the File Size Smaller compare to MJPG
fourcc = cv2.VideoWriter_fourcc(*'mp4v')


# Get the current date and time
now = datetime.datetime.now()

# Create the file name using the current date and time
filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".avi"
out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

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

        # Add text on top of the rectangle
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Human"
        text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
        text_x = x + 10
        text_y = y - text_size[1] - 10
        cv2.putText(frame, text, (text_x, text_y), font, 0.5, (0, 255, 0), 1)

    # Add the date and time stamp in the upper left side of the frame
    date_time = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(date_time, font, 0.5, 1)[0]
    text_x = 10
    text_y = text_size[1] + 10
    cv2.putText(frame, date_time, (text_x, text_y), font, 0.5, (255, 255, 255), 1)
    
    # Write the frame to the output video file
    out.write(frame)

    # Display the frame
    cv2.imshow("Camera", frame)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to stop recording and quit
        break

# Clean up
out.release()
camera.release()
cv2.destroyAllWindows()

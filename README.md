# Computer-Vision-Based-Surveillance-System--Object-Tracking
This code captures video frames from a camera, applies a background subtraction algorithm to the frames, finds contours in the resulting mask, and draws a rectangle and text label around the largest contour. The loop continues indefinitely until the user presses the 'ESC' key, at which point the camera is released and all windows are closed.

The background subtractor is created using the cv2.createBackgroundSubtractorMOG2() function. MOG2 stands for "Mixture of Gaussians 2" and is a type of background subtraction algorithm that models the background of the scene as a mixture of several Gaussians. It is able to adapt to changing lighting conditions and can handle some level of foreground occlusion.

The cv2.findContours() function is used to find contours in the mask. The cv2.RETR_EXTERNAL flag retrieves only the external contours, and the cv2.CHAIN_APPROX_SIMPLE flag compresses horizontal, diagonal, and vertical segments, which can help speed up the contour processing.

The largest contour is found using the max() function with the cv2.contourArea() function as the key. The bounding rectangle of the contour is then calculated using cv2.boundingRect(). The rectangle and text label are drawn on the original frame using cv2.rectangle() and cv2.putText().

Finally, the frame is displayed using cv2.imshow(), and the user input is checked using cv2.waitKey(). If the user presses the 'ESC' key (ASCII value 27), the loop breaks and the program cleans up by releasing the camera and destroying all windows.

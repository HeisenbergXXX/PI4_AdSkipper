import cv2
import numpy as np
import os
import subprocess

# Set up LIRC
lirc_cmd = 'irsend SEND_ONCE Sam KEY_OK'
lirc_delay = 0.5  # delay in seconds between sending LIRC signals

# Load reference image "D:\Bennett\Documents\PI_IR_project\pcRef.png"
ref_image = cv2.imread('pcRef.png')
print('Loaded reference image: pcRef.png')

# Initialize video capture
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
print('Video capture Initialized.')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print('Resolution set to: 640x480.')

# Define image matching method
method = cv2.TM_CCOEFF_NORMED

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    if not ret or frame is None:
        # Handle the case where the capture failed or returned an empty frame
        continue

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Match template with reference image
    result = cv2.matchTemplate(gray, ref_image, method)

    # Get maximum correlation coefficient
    max_val = np.max(result)

    # If the maximum correlation coefficient is greater than 0.9, we have a match
    if max_val > 0.9:
        print('Match found: ' + str(max_val))
        # Send LIRC signal
        subprocess.call(lirc_cmd, shell=True)
        print('Sent LIRC signal: KEY_OK')
        # Wait for a short time to avoid spamming LIRC signals
        time.sleep(lirc_delay)

    # Display the frame
    cv2.imshow('frame', frame)

    # Quit if user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()

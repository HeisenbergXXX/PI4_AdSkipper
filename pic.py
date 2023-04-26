import cv2

# Open the default camera
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video capture")

# Read a frame from the camera
ret, frame = cap.read()

# Check if frame read successfully
if not ret:
    print("Error reading frame")

# Save the frame as an image file
cv2.imwrite("image.jpg", frame)

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

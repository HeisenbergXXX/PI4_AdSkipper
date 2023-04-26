import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
print('Video capture Initialized.')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print('Resolution set to: 640x480.')

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640, 480))
    if not ret:
        print("Error reading video stream")
        break
    else:
        print('Frame read successfully')
        cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

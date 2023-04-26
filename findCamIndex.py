import cv2

for i in range(50):
    cap = cv2.VideoCapture(i, cv2.CAP_V4L2)
    print(f"Trying camera index {i}.")
    if not cap.read()[0]:
        continue
    cap.release()
    print(f"Camera index {i} is available.")


#cmake /home/bennett/opencv -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local

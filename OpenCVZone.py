pip install opencv-python
import cv2
cap=cv2.VideoCapture(0)
while True:
    status , photo = cap.read()
    cv2.imshow("Jatin video",photo)
    if cv2.waitKey(50) == 13:
        break

cv2.destroyAllWindows()
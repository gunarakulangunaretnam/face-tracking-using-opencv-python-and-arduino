import cv2
import numpy as np
import time
from cvzone.FaceDetectionModule import FaceDetector

videoCam = cv2.VideoCapture(3)

detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)

    fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
    print(fx)
    print(fy)
    















videoCam.release()
cv2.destroyAllWindows()
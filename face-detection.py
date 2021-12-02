import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(3)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img) #draw=False will not draw the bounding box
        
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

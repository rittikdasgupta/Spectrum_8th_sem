import cv2
import numpy as np


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
detector = cv2.FaceDetectorYN.create("face_detection_yunet_2022mar.onnx", "", (320, 320))

pedestrian_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

names = ['None', 'Rittik'] 

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)


minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    _, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Get image shape
    img_W = int(img.shape[1])
    img_H = int(img.shape[0])
    # Set input size
    detector.setInputSize((img_W, img_H))

    # Getting detections
    detections = detector.detect(img)

    pedestrians = pedestrian_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    if (detections[1] is not None) and (len(detections[1]) > 0):
        for detection in detections[1]:
            # Converting predicted and ground truth bounding boxes to required format
            pred_bbox = detection
            pred_bbox = [int(i) for i in pred_bbox[:4]]
            # print(pred_bbox)
            cv2.rectangle(img,pred_bbox,(0,255,0),5)

            id, confidence = recognizer.predict(gray[pred_bbox[0]:pred_bbox[0] + pred_bbox[3],pred_bbox[1]:pred_bbox[1] + pred_bbox[2]])
            # print(confidence)
            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (pred_bbox[0],pred_bbox[1]), font, 1, (255,255,255), 2)
            # cv2.putText(img, str(confidence), (pred_bbox[0] + 100,pred_bbox[1]), font, 1, (255,255,0), 1)  
   
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break


print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
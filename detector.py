import cv2
# Initialize detector
detector = cv2.FaceDetectorYN.create("face_detection_yunet_2022mar.onnx", "", (320, 320))

face_id = input('\n enter user id end press <return> ==>  ')

cap = cv2.VideoCapture(0)

count = 0

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Get image shape
    img_W = int(img.shape[1])
    img_H = int(img.shape[0])
    # Set input size
    detector.setInputSize((img_W, img_H))
    # Getting detections
    detections = detector.detect(img)

    if (detections[1] is not None) and (len(detections[1]) > 0):
        for detection in detections[1]:
            # Converting predicted and ground truth bounding boxes to required format
            pred_bbox = detection
            pred_bbox = [int(i) for i in pred_bbox[:4]]
            print(pred_bbox)

            cv2.rectangle(img,pred_bbox,(0,255,0),5)

            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[pred_bbox[0]:pred_bbox[0] + pred_bbox[3],pred_bbox[1]:pred_bbox[1] + pred_bbox[2]])

            count += 1
            cv2.imshow('image', img)

            if count >= 300: break

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
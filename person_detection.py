from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


while True:
    _, image = cam.read()

    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)
	# draw the original bounding boxes
	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
	# draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
	# show some information on the number of bounding boxes
	# show the output images
	# cv2.imshow("Before NMS", orig)
    cv2.imshow("After NMS", image)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
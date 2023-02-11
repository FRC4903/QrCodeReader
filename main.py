import glob
import cv2 as cv
# import pandas as pd
import pathlib
import csv
import os

lastValue = ""

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    
    exit()

while True:

    ret, frame = cap.read()
    detect = cv.QRCodeDetector()
    value, points, stright_qr=detect.detectAndDecode(frame)

    if(len(value) > 0 and lastValue != value):
        print(value)
        lastValue = value
        Vl = value.split(",")

        if(os.path.exists(f"Teams\\{Vl[0]}.csv")):
            with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                w = csv.writer(f)
                w.writerow(Vl[1:])
        else:
            open(f"Teams\\{Vl[0]}.csv", "a").close()
            with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                w = csv.writer(f)
                w.writerow(["field 1", "field 2", "field 3", "field 4", "field 5"])
                w.writerow(Vl[1:])

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame=cv.flip(frame, 1)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

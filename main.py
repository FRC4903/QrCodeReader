import glob
import cv2 as cv
import pathlib
import csv
import os

lastValue = ""

#Starts the video capture
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    
    exit()

while True:

    ret, frame = cap.read()
    detect = cv.QRCodeDetector()
    value, points, stright_qr=detect.detectAndDecode(frame)
    value = value.replace("false", "No")
    value = value.replace("true", "Yes")
    if(len(value) > 0 and lastValue != value):
        lastValue = value

        print(value)
        Vl = value.split(",")

        if(os.path.exists(f"Teams\\{Vl[0]}.csv")):
            with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                w = csv.writer(f)
                w.writerow(Vl[1:])
        else:
            open(f"Teams\\{Vl[0]}.csv", "a").close()
            with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                w = csv.writer(f)
                w.writerow(["Match Number", "Scouter", "extra cones", "extra cubes", "taxi", "balance attempt", "preloaded cone", "preload cube", "scored preload", "cone upper", "cone mid", "cone lower", "cube upper", "cube mid", "cube lower", "links", "game pieces picked up", "defence", "time to climb", "climb attempts", "climb successful", "auto notes", "teleop notes", "endgame notes" ])
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

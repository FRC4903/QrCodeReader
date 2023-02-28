import glob
import cv2 as cv
import pathlib
import csv
import os

lastValue = ""
values =[""]

if(not (os.path.exists("Teams"))):
    os.mkdir("Teams")

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

        Vl = value.split("~~~")
        values = Vl
        print(f"Team {Vl[0]} match {Vl[1]} has been scanned")

        if(os.path.exists(f"Teams\\{Vl[0]}.csv")):
            with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                w = csv.writer(f)
                w.writerow(Vl)
        else:
            open(f"Teams\\{Vl[0]}.csv", "a").close()
            with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                w = csv.writer(f)
                w.writerow(["Team Number","Match Number", "Scouter", "extra cones",
                            "extra cubes", "Start Positon", "Taxi", "Balance Attempt", "Preloaded Cone",
                            "Preload Cube", "Scored Preload", "Docked Auto", "Engaged Auto", "Upper Cone", "Mid Cone",
                            "Lower Cone", "Upper Cube", "Mid cube", "Lower Cube", "Links",
                            "Picked Up", "Capable to Pick Up From Station", "Capable to Pick Up From Floor","Can go over bump", "Did Defend", "Was Defended", "Time", "Docking attempts",
                            "Endgame Docked", "Endgame Engaged", "Parked", "Auto Notes", "Teleop Notes", "Endgame Notes", "Won", "RP" ])
                w.writerow(Vl)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    font = cv.FONT_HERSHEY_COMPLEX_SMALL
    fontScale = 1.25
    color = (50,255,50)
    thickness = 1
    frame=cv.flip(frame, 1)
    cv.putText(frame, f"scanned", (25,25), font, fontScale, color, thickness, cv.LINE_AA)
    cv.putText(frame, f"{values[0]}", (25,50), font, fontScale, color, thickness, cv.LINE_AA)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

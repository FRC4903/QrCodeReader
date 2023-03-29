import glob
import cv2 as cv
import pathlib
import csv
import os

lastValue = ""
values =[""]
text = ""


if(not (os.path.exists("Teams"))):
    os.mkdir("Teams")

if(not (os.path.exists("Teams\\PitScouting"))):
    os.mkdir("Teams\\PitScouting")
if(not (os.path.exists("Teams\\PitScouting\\PitScouting.csv"))):
    open(f"Teams\\PitScouting\\PitScouting.csv", "a").close()
    with open(f"Teams\\PitScouting\\PitScouting.csv", "a", encoding='UTF8') as f:
        w = csv.writer(f)
        w.writerow(["Team Number", "weight", "length", "Swerve", "Tank", "Mecanum", "Other Name", "Other", "Comments", "Visisted", "Team Name"])        

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
        if(Vl[0] == "krishraw"):
            text=Vl[1]
            print(f"Team {Vl[1]} Pit Scouting data has been scanned")
            if(os.path.exists(f"Teams\\PitScouting\\PitScouting.csv")):
                with open(f"Teams\\PitScouting\\PitScouting.csv", "a", encoding='UTF8') as f:
                    w = csv.writer(f)
                    w.writerow(Vl[1:])
        else:
            text=Vl[0]
            print(f"Team {Vl[0]} match {Vl[1]} has been scanned")

            if(os.path.exists(f"Teams\\{Vl[0]}.csv")):
                with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                    w = csv.writer(f)
                    w.writerow(Vl[1:])
            else:
                open(f"Teams\\{Vl[0]}.csv", "a").close()
                with open(f"Teams\\{Vl[0]}.csv", "a", encoding='UTF8') as f:
                    w = csv.writer(f)
                    w.writerow(["Team Number","Match Number", "Scouter", "extra cones",
                                "extra cubes", "Start Positon", "Taxi", "Balance Attempt", "Preloaded Cone",
                                "Preload Cube", "Scored Preload", "Docked Auto", "Engaged Auto", "Upper Cone", "Mid Cone",
                                "Lower Cone", "Upper Cube", "Mid cube", "Lower Cube", "Links",
                                "Picked Up", "Capable to Pick Up From Station", "Capable to Pick Up From Floor","Can go over bump", "Stationable", "Did Defend", "Was Defended", "Not Tipsy", "Little Tipsy", "Very Tipsy", "Time", "# of Robot's Docked", "Docking attempts",
                                "Endgame Docked", "Endgame Engaged", "Parked", "Auto Notes", "Teleop Notes", "Endgame Notes", "Won", "RP" ])
                    w.writerow(Vl)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1.25
    color = (255,255,255)
    thickness = 1
    frame=cv.flip(frame, 1)
    cv.putText(frame, f"Scanned:", (25,30), font, fontScale, (0,0,0), 3, cv.LINE_AA)
    cv.putText(frame, f"Scanned:", (25,30), font, fontScale, color, 2, cv.LINE_AA)
    cv.putText(frame, f"{text}", (25,60), font, fontScale, (0,0,0), 3, cv.LINE_AA)
    cv.putText(frame, f"{text}", (25,60), font, fontScale, color, 2, cv.LINE_AA)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

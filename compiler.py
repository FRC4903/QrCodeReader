import glob
import cv2 as cv
import pathlib
import csv
import os
count = 0
total=0
mNumber = input("Enter Match Number: ")
team1 = input("Input Team 1: ")
team2 = input("Input Team 2: ")
team3 = input("Input Team 3: ")
team4 = input("Input Team 4: ")
team5 = input("Input Team 5: ")
teamlist = [team1,team2,team3,team4,team5]
Teams={
    f"{team1}":
    {
        f"ECubes": 0, 
        f"ECones": 0,
        f"UpperCone": 0,
        f"Mid Cone": 0,
        f"Lower Cone": 0,
        f"Upper Cube": 0,
        f"Mid Cube": 0,
        f"Lower Cube": 0,
        f"Tele-op opr": 0,
        f"Auto opr": 0,
        f"Robots Balanced": 0,
    },
       f"{team2}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0,f"Upper Cube": 0,
        f"Mid Cube": 0,
        f"Lower Cube": 0,
        f"Tele-op opr": 0,
        f"Auto opr": 0,
        f"Robots Balanced": 0,},
       f"{team3}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0,f"Upper Cube": 0,
        f"Mid Cube": 0,
        f"Lower Cube": 0,
        f"Tele-op opr": 0,
        f"Auto opr": 0,
        f"Robots Balanced": 0,},
       f"{team4}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0,f"Upper Cube": 0,
        f"Mid Cube": 0,
        f"Lower Cube": 0,
        f"Tele-op opr": 0,
        f"Auto opr": 0,
        f"Robots Balanced": 0,},
       f"{team5}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0,f"Upper Cube": 0,
        f"Mid Cube": 0,
        f"Lower Cube": 0,
        f"Tele-op opr": 0,
        f"Auto opr": 0,
        f"Robots Balanced": 0,}}

if((os.path.exists("Teams"))):
    for i in teamlist:
        count=0
        if((os.path.exists(f"Teams\\{i}.csv"))):
             with open(f"Teams\\{i}.csv", "r", encoding='UTF8') as r:
                data = list(csv.reader(r, delimiter=","))
                for row in data:
                    try:
                        count+=1
                        # print(row[3])
                        print(Teams[i]["ECubes"])
                        print(row[3])
                        Teams[i]["ECubes"] += int(row[3])
                        Teams[i]["ECones"] += int(row[4])
                        Teams[i]["UpperCone"] += int(row[13])
                        Teams[i]["Mid Cone"] += int(row[14])
                        Teams[i]["Lower Cone"] += int(row[15])
                        Teams[i]["Upper Cube"] += int(row[16])
                        Teams[i]["Mid Cube"] += int(row[17])
                        Teams[i]["Lower Cube"] += int(row[18])
                        Teams[i]["Tele-op opr"] = int((row[16] + row[14]) * 5 + (row[17] + row[15]) * 3 + (row[15] + row[18]) * 2 + (row[19]) * 5 + 6 if row[33] == "Yes" else 0 + 10 if row[34] == "Yes" and row[33] == "No" else 0 + 2 if row[35] else 0)
                        Teams[i]["Auto opr"] = int((row[3] + row[4])*4 + 8 if row[11] == "Yes" else 0 + 12 if row[12] == "Yes" and row[33] == "No" else 0 + 3 if row[6] == "Yes" else 0)
                        Teams[i]["Robots Balanced"] += int(row[31])
                    except:
                        # print("")
                        pass
                        # print(total)
                        # print(count)
                Teams[i]["ECubes"] = Teams[i]["ECubes"]/count
                Teams[i]["ECones"] = Teams[i]["ECubes"]/count
                Teams[i]["Mid Cone"] = Teams[i]["Mid Cone"]/count
                Teams[i]["UpperCone"] = Teams[i]["UpperCone"]/count
                Teams[i]["Lower Cone"] = Teams[i]["Lower Cone"]/count
                Teams[i]["Upper Cube"] = Teams[i]["Mid Cube"]/count
                Teams[i]["Mid Cube"] = Teams[i]["Mid Cube"]/count
                Teams[i]["Lower Cube"] = Teams[i]["Lower Cube"]/count
                Teams[i]["Tele-op opr"] = Teams[i]["Tele-op opr"]/count
                Teams[i]["Auto opr"] = Teams[i]["Tele-op opr"]/count
                Teams[i]["Robots Balanced"] = Teams[i]["Robots Balanced"]/count
else:          
    print("ERROR: No Teams Folder found")

print(Teams)

if(not (os.path.exists("Compile"))):
    os.mkdir("Compile")

ec="ECubes"
eco="ECones"
mc="Mid Cone"
up="UpperCone"
lc="Lower Cone"
uc = "Upper Cube"
mcu = "Mid Cube"
lcu = "Lower Cube"
Topr = "Tele-op opr"
Aopr = "Auto opr"
Rb = "Robots Balanced"

open(f"Compile\\{mNumber}.csv", "a").close()
with open(f"Compile\\{mNumber}.csv", "a", encoding='UTF8') as f:
    w = csv.writer(f)
    w.writerow(["Teams", ec,eco,mc,up,lc,uc,mcu,lcu,Topr,Aopr,Rb])
    for i in teamlist:
        w.writerow([f"{i}",f"{Teams[i][ec]}", f"{Teams[i][eco]}",f"{Teams[i][mc]}",f"{Teams[i][up]}",f"{Teams[i][lc]}",f"{Teams[i][uc]}",f"{Teams[i][mcu]}",f"{Teams[i][lcu]}",f"{Teams[i][Topr]}",f"{Teams[i][Aopr]}",f"{Teams[i][Rb]}"])

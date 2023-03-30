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
        f"Lower Cone": 0
    },
       f"{team2}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0},
       f"{team3}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0},
       f"{team4}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0},
       f"{team5}":{f"ECubes": 0, f"ECones": 0,f"UpperCone": 0,f"Mid Cone": 0,f"Lower Cone": 0}}

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
                        Teams[i]["UpperCone"] += int(row[14])
                        Teams[i]["Mid Cone"] += int(row[15])
                        Teams[i]["Lower Cone"] += int(row[15])

                 
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

open(f"Compile\\{mNumber}.csv", "a").close()
with open(f"Compile\\{mNumber}.csv", "a", encoding='UTF8') as f:
    w = csv.writer(f)
    w.writerow(["Teams", ec,eco,mc,up,lc])
    for i in teamlist:
        w.writerow([f"{i}",f"{Teams[i][ec]}", f"{Teams[i][eco]}",f"{Teams[i][mc]}",f"{Teams[i][up]}",f"{Teams[i][lc]}"])
    
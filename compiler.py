import glob
import cv2 as cv
import pathlib
import csv
import os

team1 = input("Input Team 1: ")
team2 = input("Input Team 2: ")
team3 = input("Input Team 3: ")
team4 = input("Input Team 4: ")
team5 = input("Input Team 5: ")
teamlist = [team1,team2,team3,team4,team5]
if((os.path.exists("Teams"))):
    for i in teamlist:
        if((os.path.exists(f"Teams\\{i}.csv"))):
             with open(f"Teams\\{i}.csv", "r", encoding='UTF8') as r:
                re = csv.reader(r)
                for ro in re:
                    print(ro)
else:
    print("ERROR: No Teams Folder found")
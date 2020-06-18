import csv

import json

data = {
    "madrichone": [],
    "pnt": [],
    "linan": [],
    "carryme": [],
    "navi": [],
    "zairus": [],
    "betanoob": [],
    "woo": [],
    "koolaid": [],
    "ysided": [],
    "tapegun": [],
    "iggy": [],
    "sneak": [],
    "dozer": [],
    "clouds": [],
    "poomer": [],
    "rexgunderman": [],
    "cre8": [],
    "sylo": [],
    "gamesghoul": [],
    "habibi": [],
    "mood": [],
    "v1nh": [],
}

w = csv.writer(open("output.csv", "w"))
for key, val in data.items():
    w.writerow([key, val])


json = json.dumps(data)
f = open("rankings.json","w")
f.write(json)
f.close()
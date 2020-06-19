import csv

import json

data = {
    "madrichone": [200],
    "pnt": [200],
    "linan": [200],
    "carryme": [200],
    "navi": [200],
    "zairus": [200],
    "betanoob": [200],
    "woo": [200],
    "koolaid": [200],
    "ysided": [200],
    "tapegun": [200],
    "iggy": [200],
    "sneak": [200],
    "dozer": [200],
    "clouds": [200],
    "poomer": [200],
    "rexgunderman": [200],
    "cre8": [200],
    "sylo": [200],
    "gamesghoul": [200],
    "habibi": [200],
    "mood": [200],
    "v1nh": [200],
}

w = csv.writer(open("output.csv", "w"))
for key, val in data.items():
    w.writerow([key, val])


json = json.dumps(data)
f = open("rankings.json","w")
f.write(json)
f.close()
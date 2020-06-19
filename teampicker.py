import json

with open('rankings.json', 'r') as f:
    rankstore = json.load(f)

players = (input("list the 10 players that want to play seperated by a space: ").split())
accuracy = int(input("input a number greater than 10 for to determine accuracy: "))
bestteam1 = []
bestteam2 = []
#initial values for best teams

avg1 = 0
avg2 = 0
for x in range(5):
    avg1 += rankstore[players[x]][0]
    bestteam1.append(players[x])
for y in range(5):
    avg2 += rankstore[players[y+5]][0]
    bestteam2.append(players[y+5])


diffavg = abs(avg1-avg2)

def avgdifference():
    tempavg1 = 0
    tempavg2 = 0
    for a in range(len(bestteam1)):
        tempavg1 += rankstore[bestteam1[a]][0]
    tempavg1 = tempavg1/len(bestteam1)

    for b in range(len(bestteam2)):
        tempavg2 += rankstore[bestteam2[b]][0]
    tempavg2 = tempavg2/len(bestteam2)
    return abs(tempavg1 - tempavg2)

for y in range (accuracy):
    for a in range(5):
        for b in range (5):
            temp = bestteam1[a]
            bestteam1[a] = bestteam2[b]
            bestteam2[b] = temp
            if(avgdifference() > diffavg):
                diffavg = avgdifference()
                continue

print("team one: " + str(bestteam1))
print("team two: " + str(bestteam2))
print("skill difference: " + str(diffavg))
### P(players, 10) different teams **permutations**


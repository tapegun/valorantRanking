import json

# gamedata = json.loads(scrimvalues.json)
# rankdata = json.loads(rankings.json)

def sortthird(val): 
    return val[12]  

with open('rankings.json') as f:
    rankstore = json.load(f)
with open('newgame.json', 'r') as s:
    gamestore = json.load(s)
# orderedkd = []
# for x in range(10):
#     player = gamestore[str(x+1)]
#     if(len(orderedkd) == 0):
#         orderedkd.append(player)
#     else:
#         for y in range(len(orderedkd)):
#             if(orderedkd[y][2] < player[2]):
#                 orderedkd.insert(y,player)
#                 break;
#         orderedkd.append(player)

# orderedkd.sort(key=sortthird)   

average1 = 0
average2 = 0

stddev1 = 0
stddev2 = 0 

# calculating average team 1
for a in range(5):
    average1 += gamestore[str(a+1)][2]

average1 = (average1/5.0)

# calculating standard deviation team 1
for b in range(5):
    stddev1 += (gamestore[str(b+1)][2] - average1)**2
stddev1 = (stddev1/4.0)**(.5)



# calculating average team 2
for c in range(5):
    average2 += gamestore[str(c+5)][2]

average2 = (average2/5.0)

# calculating standard deviation team 2
for d in range(5):
    stddev2 += (gamestore[str(d+5)][2] - average2)**2
stddev2 = (stddev2/4.0)**(.5)

for z in range(10):
    playername = gamestore[str(z)][0]
    csnew = gamestore[str(z)][1]
    kda = gamestore[str(z)][2]
    csstable = rankstore[playername][0]


    if(z<5):
        newelo = ((3.0/4)*(csstable) + ((1.0/4)*(csnew)*((kda-average1) + 1)))
        print(playername + "'s new elo is " + str(newelo))
        rankstore[playername][0] = newelo
    else:
        newelo = ((3.0/4)*(csstable) + ((1.0/4)*(csnew)*((kda-average2) + 1)))
        print(playername + "'s new elo is " + str(newelo))
        rankstore[playername][0] = newelo

sort = sorted(rankstore.items(), key=lambda x: x[1], reverse=True)
print(sort)

with open('rankings.json', 'w+') as f:
    json.dump(rankstore, f)


with open('sortedrankings.json', 'w+') as f:
    json.dump(sort, f)
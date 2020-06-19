import json

p1 = input("enter name, combat score, and k/d seperated by a space: ").split()
p2 = input("enter name, combat score, and k/d seperated by a space: ").split()
p3 = input("enter name, combat score, and k/d seperated by a space: ").split()
p4 = input("enter name, combat score, and k/d seperated by a space: ").split()
p5 = input("enter name, combat score, and k/d seperated by a space: ").split()
p6 = input("enter name, combat score, and k/d seperated by a space: ").split()
p7 = input("enter name, combat score, and k/d seperated by a space: ").split()
p8 = input("enter name, combat score, and k/d seperated by a space: ").split()
p9 = input("enter name, combat score, and k/d seperated by a space: ").split()
p10 = input("enter name, combat score, and k/d seperated by a space: ").split()

for y in range(2):
    p1[y+1] = float(p1[y+1])
for y in range(2):
    p2[y+1] = float(p2[y+1])
for y in range(2):
    p3[y+1] = float(p3[y+1])
for y in range(2):
    p4[y+1] = float(p4[y+1])
for y in range(2):
    p5[y+1] = float(p5[y+1])
for y in range(2):
    p6[y+1] = float(p6[y+1])
for y in range(2):
    p7[y+1] = float(p7[y+1])
for y in range(2):
    p8[y+1] = float(p8[y+1])
for y in range(2):
    p9[y+1] = float(p9[y+1])
for y in range(2):
    p10[y+1] = float(p10[y+1])

data = {
    0 : p1[0:],
    1 : p2[0:],
    2 : p3[0:],
    3 : p4[0:],
    4 : p5[0:],
    5 : p6[0:],
    6 : p7[0:],
    7 : p8[0:],
    8 : p9[0:],
    9 : p10[0:],
}



json = json.dumps(data)
f = open("newgame.json","w")
f.write(json)
f.close()
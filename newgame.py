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

for y in range(3):
    p1[y+1] = int(p1[y+1])
for y in range(3):
    p2[y+1] = int(p2[y+1])
for y in range(3):
    p3[y+1] = int(p3[y+1])
for y in range(3):
    p4[y+1] = int(p4[y+1])
for y in range(3):
    p5[y+1] = int(p5[y+1])
for y in range(3):
    p6[y+1] = int(p6[y+1])
for y in range(3):
    p7[y+1] = int(p7[y+1])
for y in range(3):
    p8[y+1] = int(p8[y+1])
for y in range(3):
    p9[y+1] = int(p9[y+1])
for y in range(3):
    p10[y+1] = int(p10[y+1])

data = {
    p1[0]: p1[1:],
    p2[0]: p2[1:],
    p3[0]: p3[1:],
    p4[0]: p4[1:],
    p5[0]: p5[1:],
    p6[0]: p6[1:],
    p7[0]: p7[1:],
    p8[0]: p8[1:],
    p9[0]: p9[1:],
    p10[0]: p10[1:],
}



json = json.dumps(data)
f = open("newgame.json","w")
f.write(json)
f.close()
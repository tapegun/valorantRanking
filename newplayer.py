import json

with open('rankings.json', 'r+') as f:
    data = json.load(f)
    x = str(input("enter players names separated by a space: "))
    x = x.split()
    for i in range(len(x)):
        cs = int(input("enter " + x[i] + "'s combat score "))
        data[x[i]] = [cs]
        

    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part
    
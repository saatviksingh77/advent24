import copy
f=open("day12/day12-input.txt",'r')
data=[list(x) for x in f.read().split()]
f.close()

def printmap(data):
    for rec in data:
        print(*rec,sep='')

letters=[]
for rec in data:
    for ch in rec:
        if(ch not in letters): letters.append(ch)
print(letters)


for letter in letters:
    for i in range(len(data)):
        for j in range(len(data[0])):
            if(i-1>=0):
                if(0): pass
            if(i<len(data[0])-1): pass
            if(j>=0): pass
            if(j<len(data)-1): pass


    print()

f=open("day01/day01-input.txt","r")
data=[i for i in f.read().split()]
f.close()

pos=50
zeros=0
for step in data:
    dir=step[0]
    jump=int(step[1:])
    
    if dir=="R" or dir=="r":
        newpos=pos+jump
        zeros+=newpos//100 - pos//100
    if dir=="L" or dir=="l":
        newpos=pos-jump
        zeros+=(pos-1)//100 - (newpos-1)//100
    

    print(newpos, zeros)

    pos=newpos

print(zeros)
f=open("day01/day01-input.txt","r")
data=[i for i in f.read().split()]
f.close()

pos=50
zeros=0

for step in data:
    dir= 1 if step[0]=="R" else -1
    jump=int(step[1:])
    pos+=dir*jump
    while pos<0 or pos>99:
        if pos<0: pos+=100
        elif pos>99: pos=0+(pos-100)
    if pos==0: zeros+=1
print(zeros)
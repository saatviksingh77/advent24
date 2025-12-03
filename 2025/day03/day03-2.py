with open("day03/day03-input.txt","r") as f:
    banks=[i for i in f.read().split()]
print(banks)

total=0
for bank in banks:
    length=12
    currnum=0
    nextindex=-1

    for x in range(length-1,-1,-1):
        digit=0
        for j in range(nextindex+1,len(bank)-x):
            if(int(bank[j])>digit):
                digit=int(bank[j])
                nextindex=j
                if(digit==9): break
        currnum+=digit*10**(x)

    total+=currnum
print(total)
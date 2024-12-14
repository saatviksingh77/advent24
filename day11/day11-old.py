f=open("day11/day11-input.txt","r")
data=[int(i) for i in f.read().split()]
f.close()

for i in range(25): #25 is fine, 75 takes too many resources and too long to execute
    newdata=[]
    for stone in data:
        stone=str(stone)
        if(int(stone)==0): newdata.append(1)
        elif(len(stone)%2==0):
            newdata.append(int(stone[:len(stone)//2]))
            if(int(stone[len(stone)//2:])==0):
                newdata.append(0)
            else: newdata.append(int(stone[len(stone)//2:]))
        else: newdata.append(int(stone)*2024)
    data=newdata
    # print(data)
    # print(len(data))
print(len(data))
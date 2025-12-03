with open("day03/day03-input.txt","r") as f:
    banks=[i for i in f.read().split()]

print(banks)
total=0
for bank in banks:
    maxnum=0
    maxindex=0
    for i in range(len(bank)-1):
        if(int(bank[i])>maxnum):
            maxnum=int(bank[i])
            maxindex=i
    
    nextnum=0
    for j in range(maxindex+1,len(bank)):
        if(int(bank[j])>nextnum):
            nextnum=int(bank[j])

    print(maxnum, nextnum)
    total+=maxnum*10+nextnum
print(total)
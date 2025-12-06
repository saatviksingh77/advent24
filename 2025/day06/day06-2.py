with open("day06/day06-input.txt","r") as f:
    data=[i for i in f.read().splitlines()]

operations=data[-1].split()
numlist=data[:-1]
# for i in numlist:print(i)
# print(operations)

totals=[]
opindex=0
if(operations[opindex]=='+'): currtotal=0
else: currtotal=1

for j in range(len(numlist[0])):
    strnum=''
    for i in range(n:=len(numlist)):
        strnum+=(numlist[i][j])
    strnum=strnum.strip()
    # print(strnum)
    if strnum=='':
        opindex+=1
        totals.append(currtotal)
        if(operations[opindex]=='+'): currtotal=0
        else: currtotal=1
        continue
    strnum=strnum.replace(' ','0')
    if operations[opindex]=='+':
        currtotal+=int(strnum)
    else:
        currtotal*=int(strnum)
    # print(currtotal, opindex, operations[opindex])
totals.append(currtotal)

# print(totals)
print(sum(totals))
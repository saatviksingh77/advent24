f=open("day9/day9-input.txt")
data=[int(i) for i in f.read()]
f.close()

blocks=[]
id=0
for i in range(len(data)):
    if(i%2==0):
        for k in range(data[i]): blocks.append(str(id))
        id+=1
    else:
        for k in range(data[i]): blocks.append('.')
#print(*blocks,sep='')

while(True):
    spot=0
    num=len(blocks)-1
    for f in range(len(blocks)):
        if(not blocks[f].isdigit()):
            spot=f
            break
    for b in range(len(blocks)-1,-1,-1):
        if(blocks[b].isdigit()):
            num=b
            break
    if(spot>num): break
    blocks[spot]=blocks[num]
    blocks[num]='.'
#print(*blocks,sep='')

checksum=0
for i in range(len(blocks)):
    if(not blocks[i].isdigit()): break
    else:
        checksum+=i*int(blocks[i])
print(checksum)
import time
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

for k in range(len(blocks)):
    if(not blocks[k].isdigit()):
        slot=[k]
        break
for k in range(len(blocks)-1,-1,-1):
    if(blocks[k].isdigit):
        file=[k]
        break


counter=0
while(True):
    
    for b in range(file[0]-1,-1,-1):
        if(blocks[b].isdigit()):
            if (blocks[b]==blocks[file[-1]]):
                file.insert(0,b)
            else: break
    print(file)

    while(slot[-1]<file[0]):
        
        for f in range(slot[-1]+1,file[0]):
            if(not blocks[f].isdigit()):
                slot.append(f)
            else: break
        print(slot)
        time.sleep(2)
        
        if(len(slot)>=len(file)):
            for i in range(len(file)):
                blocks[slot[i]]=blocks[file[i]]
                blocks[file[i]]='.'
                lastreplaced=slot[i]
            break
        else: lastreplaced=slot[-1]
    
    print(*blocks,sep='')

    for k in range(lastreplaced+1,len(blocks)):
        if(not blocks[k].isdigit()):
            slot=[k]
            break
    for k in range(file[0]-1,-1,-1):
        if(blocks[k].isdigit):
            file=[k]
            break
    
    print(slot)
    print(file)
    print()
    # if(file[0]==0):
    #     break
    counter+=1
    if(counter==3): break
    
#print(*blocks,sep='')

checksum=0
for i in range(len(blocks)):
    if(not blocks[i].isdigit()): break
    else:
        checksum+=i*int(blocks[i])
print(checksum)
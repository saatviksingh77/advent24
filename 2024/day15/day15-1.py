f=open("day15/day15-input.txt",'r')
input=f.read().split('\n\n')
f.close()
robomap=[list(i) for i in input[0].split()]
moves=input[1].replace("\n",'')

# for rec in robomap:
#     print(*rec,sep='')
# print(moves)

for i in range(len(robomap)):
    for j in range(len(robomap[0])):
        if(robomap[i][j]=='@'):
            pos=[i,j]
            break
    else: continue
    break
# print(pos)

counter=1
for move in moves:
    if(move=='<'):
        if(robomap[pos[0]][pos[1]-1]=='.'):
            robomap[pos[0]][pos[1]-1]='@'
            robomap[pos[0]][pos[1]]='.'
            pos[1]-=1
        elif(robomap[pos[0]][pos[1]-1]=='O'):
            i=2
            while(robomap[pos[0]][pos[1]-i]=='O'): i+=1
            if(robomap[pos[0]][pos[1]-i]=='.'):
                while(i>1):
                    robomap[pos[0]][pos[1]-i]='O'
                    robomap[pos[0]][pos[1]-i+1]='.'
                    i-=1
                robomap[pos[0]][pos[1]-1]='@'
                robomap[pos[0]][pos[1]]='.'
                pos[1]-=1

    elif(move=='>'):
        if(robomap[pos[0]][pos[1]+1]=='.'):
            robomap[pos[0]][pos[1]+1]='@'
            robomap[pos[0]][pos[1]]='.'
            pos[1]+=1
        elif(robomap[pos[0]][pos[1]+1]=='O'):
            i=2
            while(robomap[pos[0]][pos[1]+i]=='O'): i+=1
            if(robomap[pos[0]][pos[1]+i]=='.'):
                while(i>1):
                    robomap[pos[0]][pos[1]+i]='O'
                    robomap[pos[0]][pos[1]+i-1]='.'
                    i-=1
                robomap[pos[0]][pos[1]+1]='@'
                robomap[pos[0]][pos[1]]='.'
                pos[1]+=1
        
    elif(move=='^'):
        if(robomap[pos[0]-1][pos[1]]=='.'):
            robomap[pos[0]-1][pos[1]]='@'
            robomap[pos[0]][pos[1]]='.'
            pos[0]-=1
        elif(robomap[pos[0]-1][pos[1]]=='O'):
            i=2
            while(robomap[pos[0]-i][pos[1]]=='O'): i+=1
            if(robomap[pos[0]-i][pos[1]]=='.'):
                while(i>1):
                    robomap[pos[0]-i][pos[1]]='O'
                    robomap[pos[0]-i+1][pos[1]]='.'
                    i-=1
                robomap[pos[0]-1][pos[1]]='@'
                robomap[pos[0]][pos[1]]='.'
                pos[0]-=1

    elif(move=='v'):
        if(robomap[pos[0]+1][pos[1]]=='.'):
            robomap[pos[0]+1][pos[1]]='@'
            robomap[pos[0]][pos[1]]='.'
            pos[0]+=1
        elif(robomap[pos[0]+1][pos[1]]=='O'):
            i=2
            while(robomap[pos[0]+i][pos[1]]=='O'): i+=1
            if(robomap[pos[0]+i][pos[1]]=='.'):
                while(i>1):
                    robomap[pos[0]+i][pos[1]]='O'
                    robomap[pos[0]+i-1][pos[1]]='.'
                    i-=1
                robomap[pos[0]+1][pos[1]]='@'
                robomap[pos[0]][pos[1]]='.'
                pos[0]+=1

    # print(move,counter)
    # for rec in robomap:
    #     print(*rec,sep='')
    # # print(pos[0],pos[1])
    # print()
    # counter+=1

gps=0
for i in range(len(robomap)):
    for j in range(len(robomap[0])):
        if(robomap[i][j]=='O'): gps+=(100*i)+j
print(gps)
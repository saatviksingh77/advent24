import copy,time
t1=time.time()
f=open('day6/day6-input.txt','r')
map=[list(i) for i in f.read().split()]
f.close()

def printmap(map):
    for i in map:
        for j in i: print(j,end='')
        print()
    print()
printmap(map)

ogmap=copy.deepcopy(map)

dir=['U','R','D','L']
diridx=0
def update_dir():
    global diridx
    diridx+=1
    diridx%=4
def direction():
    return dir[diridx]

for row in map:
    for char in row:
        if(char=='^'): pos=[map.index(row),row.index(char)]

U=0
R=len(map[0])-1
L=0
D=len(map)-1

loop=0

for i in range(len(ogmap)):
    for j in range(len(ogmap[0])):
        if(map[i][j]=='.'): map[i][j]='#'
        else: continue
        seenstates=[]

        for row in map:
            for char in row:
                if(char=='^'): pos=[map.index(row),row.index(char)]
        diridx=0
        
        ti=time.time()
        while(not(direction()=='U' and pos[0]==U) and not(direction()=='R' and pos[1]==R) and not(direction()=='D' and pos[0]==D) and not(direction()=='L' and pos[1]==L)):
            state=copy.deepcopy((pos,direction()))
            seenstates.append(state)
            
            if(direction()=='U'):
                if(map[pos[0]-1][pos[1]]!='#'):
                    map[pos[0]][pos[1]]='X'
                    pos[0]-=1
                else: update_dir()
            if(direction()=='R'):
                if(map[pos[0]][pos[1]+1]!='#'):
                    map[pos[0]][pos[1]]='X'
                    pos[1]+=1
                else: update_dir()
            if(direction()=='D'):
                if(map[pos[0]+1][pos[1]]!='#'):
                    map[pos[0]][pos[1]]='X'
                    pos[0]+=1
                else: update_dir()
            if(direction()=='L'):
                if(map[pos[0]][pos[1]-1]!='#'):
                    map[pos[0]][pos[1]]='X'
                    pos[1]-=1
                else: update_dir()
            
            newstate=copy.deepcopy((pos,direction()))
            if(newstate in seenstates):
                loop+=1
                print(loop)
                break
        tf=time.time()
        print(i,j, tf-ti)
        map=copy.deepcopy(ogmap)

t2=time.time()
print(loop)
print(t2-t1) #### Ran for 80-85 minutes
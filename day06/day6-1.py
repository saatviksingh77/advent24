f=open('day6/day6-input.txt','r')
map=[list(i) for i in f.read().split()]
f.close()

def printmap(map):
    for i in map:
        for j in i: print(j,end='')
        print()
    print()

printmap(map)

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

while(not(direction()=='U' and pos[0]==U) and not(direction()=='R' and pos[1]==R) and not(direction()=='D' and pos[0]==D) and not(direction()=='L' and pos[1]==L)):
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
map[pos[0]][pos[1]]='X'

printmap(map)

count=0
for row in map:
    for char in row:
        if(char=='X'): count+=1
print(count)
f=open("day10/day10-input.txt",'r')
topo=[list(map(int,i)) for i in f.read().split()]
f.close()
print(topo)

zeros=[]
for i in range(len(topo)):
    for j in range(len(topo[0])):
        if topo[i][j]==0: zeros.append([i,j])
print(zeros)

for zeropos in zeros:
    elementpos=zeropos
    digits=[[]]
    while(topo[elementpos[0]][elementpos[1]]!=9):
        up=[elementpos[0]-1,elementpos[1]]
        down=[elementpos[0]+1,elementpos[1]]
        right=[elementpos[0],elementpos[1]+1]
        left=[elementpos[0],elementpos[1]-1]

        if(up[0]>=0):
            if(topo[up[0]][up[1]]==topo[elementpos[0]][elementpos[1]]+1):
                digits.append(up)
        if(down[0]<len(topo)):

        if(left[1]>=0):

        if(right[1]<len(topo)):

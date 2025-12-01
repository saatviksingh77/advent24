import copy
f=open("day8/day8-input.txt",'r')
data=[list(i) for i in f.read().split()]
f.close()

ansmap=copy.deepcopy(data)
for i in range(len(ansmap)):
    for j in range(len(ansmap[0])):
        if(j!='.'): ansmap[j][i]='.'

# print(*data,sep='\n')
# print()
# print(*ansmap,sep='\n')

antennas={}
for i in range(len(data)):
    for j in range(len(data[0])):
        if(data[i][j]!='.'):
            if(data[i][j] in antennas): antennas[data[i][j]].append([i,j])
            else: antennas[data[i][j]]=[[i,j]]
        print(data[i][j],end='')
    print()
#print(antennas)

for key in antennas:
    for first in range(len(antennas[key])):
        for second in range(first+1,len(antennas[key])):
            distr=antennas[key][first][0]-antennas[key][second][0]
            distc=antennas[key][first][1]-antennas[key][second][1]

            if(distr<0):
                pos1r=antennas[key][first][0]+distr
                pos2r=antennas[key][second][0]-distr
            else:
                pos1r=antennas[key][first][0]-distr
                pos2r=antennas[key][second][0]+distr
            
            if(distc>0):
                pos1c=antennas[key][first][1]+distc
                pos2c=antennas[key][second][1]-distc
            else:
                pos1c=antennas[key][first][1]+distc
                pos2c=antennas[key][second][1]-distc

            # print(antennas[key][first][0],antennas[key][first][1])
            # print(antennas[key][second][0],antennas[key][second][1])
            # print(distr,distc)
            # print(pos1r,pos1c)
            # print(pos2r,pos2c)
            #print()
            
            if(pos1r>=0 and pos1r<len(ansmap)) and (pos1c>=0 and pos1c<len(ansmap[0])):
                ansmap[pos1r][pos1c]='#'
            if(pos2r>=0 and pos2r<len(ansmap)) and (pos2c>=0 and pos2c<len(ansmap[0])):
                ansmap[pos2r][pos2c]='#'

print()
for i in ansmap:
    print(*i,sep='')
print()

count=0
for i in ansmap:
    for j in i:
        if(j=='#'): count+=1
print(count)
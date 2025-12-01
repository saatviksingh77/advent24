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
# print(antennas)

for key in antennas:
    for first in range(len(antennas[key])):
        for second in range(first+1,len(antennas[key])):
            pos1r=antennas[key][first][0]
            pos1c=antennas[key][first][1]
            pos2r=antennas[key][second][0]
            pos2c=antennas[key][second][1]

            ansmap[pos1r][pos1c]='#'
            ansmap[pos2r][pos2c]='#'

            distr=pos1r-pos2r
            distc=pos1c-pos2c
            
            while(((pos1r>=0 and pos1r<len(ansmap)) and (pos1c>=0 and pos1c<len(ansmap[0]))) or ((pos2r>=0 and pos2r<len(ansmap)) and (pos2c>=0 and pos2c<len(ansmap[0])))):
                if(distr<0):
                    pos1r=pos1r+distr
                    pos2r=pos2r-distr
                else:
                    pos1r=pos1r-distr
                    pos2r=pos2r+distr
                
                if(distc>0):
                    pos1c=pos1c+distc
                    pos2c=pos2c-distc
                else:
                    pos1c=pos1c+distc
                    pos2c=pos2c-distc
                
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
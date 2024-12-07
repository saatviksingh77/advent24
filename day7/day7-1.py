from itertools import product
f=open("day7/day7-input.txt",'r')
data=[list(map(int,i.split())) for i in f.read().splitlines()]
f.close()

total=0
for rec in data:
    target=rec[0]
    op=list(product(['*','+'],repeat=len(rec)-2))
    for k in range(len(op)):
        ans=rec[1]
        for i in range(len(op[0])):
            if(op[k][i]=='+'): ans+=rec[2+i]
            else: ans*=rec[2+i]
        if ans==target:
            total+=ans
            break

print(total)
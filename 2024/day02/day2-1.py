f=open("day2/day2-input.txt",'r')
l=f.read().splitlines()
f.close()
data=[list(map(int,i.split())) for i in l]
#print(data)

safe=0
for rec in data:
    flag=True
    inc=False
    dec=False
    if(rec[1]-rec[0]>0): inc=True
    else: dec=True
    for i in range(len(rec)-1):
        if(inc):
            if(not(rec[i+1]-rec[i]>=1 and rec[i+1]-rec[i]<=3)): flag=False
        if(dec):
            if(not(rec[i]-rec[i+1]>=1 and rec[i]-rec[i+1]<=3)): flag=False
    if(flag): safe+=1
print(safe)
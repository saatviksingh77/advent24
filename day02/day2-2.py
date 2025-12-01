f=open("day2/day2-input.txt",'r')
l=f.read().splitlines()
f.close()
data=[list(map(int,i.split())) for i in l]
#print(data)

def checksafe(rec):
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
    return flag

unsafe=[]
for rec in data:
    if(not checksafe(rec)): unsafe.append(rec)

newsafe=[]
for rec in unsafe:
    for i in range(len(rec)):
        ele=rec.pop(i)
        if(checksafe(rec)):
            newsafe.append(rec)
            break
        else: rec.insert(i,ele)

total=len(data)-len(unsafe)+len(newsafe)
print(total)
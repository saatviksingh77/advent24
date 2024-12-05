import re
f=open("day3/day3-input.txt",'r')
data=f.read().split("do()")

l=[]
count=0
for rec in data:
    l.append(re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",rec.split("don't()")[0]))
#print(l)

sum=0
for x in l:
    for k in x:
        sum+=int(k[0])*int(k[1])
print(sum)
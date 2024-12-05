import re
f=open("day3/day3-input.txt",'r')
data=f.read()
l=re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",data)
sum=0
for x in l:
    sum+=int(x[0])*int(x[1])
print(sum)
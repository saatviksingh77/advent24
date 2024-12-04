import re,numpy
f=open("day4-input.txt",'r')
data=f.read().split()
#print(data)

count=0
for rec in data:
    count+=len(re.findall("XMAS",rec))
    count+=len(re.findall("SAMX",rec))

for i in range(len(data)-3):
    for j in range(len(data[0])-3):
        if((data[i][j]=="X" and data[i+1][j+1]=="M" and data[i+2][j+2]=="A" and data[i+3][j+3]=="S") or (data[i][j]=="S" and data[i+1][j+1]=="A" and data[i+2][j+2]=="M" and data[i+3][j+3]=="X")): count+=1

for i in range(len(data)-3):
    for j in range(3,len(data[0])):
        if((data[i][j]=="X" and data[i+1][j-1]=="M" and data[i+2][j-2]=="A" and data[i+3][j-3]=="S") or (data[i][j]=="S" and data[i+1][j-1]=="A" and data[i+2][j-2]=="M" and data[i+3][j-3]=="X")): count+=1

for i in range(len(data)-3):
    for j in range(len(data[0])):
        if((data[i][j]=="X" and data[i+1][j]=="M" and data[i+2][j]=="A" and data[i+3][j]=="S") or (data[i][j]=="S" and data[i+1][j]=="A" and data[i+2][j]=="M" and data[i+3][j]=="X")): count+=1

print(count)
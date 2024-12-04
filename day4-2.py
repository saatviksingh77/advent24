import re,numpy
f=open("day4-input.txt",'r')
data=f.read().split()
#print(data)

count=0
for i in range(len(data)-2):
    for j in range(len(data[0])-2):
        if(((data[i][j]=="M" and data[i+1][j+1]=="A" and data[i+2][j+2]=="S") or (data[i][j]=="S" and data[i+1][j+1]=="A" and data[i+2][j+2]=="M")) and ((data[i][j+2]=="M" and data[i+1][j+1]=="A" and data[i+2][j]=="S") or (data[i][j+2]=="S" and data[i+1][j+1]=="A" and data[i+2][j]=="M"))): count+=1

print(count)
with open("day04/day04-input.txt","r") as f:
    data=[i for i in f.read().split()]

rows=len(data)
cols=len(data[0])
valid=0
for i in range(rows):
    for j in range(cols):
        if(data[i][j]=="@"):
            adj=0
            if(i-1>=0 and j-1>=0 and    data[i-1][j-1]=='@'): adj+=1
            if(i-1>=0 and               data[i-1][j]=='@'): adj+=1
            if(i-1>=0 and j+1<cols and  data[i-1][j+1]=='@'): adj+=1
            
            if(j-1>=0 and               data[i][j-1]=='@'): adj+=1
            if(j+1<cols and             data[i][j+1]=='@'): adj+=1

            if(i+1<rows and j-1>=0 and      data[i+1][j-1]=='@'): adj+=1
            if(i+1<rows and                 data[i+1][j]=='@'): adj+=1
            if(i+1<rows and j+1<cols and    data[i+1][j+1]=='@'): adj+=1

            if adj<4: valid+=1
print(valid)


        






with open("day04/day04-input.txt","r") as f:
    data=[list(i) for i in f.read().split()]

rows=len(data)
cols=len(data[0])

valid=1
total=0
removed=[]
while(valid>0):
    valid=0
    removed.clear()
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

                if adj<4:
                    valid+=1
                    removed.append([i,j])
    total+=valid
    print(removed)
    for pt in removed:
        data[pt[0]][pt[1]]="."
print(total)


        






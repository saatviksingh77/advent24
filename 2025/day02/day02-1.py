f=open("day02/day02-input.txt","r")
idranges=[i for i in f.read().split(',')]
f.close()

points=[[int(i.split('-')[0]),int(i.split('-')[1])] for i in idranges]

print(idranges)
print(points)

total=0
for dataset in points:
    for i in range(dataset[0],dataset[1]+1):
        if (n:=len(str(i)))%2==0:
            if(str(i)[0:n//2]==str(i)[n//2:]): total+=i
print(total)
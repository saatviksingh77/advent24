from itertools import batched
with open("day02/day02-input.txt","r") as f:
    idranges=[i for i in f.read().split(',')]


points=[[int(i.split('-')[0]),int(i.split('-')[1])] for i in idranges]

print(idranges)
print(points)

total=0
for dataset in points:
    for num in range(dataset[0],dataset[1]+1):
        for x in range(1,len(str(num))//2+1):
            splitted=[''.join(batch) for batch in batched(str(num),x)]
            # print(splitted)
            if(len(set(splitted))==1):
                total+=num
                break
print(total)
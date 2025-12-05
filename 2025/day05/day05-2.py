with open("day05/day05-input.txt","r") as f:
    ranges,ids=[],[]
    for i in f.read().split():
        if('-' in i):
            ranges.append([int(i.split('-')[0]),int(i.split('-')[1])])
        else: ids.append(int(i))
ranges.sort(key=lambda inner: inner[0])
print(ranges)

freshranges=[ranges[0]]
for interval in ranges[1:]:
    for x in freshranges:
        if(interval[0]>=x[0] and interval[1]<=x[1]):
            break
        if(interval[0]>=x[0] and interval[0]<=x[1] and interval[1]>x[1]):
            x[1]=interval[1]
            break
    else:   
        freshranges.append(interval)

total=0
for x in freshranges: total+=x[1]-x[0]+1
print(total)

# fresh=set()
# for interval in ranges:
#     for i in range(interval[0],interval[1]+1): fresh.add(i)

# print(len(fresh))
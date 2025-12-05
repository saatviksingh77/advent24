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
    lastrange=freshranges[-1]
    if(interval[0]<=lastrange[1]):
        lastrange[1] = max(lastrange[1], interval[1])
    else:
        freshranges.append(interval)

'''
###   only checking the last range each time because since they are sorted,
###   there would be no conflict with any of the previous ranges
'''


total=0
for x in freshranges: total+=x[1]-x[0]+1
print(total)
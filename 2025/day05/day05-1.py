with open("day05/day05-input.txt","r") as f:
    ranges,ids=[],[]
    for i in f.read().split():
        if('-' in i):
            ranges.append(i.split('-'))
        else: ids.append(int(i))
print(ranges,ids)

fresh=0
for num in ids:
    for interval in ranges:
        if num>=int(interval[0]) and num<=int(interval[1]):
            fresh+=1
            break

print(fresh)
f=open("day19/day19-input.txt",'r')
data=f.read().split("\n\n")
combo=data[0].split(', ')
designs=data[1].split()
f.close()
print(combo)
print(designs)

max=0
for x in combo: max=len(x) if len(x) > max else max

left=0
right=1

count=1
for design in designs:

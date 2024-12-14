#took hint
from functools import cache

f=open("day11/day11-input.txt","r")
data=[int(i) for i in f.read().split()]
f.close()

@cache
def count(stone,steps):
    if(steps==0): return 1
    if(stone==0):
        return count(1,steps-1)
    if(len(str(stone))%2==0):
        return count(int(str(stone)[:len(str(stone))//2]),steps-1) + count(int(str(stone)[len(str(stone))//2:]),steps-1)
    return count(stone*2024,steps-1)

print(sum(count(stone,75) for stone in data))
#way more efficient
#can work till recursion depth limit(around 500)
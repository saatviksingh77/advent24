with open("day06/day06-input.txt","r") as f:
    data=[i for i in f.read().splitlines()]
operations=data[-1].split()
nums=[list(map(int,(i.split()))) for i in data[:-1]]
#print(nums,operations)

totals=nums[0]
for i in range(1,len(nums)):
    for j in range(len(nums[0])):
        if operations[j]=='+':
            totals[j]+=nums[i][j]
        else:
            totals[j]*=nums[i][j]

print(sum(totals))
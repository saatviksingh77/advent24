f=open("day5/day5-input.txt",'r')
data=f.read().split('\n\n')
f.close()
rules=[list(map(int,i.split('|'))) for i in data[0].split()]
updates=[list(map(int,i.split(','))) for i in data[1].split()]
# print(rules)
# print(updates)

valid=[]
for update in updates:
    update_valid=True
    for n in range(len(update)):
        for x in range(n+1,len(update)):
            rule_valid=False
            for rule in rules:
                if(rule[0]==update[n] and (rule[1]==update[x])):
                    rule_valid=True
                    break
            if(not rule_valid):
                update_valid=False
                break
        if(not update_valid): break
    if(update_valid): valid.append(update)

sum=0
for i in valid: sum+=i[len(i)//2]
print(sum)
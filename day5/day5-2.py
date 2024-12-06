f=open("day5/day5-input.txt",'r')
data=f.read().split('\n\n')
rules=[list(map(int,i.split('|'))) for i in data[0].split()]
updates=[list(map(int,i.split(','))) for i in data[1].split()]
# print(rules)
# print(updates)

invalid=[]
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
    if(not update_valid): invalid.append(update)

for update in invalid:
    changed=True
    while(changed):
        changed=False
        update_valid=True
        for n in range(len(update)):
            for x in range(n+1,len(update)):
                rule_valid=False
                for rule in rules:
                    if(rule[0]==update[n] and (rule[1]==update[x])):
                        rule_valid=True
                        break
                if(not rule_valid):
                    temp=update[n]
                    update[n]=update[x]
                    update[x]=temp
                    changed=True
                    update_valid=False
                    break
            if(not update_valid): break
        if(not update_valid): continue

sum=0
for i in invalid: sum+=i[len(i)//2]
print(sum)
from sympy import symbols, Eq, solve
f=open("day13/day13-inputedited.txt",'r')
temp=[i.split('\n') for i in f.read().split("\n\n")]
f.close()
machines=[]
for i in temp: machines.append([list(map(int,j.split(', '))) for j in i])
# print(*machines,sep='\n')

A_COST=3
B_COST=1

cost=0
for claw in machines:
    claw[2][0]+=10000000000000
    claw[2][1]+=10000000000000
    a,b=symbols('a,b')
    eq1=Eq((claw[0][0]*a+claw[1][0]*b),claw[2][0])
    eq2=Eq((claw[0][1]*a+claw[1][1]*b),claw[2][1])
    ans=solve((eq1,eq2),(a,b))
    # print(ans)
    if(int(ans[a])==ans[a] and int(ans[b])==ans[b]):  #also should add check for <100 moves but works without
        cost+=int(ans[a])*A_COST+int(ans[b])*B_COST
print(cost)

#runs slow
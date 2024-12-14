import re
WIDTH=101
HEIGHT=103
SECONDS=100

finalpos=[]
for robot in open("day14/day14-input.txt",'r').read().splitlines():
    px,py,vx,vy=map(int,(re.findall(r"-?\d+",robot)))
    finalpos.append([(px+vx*SECONDS)%WIDTH,(py+vy*SECONDS)%HEIGHT])

q1=q2=q3=q4=0
for pos in finalpos:
    px=pos[0]
    py=pos[1]
    if(px<WIDTH//2 and py<HEIGHT//2): q1+=1
    if(px>WIDTH//2 and py<HEIGHT//2): q2+=1
    if(px<WIDTH//2 and py>HEIGHT//2): q3+=1
    if(px>WIDTH//2 and py>HEIGHT//2): q4+=1

print(q1*q2*q3*q4)
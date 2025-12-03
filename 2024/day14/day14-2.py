#took hint
import re
WIDTH=101
HEIGHT=103

robots=[]
for robot in open("day14/day14-input.txt",'r').read().splitlines():
    robots.append(tuple(map(int,(re.findall(r"-?\d+",robot)))))

min=float("inf")
for sec in range(WIDTH*HEIGHT):
    finalpos=[]
    for px,py,vx,vy in robots:
        finalpos.append([(px+vx*sec)%WIDTH,(py+vy*sec)%HEIGHT])

    q1=q2=q3=q4=0
    for pos in finalpos:
        px=pos[0]
        py=pos[1]
        if(px<WIDTH//2 and py<HEIGHT//2): q1+=1
        if(px>WIDTH//2 and py<HEIGHT//2): q2+=1
        if(px<WIDTH//2 and py>HEIGHT//2): q3+=1
        if(px>WIDTH//2 and py>HEIGHT//2): q4+=1
    sf=q1*q2*q3*q4
    if(sf<min):
        ans=sec
        min=sf
print(ans)

#mathematical approach
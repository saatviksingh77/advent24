import re
WIDTH=101
HEIGHT=103

robots=[]
for robot in open("day14/day14-input.txt",'r').read().splitlines():
    robots.append(tuple(map(int,(re.findall(r"-?\d+",robot)))))

sec=7572
output=[['.']*WIDTH for i in range(HEIGHT)]
for px,py,vx,vy in robots:
    output[(py+vy*sec)%HEIGHT][(px+vx*sec)%WIDTH]='$'
for rec in output: print(*rec,sep='')
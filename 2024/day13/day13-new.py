import re
total=0
for block in open("day13/day13-input.txt",'r').read().split("\n\n"):
    ax,ay,bx,by,px,py=map(int,re.findall(r"\d+",block))
    px+=10000000000000
    py+=10000000000000
    ca=(px*by-py*bx)/(ax*by-ay*bx)
    cb=(px-ax*ca)/bx
    # if(ca%1==cb%1==0):
    #     if(ca<=100 and cb<=100):      #for part 1 check
    #         total+=int(ca*3+cb)
    if(ca%1==cb%1==0): total+=int(ca*3+cb)
print(total)

#much faster
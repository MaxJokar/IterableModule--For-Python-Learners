from ast import Break
import itertools

# print(dir(itertools))
#start,step of count:Endless!
for i in itertools.count(0,8):
    if i>10:
       Break
    print(i,end="")
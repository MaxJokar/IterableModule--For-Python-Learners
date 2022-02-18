from ast import Break
import itertools

#count
# print(dir(itertools))
#start,step of count:Endless!
for i in itertools.count(0,2):
    if i>50:
       break
    print(i,end=" ")
    
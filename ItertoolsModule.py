from ast import Break
import itertools

#count
# print(dir(itertools))
#start,step of count:Endless!
# for i in itertools.count(0,2):
#     if i>50:
#        break
#     print(i,end=" ")
    
    
#cycle
# counter=0
# for i in itertools.cycle("Max Jokar"):    
#     if counter>17:
#         break
#     print(i,end=" ") 
#     counter+=1                 
                         
                         
# counter=0
# for i in itertools.cycle([12,23,45,56,89,78,45,12,5]):    
#     if i>80:
#       break
#     print(i,end=" ") 
                
                                              
                         
 # Repeat: how many times?4 times
# for i in itertools.repeat("Max Jokar", 4) :                        
#     print(i,end='')                       
                         
                         
                         
#Produt             


# print(list(itertools.product([1,2,3],['a','b'])))
# print(list(itertools.product([1,2,3],['a','b'],repeat=2)))
# print(list(itertools.product([1,2,3],['a','b'],"george")))


#Permutations ;
# print(list(itertools.permutations([1,2,3,4,5],3)))


#(Combinations Methods)
# print(list(itertools.combinations([1,2,3,4,5],3)))
# print(list(itertools.combinations(['A','B','C'],3)))


# print(list(itertools.combinations_with_replacement([1,2,3,4,5],3)))


import operator
#accumulate: To calculate,compute , operate  on a  list 

#adds the items inside the list , two parameters
# list1=[8,3,6,2]
# print(list1)
# list2=list(itertools.accumulate(list1,operator.add))
# print(list2)
# list2=list(itertools.accumulate(list1,operator.sub))
# print(list2)
# list2=list(itertools.accumulate(list1,operator.mul))
# print(list2)
# list2=list(itertools.accumulate(list1,operator.mod))
# print(list2)


#Chain

# list1=[1,2,3]
# list2=["dany","jack","Max"]
# list3=[1200,True]
# list4=[True,False,True]

# mainlist=[list1,list2,list3,list4]
# print(mainlist)
# chainlist=list(itertools.chain.from_iterable(mainlist))
# print(chainlist)



# print(list(itertools.chain.from_iterable([list1,list2,list3,list4])))

# list1=[1,2,3]
# list2=("dany","jack","Max")
# list3="Max Jokar"
# list4=[True,False,True]
# print(list(itertools.chain.from_iterable([list1,list2,list3,list4])))



#Compress:drag a group of  things from a  complex
# print(list(itertools.compress("Max Jokar",[1,0,1,0,0,1,0,1])))

#Example for Compress:
# print(list(itertools.compress(["Max","Dany","Rose","Philip"],[1,0,1,0,1,0])))

#DropWhile

# list1=[2,4,5,6,89,78,45,1,25]
# itertools.dropwhile(lambda x:x%2==0,list1)
# print(list(itertools.dropwhile(lambda x:x%2==0,list1)))



#TakeWhile:Brings those ones have our condition

# list1=[2,4,5,6,89,78,45,1,25]
# print(list(itertools.takewhile(lambda x:x%2==0,list1)))



#FilterFalse:brings odd number
list1=[2,4,5,6,89,78,45,1,25]

print(list(itertools.filterfalse(lambda x:x%2==0,list1)))



#iSlice:list code, start, stop, step
list1=[2,4,5,6,89,78,45,1,25]
# print(list(itertools.islice(list1,2,25,2)))
print(list1[2:8:2])




























































                    
                         
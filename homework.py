# def averageThree(a,b,c):
#     return (a+b+c)/3

# result=averageThree(3,8,1)
# print(result)


import functools
# def averageList(a):
#     sum=0
#     for elm in a:
#         sum+=elm
        
#     return sum/len(a)

def sum(x,y):
    return x+y

def averageList(a):
    s=functools.reduce(sum,a)    
    return s/len(a)







# def make01List(a):
#     c=[]
#     for elm in a:
#         if elm%2==0:
#             c.append(1)
#         else:
#             c.append(0)
            
#     return c

 
def make01List(a):
    return list(map(lambda x:1 if x%2==0 else 0,a))
    

result3=make01List([6, 3, 4, 1, 9, 13])
print(result3)




def removeElemFromList(list1, k):
    resultList = []
    for elem in list1:
        if(elem != k): resultList.append(elem)
    return resultList
removeElemFromList([1, 2, 3, 2], 2)
[i for i in [1,2,3,2] if i!=2]
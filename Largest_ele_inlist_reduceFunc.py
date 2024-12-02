import functools 
l=[1,445,8879,0]
print(functools.reduce(lambda x,y:x if x>y else y,l))

def days(index):
    day = ['S','M','T','W','Tr','F','St']            
    yield day[index]    
    yield day[index+1]  
  
res = days(0)
print(next(res), next(res))

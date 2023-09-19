def tmp(a, b=[1,2,3]):
         b.append(a)     
         return b  
a = tmp(4) 
b = tmp(5) 
print(b)

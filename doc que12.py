def fun(a):
    a=[1450,96000,1050,1050]    
    i=0
    b=[]
    while i<len(a):
        while a[i]>0:
            if a[i]%10!=0:
                b.append(a[i])
                break
            a[i]//=10
        i+=1  
    print(b)         
(fun([1450,96000,1050,1050]))  
           
l=[1200,300400,190500]
i=0
b=[]
while i<len(l):
    while l[i]>0:
        if l[i]%10!=0:
            b.append(l[i])
            break
        l[i]=l[i]//10
    i+=1
print(b)        
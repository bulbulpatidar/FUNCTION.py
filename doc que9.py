def square(a):
    i=1
    l=[]
    l1=[]
    while i<=(a):
        if i>0 and i<6:
            l.append(i**2)
        elif i>25 and i<=30:
            l1.append(i**2)
        i+=1
    print((l,l1))  
square(30)          
 
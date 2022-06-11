def my_func(l):
    
    i=0
    max=0
    max2=0
    while i<len(l):
        j=0
        while j<len(l): 
            if l[j]>max:
                max=l[j]
            if l[j]>max2 and l[j]!=max:
                max2=l[j]
            j+=1    
        i+=1
    print("first max ",max) 
    print("second max",max2)
    print(max+max2)
my_func([10,14,2,23,19])          
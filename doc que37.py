
def present(a):
    i=0
    count=0
    while i<len(a):
        if a[i]==True:
            count+=1
        i+=1
    print(count)  
present([True, True, True, False,
True, True, True, True ,
True, False, True, False,
True, False, False, True ,
True, True, True, True ,
False, False, True, True])          
         

    
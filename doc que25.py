def count_positive_negative(a):
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>0:
            c+=1
        if a[i]<0:
            c1+=1
        i+=1
    print("positive number:-",c)
    print("negative number:-",c1)  
count_positive_negative([2,-7,5,-64,-14])              
            

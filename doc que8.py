
def string(a):
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>="a" and a[i]<="z":
            c+=1
        if a[i]>="A" and a[i]<="Z":
            c1+=1
        i+=1
    print("uppercase letter : ",c1)  
    print("lowercase letter : ",c) 
string("The quick Brow Fox")      


def perfect(n):
    s=0
    i=1
    while i<n:
        if n%i==0:
            s+=i
        i+=1     
    print(s)
    if s==n:
        print("perfect number")
    else:
        print("not perfect number")
a=int(input("enter the num :-"))        
perfect(a)                    
    



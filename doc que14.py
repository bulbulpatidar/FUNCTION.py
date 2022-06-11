def primeornot(n):
    count=0
    i=1
    while i<=n:
        if n%i==0:
            count=count+1
        i+=1
    if count==2:
        print("prime number")
    else:
        print("not prime number")
a=int(input("enter the number:-")) 
primeornot(a)           

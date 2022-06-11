
def primeornot(n):
    a=1
    while a<=n:
       count=0
       i=1
       while i<=a:
            if a%i==0:
                count=count+1
            i+=1
       if count==2:
            print("prime number",a)
       else:
            print("not prime number",a)  
       a+=1      

a=int(input("enter the number:-")) 
primeornot(a)           

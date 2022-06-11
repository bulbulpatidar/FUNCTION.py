
def my_fun(l):
    i=0
    while i<len(l):    
        if l[i]%2==0:
            print(100*l[i])
        else:
            print(l[i]*-1)
        i+=1 
l=[]
i=1
while i<=5:
    n=int(input("enter the number:-"))
    i+=1
    l.append(n)
print(l) 
my_fun(l)        

   

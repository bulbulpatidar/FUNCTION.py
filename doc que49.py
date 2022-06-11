

def evenodd(n):
    i=0
    while i<len(n):
        if n[i]%2==0:
            print("even")
        if n[i]%2!=0:
            print("odd")
        i+=1
        
b=int(input("enter the number:-"))
i=0
n=[]
while i<=b:
    e=int(input("enter the element:-"))
    i+=1
    n.append(e)
# print(n) 
evenodd(n)            
    
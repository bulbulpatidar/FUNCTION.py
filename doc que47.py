

l=[2,4,6,8]
i=0
b=[]
while i<len(l)-1:
    k=l[i+1]-l[i]
    b.append(k)
    i+=1
print(b) 
i=0
c=0
a=b[i]
while i<len(b):
    if b[i]==a:
        c+=1
    i+=1 
if c==len(b):
    print("true")
else:
    print("false")                

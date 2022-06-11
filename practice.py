# def sum():
#     a=3
#     b=4
#     c=2
#     print(a+b+c)
# sum()    

# def greter(a,b):
#     ad=a+b
#     if ad>=15 and ad<=20:
#         print("20")
#     else:
#         print(ad) 
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# greter(a,b)           

# def reverse(a):
#     i=1
#     l=[]
#     while i<=len(a):
#         l.append(a[-i])
#         i+=1
#     print(l)
# reverse(["a","3",5,"e"])        

def present(n):
    b=int(input("enter the number"))
    i=0
    while i<len(n):
        if n[i]==b:
            print(b,"is present")
            break
        else:
            print("not present")
            break
        i+=1
l=[]
j=1
while j<=5:
    e=int(input("enter the element"))
    j+=1
    l.append(e)
print(l)  
present(l)  



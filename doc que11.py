def generaterange(a,b,c):
    l=[]
    for i in range(a,b,c):
        l.append(i)
    print(l)  
a=int(input("enter the starting number that will be min :-")) 
b=int(input("enter the endind number that will be max :-")) 
c=int(input("enter the step value :-"))  
generaterange(a,b,c) 

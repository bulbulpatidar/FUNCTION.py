def calculater(operation):
    a=int(input("enter the number:-"))
    b=int(input("enter the number:-"))
    if operation=="+":
        print(a+b)
    elif operation=="-":
        print(a-b)
    elif operation=="*":
        print(a*b)
    elif operation=="/":
        print(a/b)
calculater("+")
calculater("-")
calculater("*")
calculater("/")      

# # 
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])    
# def multiply(a,b):
#     i=0
#     j=0
#     m=[]
#     while i<len(a):
#         m.append(a[i]*b[j])
#         i+=1
#         j+=1

#     print(m)        

# multiply([5, 10, 50, 20], [2, 20, 3, 5])        

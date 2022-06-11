# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the
# sum (also as a string):
# "4", "5" --> "9"
# "34", "5" --> "39"
def sum(a,b):
    c=int(a)+int(b)
    d=str(c)
    print(d)
a=input("enter the number:")  
b=input("enter the number:")  
sum(a,b)    
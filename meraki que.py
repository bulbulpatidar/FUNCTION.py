def odev(a):
    i=0
    while i<=a:
        if i%2==0:
            print(i,"even number")
        if i%2!=0:
            print(i,"odd number")
        i+=1
n=int(input("enter number"))
odev(n)            


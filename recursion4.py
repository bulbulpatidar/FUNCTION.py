# GCD
def gcd(p,q):
    if q==0:
        return p
    else:
        return(gcd(q,p%q))
p=int(input("enter the largest number:-"))
q=int(input("enter the smallest number:-"))
z=gcd(p,q)
print("gcd",z)            



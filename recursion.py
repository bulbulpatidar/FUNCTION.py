def pettern(n):
    if n==0:
        return 
    print(" _ " *n)  
    pettern(n-1)
    print(" _ " *n)  
pettern(3)    

def maxlen_minlen(l):
    a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    i=0
    max=0
    min=len(a[i])
    n=[]
    k=[]
    while i<len(a):
        if len(a[i])>max:
            max=len(a[i])
            n=a[i]
        if len(a[i])<min:
            min=len(a[i])  
            k=a[i]  
        i+=1
    print(max,n) 
    print(min,k)       
maxlen_minlen([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])

                
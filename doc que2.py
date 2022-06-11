def maximum(n):
    # n=[4,6,12]
    i=0
    max=0
    while i<len(n):
        if n[i]>max:
            max=n[i]
        i+=1
    print(max)        
maximum([7,8,12])    
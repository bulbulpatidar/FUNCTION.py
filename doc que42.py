# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

def integer_sum(a):
    i=0
    n=[]
    while i<len(a):
        b=a[i]%10
        a[i]=a[i]//10
        n.append(b+a[i])
        i+=1
    print(n)
integer_sum([12, 67, 98, 34])        

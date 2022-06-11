# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

def uniq_list(a):
    l=[]
    i=0
    while i<len(a):
        if a[i] not in l:
            l.append(a[i])
        i+=1
    print(l) 
uniq_list([1,2,3,3,3,3,4,5])           



# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def even_num(m):
    l=[]
    for i in m:
        if i%2==0:
            l.append(i)
        i+=1
    print(l)
even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])            


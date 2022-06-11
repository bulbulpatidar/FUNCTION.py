
def max(l):
    i=0
    max=0
    while i<len(l):
        if l[i]>max:
            max=l[i]
        i+=1
    print(max)
max([4,6,2,1,9,63,-134,566])            

def min(a):
    i=0
    min=a[i]
    while i<len(a):
        if a[i]<min:
            min=a[i]
        i+=1
    print(min)
min([-52, 56, 30, 29, -54, 0, -110])            
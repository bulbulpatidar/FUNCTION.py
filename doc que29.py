def my_function(a):
    i=1
    sum=0
    while i<=a:
        if i%3==0:
            # print(i)
            sum+=i
        if i%5==0:
            # print(i)
            sum+=i
        i+=1
    print(sum)
my_function(20)                
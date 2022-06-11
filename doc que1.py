def my_fun(a):
    # l=['abcd', 'xyz', 'aba', '1221']
    c=0
    for i in a:
        if len(i)>=2 and i[0]==i[-1]:
            c+=1
    print(c)
my_fun(['abcd', 'xyz', 'aba', '1221'])
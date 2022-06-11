def pettrn(num):
    if num==0:
        return
    else:
        pettrn(num-1)
        print("*"*num)
num=int(input("row:-"))
pettrn(num)               
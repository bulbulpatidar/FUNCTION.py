def chek_speed(speed):
    if speed<70:
        print("20")
    elif speed>70:
        a=speed-70
        b=a//5
        if b>12:
            print("licences suspend")
        else:
            print(b)
n=int(input("enter the speed:-"))  
chek_speed(n)                  
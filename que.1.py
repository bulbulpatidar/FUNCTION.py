#  My name is Rishabh..
# I am the co-founder of NavGurukul.
# def str():
#     print("my name is rishabh")
#     print("i am the co-founder of navgurukul")
# str()    


# def greet(*names):
#        for name in names:
#            print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender")


# def info(name,age=17):
#    print(name + " is " + age + " years old")

# # info("Sonu")
# info("Sana", "17")
# # info("Umesh", "18")

# def studentDetails(name,currentMilestone,mentorName):
#        print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","pooja")


# def add_num(a,b):
#     # a=12
#     # b=20
#     c=a+b
#     print(c)
# add_num(12,20)
# 
# 
# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")
    
# def primeorNot(num): 
#         if num > 1:
#             for i in range(2,num):
#                 if (num % i) == 0:
#                     print(num,"is not a prime number")
#                     print(i,"times",num//i,"is",num)
#                     break
#                 else:
#                     print(num,"is a prime number")
#         else:
#              print(num,"is not a prime number")
# primeorNot(406)


def greet(**names):
    for name in names:
       print("Hello", name)
greet("sonu", "kartik", "umesh", "bijender")


# def sumofdigits(number):
#      sum = 0
#      modulus = 0
#      while number!=0 :
#        modulus = number%10
#        sum+=modulus
#        number/=10
#        return sum

# print(sumofdigits(123))

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)



# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#      print(s)
#    f2()

# f1()


# def first_function():
#     s = 'I love India'
#     def second_function():
#        print(s) 
#     second_function()
# first_function()


# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)
#     second_function()
#     print(s)
 
# first_function()
# m=[]
# s=[]
# i=1
# while i<=20:
#     s.append(i**2)
#     i+=1
# # print(s)
# a=s[:5]
# b=s[-10:] 
# c=a+b
# print(c)

# l=[2,4,5,6,3,12]
# l1=[8,9,2,10,3]
# sum=0
# m=[]
# for i in l:
#     for j in l1:

#        if i==j:
#         sum+=i
#         sum+=j
# m.append(sum)

# print(m)        


# l=[2,4,5,6,3]
# l1=[8,9,2,10,3]
# sum=0
# m=[]
# for i in l:
#     for j in l1:

#        if i==j:
#         sum+=i+j
#         # sum+=j
# m.append(sum)

# print(m)

#  def calculate_sum(a,b):
#      sum = a+b
#      print(sum)
# calculate_sum(4,5)


# def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(avg)
# Avg(1,3,2)


# def voter(age):
#     if age> 18:
#       print("eligible")
#     else:
#       print("not eligible")
# voter(20)



# def distance(kms):
#    if kms < 20:
#       print("close")
#    elif kms < 50:
#       print("median")
#    else:
#       print("far")
# distance(20)

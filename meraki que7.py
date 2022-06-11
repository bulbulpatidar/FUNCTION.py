# def my_function(a,b):
#      i=0
#      while i<len(a):
#         if len(a)==len(b):
#              print(a)
#              print(b)
#              break
#         elif len(a)>len(b):
#             print(a)
#             break
#         else:
#             print(b)
#             break
#         i+=1
# my_function("hello","welcome")
# my_function("monu","sonu")         

def my_function(a,b):
     i=0
     while i<len(a):
        if len(a)==len(b):
            return a,"\n",b
            # return b
            #  break
        elif len(a)>len(b):
            return a
            # break
        return b
        i+=1
print(my_function("hello","welcome"))
print(my_function("monu","sonu") )  
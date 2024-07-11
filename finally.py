# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
  # print("I am always executed")


# x = func1()
# print(x)

def fun():
    try:
        a = input("enter a value : ")
        print(a)
    except:
        print("some error occurred")
    finally:
        print("I am always executed")
        
print("I am  executed")
y = fun()
print(y)

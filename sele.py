
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

# x = int(input("enter a value of : "))
# match x:
#     case 0:
#         print("hi")
#     case 1:
#         print("how are you")
#     case 2:
#         if x%2 == 0:
#             print("even number broh..")
#     case 3:
#         if x%2 != 0:
#             print("odd number broh..")
#     case _:
#         print("exit")
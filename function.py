#creating define functions

# def calculations(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
#     if(a>b):
#         print("A is big")
#     else:
#         print("B is big")
        
        
# a=int(input("enter a value of A : "))
# b= int(input("enter a value of B : "))
# calculations(a,b)

#pass functions
# def bif(a,b):
#     pass

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def show(a,b,c):
#     average = (a+b+c)/3
#     print(average)
    
# show(2,3,4)

# def show(a=2,b=7, c =3):
#     average = (a+b+c)/3
#     print(average)
    
# show(3,4,5)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print(sum/len(numbers))
        
average(4,6)
    



        
a=int(input("enter a number : "))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
    
b= int(input("enter a value of B : "))
if b>0:
    if b>10 and b<20:
        print("number between 10-20")
    else:
        print("out of range")
else:
    print("B is negative") 
    
# import time
# timestamp = time.strftime('%H:%M:%S') 
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)   
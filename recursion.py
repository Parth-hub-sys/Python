def factorial(n):
    if(n == 0 or n ==1):
        return 1 
    else:
        return n*factorial(n-1)
    
print("Factorial :",factorial(5))


def febonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)
    
print("Febonacci : ",febonacci(4)) 
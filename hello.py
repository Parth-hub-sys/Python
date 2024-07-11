print("hello")

#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  2 to 5 , print Not Weird
#If  is even and in the inclusive range of 6 to 20 , print Weird
#If  is even and greater than 20, print Not Weird

A = int(input("Enter a numberb : "))
if A % 2 == 1:
        print("Weird")
elif A % 2 == 0 and 2 <= A <= 5:
        print("Not Weird")
elif A % 2 == 0 and 6 <= A <= 20:
        print("Weird")
elif A % 2 == 0 and A > 20:
        print("Not Weird")
# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("average is ",sum/len(numbers))
        
# average(4,6,7,2,9)

# list = [ i*i for i in range(4)]
# print(list)

# list = [ i*i for i in range(4) if i%2 == 0]
# print(list)

marks = [3,5,6,"hi","7",6,24,79,4,89]
print(marks)
# print(type(marks))
# print(marks[1])
# print(marks[3])
# print(marks[-3])
# print(marks[len(marks)-3])


if 7 in marks:
    print("yes")
else:
    print("no")
    
if "hi" in marks:
    print("yes")
else:
    print("no")
    
print(marks[1:-1])
print(marks[1:8:2])
# i = int(input("\n Enter a number: "))
# for j in range(i):
#     if j % 2!= 0:  # if j is odd
#         continue  # skip to the next iteration
#     print(j)  # print j if it's even
    
min = int(input("enter a number : "))
for i in range(min):
    if i % 2 == 0:
        continue
    print(i)
    
ni = int(input("ente a number : "))
for i in range(ni):
    if i%2 == 0:
        print(i)
        if i == 10:
            break
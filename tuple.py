tup = (1,45,32,"green",True,56,1,89,5,9)
#tup[0] = 90
print(type(tup),tup)
#tuple value can not change
print(tup[0])
print(tup[1])

# all concept same as a list
if 45 in tup:
    print("yes 45 is in tuple")

tup2 = tup[1:4]
print(tup2)
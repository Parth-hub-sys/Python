# coun = ("india","pak","nepal")
# coun2 = ("aus","eng","china")
# fi = coun + coun2
# print(fi)

# tuple = (0,2,5,1,8,2,7,4,2,90)
# # f = tuple.count(2)
# # f= tuple.index(2)
# f= tuple.index(2,4,8)
# f = len(tuple)
# print(f)

co = ("hi","how","are")
temp = list(co)
temp.append("you")
print(temp)
temp.pop(2)
print(temp)
temp[2] = "buddy"
print(temp)
co = tuple(temp)
print(co)
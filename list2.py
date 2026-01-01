l = [12,45,2,9,4]
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(9))
print(l.count(9))
m = l
m[0] = 0
print(l)
l.insert(2,787)
print(l)

d = [200,534,898]
l.extend(d)
print(l)
k = l + d
print(k)
m = d+ l
print(m)
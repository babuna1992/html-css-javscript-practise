a = input("enter any number: ")
b = str()
c = 0
d = []

for i in range(4):
    b += a
    d.append(b)
print(d)

for i in d:
    c += int(i)
print(c)

a = input('enter numbers :').split(',')
b = []

print(a)
for i in a:
    if len(i)>=4 and int(i)%5==0:
        b.append(i)
print(','.join(b))
x = int(input('enter a number: '))
a = dict()
def mf1(x):
    for i in range(1,x+1):
        a[i] = i * i
    print(a)


mf1(x)

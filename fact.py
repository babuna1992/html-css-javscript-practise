'''
x = int(input("enter a number"))
def fct(x):
    fact = 1
    for i in range(1,x+1):
        fact = (fact * i)
    print(fact)

fct(x)
'''
x = int(input('enter a number: '))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print(fact(x))

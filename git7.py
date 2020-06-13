from math import sqrt # import specific functions as importing all using *
                      # is bad practice

C,H = 50,30
"""
a = input("enter numbers: ")
for i in a:
    d=int(i).split(',')
print(d)
"""

D = [int(i) for i in input().split(',')]
print(D)

"""
items = (input("enter numbers: "))
d = items.split(',')
for i in d:
    print(int(i))
"""

"""    
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

print(",".join(D))
"""

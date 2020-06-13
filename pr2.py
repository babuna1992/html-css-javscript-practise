"""
a = input('enter any word: ').split(" ")
for i in a:
    if a.count(i) > 1:
        a.remove(i)
    a.sort()
    
print(" ".join(a))
"""

b = ['babuna','boy','good','carom','practise','skoda']

print(" ".join(b))
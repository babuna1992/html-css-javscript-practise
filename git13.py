a = input("enter anything: ")
d = {'letter':0,"digit":0}

for i in a:
    if i.isdigit():
        d["digit"]+=1
    elif i.isalpha():
        d["letter"]+= 1
print(d)



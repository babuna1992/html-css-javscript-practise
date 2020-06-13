a = input("enter anything: ")
b = {"uppercase":0,"lowercase":0}
for i in a:
    if i.isupper():
        b["uppercase"] += 1
    elif i.islower():
        b["lowercase"] += 1
    else:
        pass
print(b,"\n***programme finished***")
    
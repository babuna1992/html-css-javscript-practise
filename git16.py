c=[]
a = input().split(',')
for i in a:
    if int(i) % 2 !=0:
        b = str(int(i) * int(i))
        c.append(b)

a=c

print(','.join(a))



        
    
    
    
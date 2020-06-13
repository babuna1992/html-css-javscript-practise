import sys
netamount = 0
while True:
    s = input("Press 'D' for deposite and 'W' for withdraw with exact amount, ex W/D 'amount': ").split()
    if not s:
        break
    oper = s[0]
    amount = s[1]
    if oper == "D":
        netamount = int(amount) + netamount

        print("deposited Rs.", amount)


    elif oper == "W":
        if netamount <= int(amount):
            print('Not enough balance')
        else:
            netamount = netamount - int(amount)
            print("amount deducted Rs.", amount)

    else:
        sys.exit()
print('Total balance is', netamount)




    


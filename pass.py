import re
pas = input("Enter Password: ")
x = True

while x:
    if len(pas) < 3 or len(pas) > 12:
        break
    elif not re.search("[a-z]",pas):
        print("password must containt a lower case letter")
        break
    elif not re.search("[A-Z]",pas):
        print("password must contain a upper case letter")
        break
    elif not re.search("[0-9]",pas):
        print("password must contain a digit")
        break
    elif not re.search("[%$#@^&*_]",pas):
        print("password must contain a special character in between %$#@^&*_")
        break
    elif re.search(r"\s",pas):
        print("password must not containt space")
        break
    else:
        print("valid password is",pas)
        x = False
        break
    




           






import datetime
a = int(input('Type Your DOB Year: '))
def age(a):
    year = datetime.datetime.now()
    b = year.year - a

    print('now your age is: ',b)

    c = a + 100
    print('your age will turn 100 in the year of', c)

age(a)

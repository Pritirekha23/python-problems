# age calculator using python
def ageCal(y,m,d):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age)
ageCal(2003,11,27)



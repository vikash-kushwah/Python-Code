year=int(input("enter year:"))
month=input("enter name of month:")
month1=month.lower()
month_normal_year={"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
month_leap_year={"january":31,"february":29,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
if year%4==0:
    print("number of days in",month,"is",month_normal_year[month1])
else:
    print("number of days in",month,"is",month_leap_year[month1])

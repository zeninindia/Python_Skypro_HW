is_year_leap = input("Введите год :")
year = int(is_year_leap)

if year%4 == 0:
    print("Год",(year), ": True")

else:
    print("Год", (year),": False")

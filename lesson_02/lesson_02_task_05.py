month = int(input("Введите номер месяца:"))
if month < 1:
    print("Ошибка")
elif month == 12 or  month < 3:
    print("Зима")
elif month < 6:
    print("Весна")
elif month < 9:
    print("Лето")
elif month < 12:
    print("Осень")
else:
    print("Ошибка")

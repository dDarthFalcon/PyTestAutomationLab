def month_to_season(monthNumber):
    if (monthNumber >= 3) and (monthNumber <= 5):
        print('Весна')
    elif (monthNumber >= 6) and (monthNumber <= 8):
        print('Лето')
    elif (monthNumber >= 9) and (monthNumber <= 11):
        print('Осень')
    elif (monthNumber == 12) or (monthNumber == 1) or (monthNumber == 2):
        print('Зима')
    else: 
        print('Некорректный номер месяца')

monthNumber = int(input('Введите номер месяца: '))
month_to_season(monthNumber)

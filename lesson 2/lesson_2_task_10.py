def bank ():
    x = float (input('Укажите сумму вклада: '))
    # Начисление происходит в конце года, т.е. если вкладчик закрое вклад досрочно, то проценты по не полному году не начислятся
    y = int (input('Укажите срок вклада (в годах): '))
    # Ставка 10% годовых
    r = 0.1
    # Формула сложного процента
    S = round((x * (1 + r) ** y), 2)
    return S

result = bank ()
print ('Итоговая сумма:', result)
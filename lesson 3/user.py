class User: # Объявляем класс
    def __init__(self, first_name, last_name): # Создаем конструктор
            self.first_name = first_name # объявляем поле "Имя"
            self.last_name = last_name # Объявляем поле "Фамилия"

    def sayFirstName (self): # создан метод, выводящий на экран "Имя" пользователя
          print("Имя:", self.first_name)

    def sayLastName (self): # создан метод, выводящий на экран "Фамилию" пользоватея
          print("Фамилия:", self.last_name)

    def sayFullName (self): # оздан метод, выводящий на экран "Имя" и "Фамилию" пользоватея
          print ("Имя и фамилия:", self.first_name, self.last_name)
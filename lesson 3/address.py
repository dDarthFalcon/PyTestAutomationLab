class Address: # Объявляем класс

    def __init__ (self,index,city,street,building,apartment):  # Конструктор, который принимает 5 параметра: индекс, город, улица, дом, квартира
        self.index = index
        self.city = city
        self.street = street 
        self.building = building
        self.apartment = apartment
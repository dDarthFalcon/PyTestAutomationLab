from smartphone import Smartphone # интегрируем класс

catalog = [] # объявляем список

# пополняем список
catalog.append(Smartphone("Apple", "iPhone 13", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79161234568"))
catalog.append(Smartphone("Google", "Pixel 6", "+79161234569"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79161234570"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79161234571"))

# вывод на экран всего списка 
for phone in catalog:
   print(f"{phone.brand} - {phone.model}. {phone.number}")
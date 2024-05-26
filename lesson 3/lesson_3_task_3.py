from address import Address
from mailing import Mailing

# Создание экземпляров Address для to_address и from_address
to_address = Address("123456", "Москва", "Ленина", "10", "20")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "15", "25")

# Создание экземпляра Mailing
mailing = Mailing(to_address, from_address, 1500, "AB123456789CD")

# Вывод информации об отправлении
print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.building} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.building} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.')

from lesson_03.address import Address
from mailing import Mailing

to_address = Address("234567", "Kaluga", "Karla-Libknehta", "34", "10")
from_address = Address("123456", "Moscow", "123", "25", "3")
cost = 1200
track = "qwe234"

mailing = Mailing(from_address, to_address, cost, track)




print(f"Отправление {mailing.track} из {mailing.from_address.zipcode}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}, {mailing.from_address.apartment} в {mailing.to_address.zipcode}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house}, {mailing.to_address.apartment} . Cтоимость  {mailing.cost} рублей.")


# количество этажей
floors = int(input('Введите количество этажей в здании: '))
# стоимость квартиры на первом этаже
first_floor_price = int(input('Введите цену квартиры на первом этаже: '))
# на сколько возрастает стоимость
price_rising = int(input('Введите сумму на которую возрастает стоимость: '))
# как часто возрастает стоимость, каждые f этажей
price_rising_freq = int(input('Введите как часто возрастает цена(через какое количество этажей): '))


def calc():
    if floors > price_rising_freq:
        price_app = ((first_floor_price + price_rising) * floors) - (price_rising_freq * price_rising)
        total_price = int(first_floor_price + price_app)
        return total_price

    else:
        little_house_price = (first_floor_price * floors)
        return little_house_price


print("\n")
print("От продажи всех квартир будет получено:", calc())

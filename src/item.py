import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, инициализирующий экземпляры класса 'Item' данными из файла 'src/items.csv.
        """
        Item.all = []
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r', newline='\n', encoding='windows- 1251') as file:
            reader = csv.DictReader(file)
            lines = list(reader)
            for line in lines:
                print(cls(name=line.get('name'),
                          price=line.get('price'),
                          quantity=line.get('quantity')))

    @staticmethod
    def string_to_number(name):
        return int(float(name))

    @property
    def name(self):
        """Получаем возможность обращаться к '__name' вне класса"""
        return self.__name

    @name.setter
    def name(self, name):
        """Вносим изменения в '__name'"""
        if len(name) > 10:
            print('Длина наименования товара превышает 10 символов')
        else:
            self.__name = name

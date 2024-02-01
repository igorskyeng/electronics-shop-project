"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

test_name = "Смартфон"
test_price = 10000
test_quantity = 20

Item.pay_rate = 0.5

item = Item(test_name, test_price, test_quantity)


def test_item__init__():
    assert item.name == test_name
    assert item.price == test_price
    assert item.quantity == test_quantity


def test_calculate_total_price():
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item.apply_discount()
    assert item.price == 5000


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10
    assert Item.string_to_number('101.15') == 101


def test_name_setter():
    item.name = '0123456789'
    assert item.name == '0123456789'
    item.name = '0123456789a'
    assert item.name != '0123456789a'


def test_repr():
    item1 = Item("Планшет", 15000, 1)
    assert repr(item1) == "Item('Планшет', 15000, 1)"


def test_str():
    item1 = Item("Планшет", 10000, 20)
    assert str(item1) == 'Планшет'

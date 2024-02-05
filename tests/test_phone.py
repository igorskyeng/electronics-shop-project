from src.phone import Phone
from src.item import Item

test_name = "Phone"
test_price = 10000
test_quantity = 20
test_number_of_sim = 2

Phone.pay_rate = 0.5

phone = Phone(test_name, test_price, test_quantity, test_number_of_sim)


def test_item__init__():
    assert phone.name == test_name
    assert phone.price == test_price
    assert phone.quantity == test_quantity


def test_name_setter():
    phone.name = '0123456789'
    assert phone.name == '0123456789'
    phone.name = '0123456789a'
    assert phone.name != '0123456789a'


def test_repr():
    phone1 = Phone("Phone", 15000, 1, 2)
    assert repr(phone1) == "Phone('Phone', 15000, 1, 2)"


def test_str():
    phone1 = Phone("Phone", 10000, 20, 1)
    assert str(phone1) == 'Phone'


def test_item__add__():
    phone1 = Phone("Phone", 10000, 10, 2)
    item1 = Item("Phone2", 10000, 20)
    assert phone1 + item1 == 30
    assert phone1 + phone1 == 20


def test_number_of_sim_setter():
    phone1 = Phone("Phone", 10000, 10, 2)
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == ValueError

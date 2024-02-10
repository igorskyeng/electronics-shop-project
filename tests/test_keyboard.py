import pytest
from src.keyboard import Keyboard

test_name = "K120 [920-002583]"
test_price = 1399
test_quantity = 20

keyboard = Keyboard(test_name, test_price, test_quantity)


def test_item__init__():
    assert keyboard.name == test_name
    assert keyboard.price == test_price
    assert keyboard.quantity == test_quantity


def test_repr():
    assert repr(keyboard) == "Keyboard('K120 [920-002583]', 1399, 20)"


def test_str():
    print(str(keyboard))
    assert str(keyboard) == 'K120 [920-002583]'


def test_change_lang():
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"

    with pytest.raises(AttributeError):
        keyboard.language = "RU"

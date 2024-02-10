from src.item import Item


class MixinLog:
    """Lополнительный функционал по хранению и изменению раскладки клавиатуры для класса 'Keyboard'."""
    def __init__(self, language="EN"):
        """
        :__language: Атрибут языка клавиатеры.
        """
        self.__language = language

    def change_lang(self):
        """
        Смена языка клавиатуры.
        """
        self.__language = "RU" if self.__language == "EN" else "EN"

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    """Класс для товара “клавиатура”."""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

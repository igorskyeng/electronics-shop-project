from src.item import Item


class MixinLog:
    def __init__(self, language="EN"):
        self.__language = language

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

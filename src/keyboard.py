from src.item import Item


class MixinLog:
    """Additional functionality for storing and changing the keyboard layout for the 'Keyboard' class."""
    def __init__(self, language="EN"):
        """
        :__language: Keyboard language attribute.
        """
        self.__language = language

    def change_lang(self):
        """
        Changing the keyboard language.
        """
        self.__language = "RU" if self.__language == "EN" else "EN"

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    """Class for the product 'keyboard'."""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

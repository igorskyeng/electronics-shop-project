from src.item import Item


class Phone(Item):
    """
    Class for adding a new attribute (SIM card)
    Docstring in English because "main" gives the error "utf-8" if something is written in English in this class
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        """
        Creating an instance of the item class.

        :param name: Product name.
        :param price: Price per item.
        :param quantity: Quantity of goods in the store.
        :param number_of_sim: Number of SIM cards in the phone.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if not isinstance(new_number_of_sim, int) or new_number_of_sim <= 0:
            raise ValueError("The number of physical SIM cards must be an integer greater than zero")
        self.__number_of_sim = new_number_of_sim

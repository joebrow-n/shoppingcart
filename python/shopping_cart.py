from abc import ABC, abstractmethod
from typing import Dict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer):
        self.pricer = pricer
        self._contents: Dict[str,int] = {}

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        if item_type not in self._contents:
            self._contents[item_type] = number
        else:
            self._contents[item_type] = self._contents[item_type] + number

    def print_receipt(self):

        total_cost = 0
        for item_key, item_amount in self._contents.items():
            price = self.pricer.get_price(item_key) * item_amount
            price_string = str(price)
            if price > 99:
                euro = price_string[:-2]
                cent = price_string[-2:]
                price_string = "€{}.{}".format(euro, cent)
            else:
                euro = str(0)
                if price < 10:
                    cent = "0{}".format(price)
                else:
                    cent = price_string
                price_string = "€{}.{}".format(euro, cent)
            print("{item_key} - {item_amount} - {price}".format(item_key = item_key, item_amount = item_amount, price = price_string))
            total_cost += price

        total_cost_string = str(total_cost)
        if total_cost > 99:
            euro = total_cost_string[:-2]
            cent = total_cost_string[-2:]
            total_cost_string = "€{}.{}".format(euro, cent)
        else:
            euro = str(0)
            cent = total_cost_string
            total_cost_string = "€{}.{}".format(euro, cent)
        print("Total cost: {}".format(total_cost_string))
        

class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())

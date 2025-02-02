import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

class ShoppingCartTest(unittest.TestCase):
    def test_print_receipt(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 4)
        sc.print_receipt(3)
        with Capturing() as output:
            sc.print_receipt(3)
        self.assertEqual("apple - 2 - €2.00", output[0])
        self.assertEqual("banana - 4 - €8.00", output[1])

    def test_doesnt_explode_on_mystery_item(self):
        sc = ShoppingCartConcreteCreator().operation()
        sc.add_item("apple", 2)
        sc.add_item("banana", 5)
        sc.add_item("pear", 5)
        with Capturing() as output:
            sc.print_receipt(3)
        self.assertEqual("apple - 2 - €2.00", output[0])
        self.assertEqual("banana - 5 - €10.00", output[1])
        self.assertEqual("pear - 5 - €0.00", output[2])

unittest.main(exit=False)

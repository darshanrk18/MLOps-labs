import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Create a fresh cart for each test."""
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 1.50, 2)
        self.assertEqual(self.cart.get_item_count(), 2)
        self.assertAlmostEqual(self.cart.get_subtotal(), 3.0)

    def test_add_item_default_quantity(self):
        self.cart.add_item("Banana", 0.75)
        self.assertEqual(self.cart.get_item_count(), 1)
        self.assertAlmostEqual(self.cart.get_subtotal(), 0.75)

    def test_add_item_duplicate_increments_quantity(self):
        self.cart.add_item("Orange", 2.0, 1)
        self.cart.add_item("Orange", 2.0, 3)
        self.assertEqual(self.cart.get_item_count(), 4)
        self.assertAlmostEqual(self.cart.get_subtotal(), 8.0)

    def test_remove_item(self):
        self.cart.add_item("Milk", 3.99)
        self.assertTrue(self.cart.remove_item("Milk"))
        self.assertEqual(self.cart.get_item_count(), 0)
        self.assertAlmostEqual(self.cart.get_subtotal(), 0.0)

    def test_remove_item_not_found(self):
        self.assertFalse(self.cart.remove_item("Nonexistent"))

    def test_update_quantity(self):
        self.cart.add_item("Bread", 2.50, 2)
        self.assertTrue(self.cart.update_quantity("Bread", 5))
        self.assertEqual(self.cart.get_item_count(), 5)
        self.assertAlmostEqual(self.cart.get_subtotal(), 12.5)

    def test_update_quantity_to_zero_removes_item(self):
        self.cart.add_item("Eggs", 4.0)
        self.assertTrue(self.cart.update_quantity("Eggs", 0))
        self.assertEqual(self.cart.get_item_count(), 0)

    def test_get_items(self):
        self.cart.add_item("A", 1.0, 2)
        self.cart.add_item("B", 2.0, 1)
        items = self.cart.get_items()
        self.assertEqual(
            items,
            {"A": {"price": 1.0, "quantity": 2}, "B": {"price": 2.0, "quantity": 1}},
        )
        # Ensure we return a copy
        items["A"]["quantity"] = 999
        self.assertEqual(self.cart.get_item_count(), 3)

    def test_clear(self):
        self.cart.add_item("X", 10.0, 3)
        self.cart.clear()
        self.assertEqual(self.cart.get_item_count(), 0)
        self.assertAlmostEqual(self.cart.get_subtotal(), 0.0)
        self.assertEqual(self.cart.get_items(), {})

    def test_add_item_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Item", -5.0)
        self.assertIn("Price must be a non-negative number", str(context.exception))

    def test_add_item_invalid_quantity(self):
        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Item", 1.0, 0)
        self.assertIn("Quantity must be a positive integer", str(context.exception))

    def test_update_quantity_negative(self):
        self.cart.add_item("Item", 1.0)
        with self.assertRaises(ValueError) as context:
            self.cart.update_quantity("Item", -1)
        self.assertIn("Quantity cannot be negative", str(context.exception))


if __name__ == "__main__":
    unittest.main()

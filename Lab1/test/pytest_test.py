import pytest
from src.shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    """Create a fresh cart for each test."""
    return ShoppingCart()


def test_add_item(cart):
    cart.add_item("Apple", 1.50, 2)
    assert cart.get_item_count() == 2
    assert cart.get_subtotal() == 3.0


def test_add_item_default_quantity(cart):
    cart.add_item("Banana", 0.75)
    assert cart.get_item_count() == 1
    assert cart.get_subtotal() == 0.75


def test_add_item_duplicate_increments_quantity(cart):
    cart.add_item("Orange", 2.0, 1)
    cart.add_item("Orange", 2.0, 3)
    assert cart.get_item_count() == 4
    assert cart.get_subtotal() == 8.0


def test_remove_item(cart):
    cart.add_item("Milk", 3.99)
    assert cart.remove_item("Milk") is True
    assert cart.get_item_count() == 0
    assert cart.get_subtotal() == 0.0


def test_remove_item_not_found(cart):
    assert cart.remove_item("Nonexistent") is False


def test_update_quantity(cart):
    cart.add_item("Bread", 2.50, 2)
    assert cart.update_quantity("Bread", 5) is True
    assert cart.get_item_count() == 5
    assert cart.get_subtotal() == 12.5


def test_update_quantity_to_zero_removes_item(cart):
    cart.add_item("Eggs", 4.0)
    assert cart.update_quantity("Eggs", 0) is True
    assert cart.get_item_count() == 0


def test_get_items(cart):
    cart.add_item("A", 1.0, 2)
    cart.add_item("B", 2.0, 1)
    items = cart.get_items()
    assert items == {"A": {"price": 1.0, "quantity": 2}, "B": {"price": 2.0, "quantity": 1}}
    # Ensure we return a copy
    items["A"]["quantity"] = 999
    assert cart.get_item_count() == 3


def test_clear(cart):
    cart.add_item("X", 10.0, 3)
    cart.clear()
    assert cart.get_item_count() == 0
    assert cart.get_subtotal() == 0.0
    assert cart.get_items() == {}


def test_add_item_invalid_price(cart):
    with pytest.raises(ValueError, match="Price must be a non-negative number"):
        cart.add_item("Item", -5.0)


def test_add_item_invalid_quantity(cart):
    with pytest.raises(ValueError, match="Quantity must be a positive integer"):
        cart.add_item("Item", 1.0, 0)


def test_update_quantity_negative(cart):
    cart.add_item("Item", 1.0)
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        cart.update_quantity("Item", -1)

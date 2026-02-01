"""
Shopping Cart application : manages items, quantities, and totals.
"""


class ShoppingCart:
    """A simple shopping cart that tracks items, prices, and quantities."""

    def __init__(self):
        self._items = {}  # name -> {"price": float, "quantity": int}

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Add an item to the cart or update quantity if already present."""
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity must be a positive integer.")
        name = str(name).strip()
        if not name:
            raise ValueError("Item name cannot be empty.")

        if name in self._items:
            self._items[name]["quantity"] += quantity
        else:
            self._items[name] = {"price": float(price), "quantity": quantity}

    def remove_item(self, name: str) -> bool:
        """Remove an item from the cart. Returns True if removed, False if not found."""
        if name in self._items:
            del self._items[name]
            return True
        return False

    def update_quantity(self, name: str, quantity: int) -> bool:
        """Update the quantity of an item. Returns True if updated, False if not found."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if name in self._items:
            if quantity == 0:
                del self._items[name]
            else:
                self._items[name]["quantity"] = quantity
            return True
        return False

    def get_subtotal(self) -> float:
        """Return the total price of all items in the cart."""
        return sum(item["price"] * item["quantity"] for item in self._items.values())

    def get_item_count(self) -> int:
        """Return the total number of items (sum of quantities)."""
        return sum(item["quantity"] for item in self._items.values())

    def get_items(self) -> dict:
        """Return a copy of the items in the cart."""
        return {name: data.copy() for name, data in self._items.items()}

    def clear(self) -> None:
        """Remove all items from the cart."""
        self._items.clear()

"""Простой калькулятор заказа. Тестовый файл без уязвимостей."""

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    quantity: int


def item_total(item: Item) -> float:
    if item.price < 0 or item.quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    return item.price * item.quantity


def order_total(items: list[Item], discount_percent: float = 0) -> float:
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    subtotal = sum(item_total(item) for item in items)
    return round(subtotal * (1 - discount_percent / 100), 2)


def format_receipt(items: list[Item], discount_percent: float = 0) -> str:
    lines = [f"{item.name} x{item.quantity}: {item_total(item):.2f}" for item in items]
    lines.append(f"Total: {order_total(items, discount_percent):.2f}")
    return "\n".join(lines)


if __name__ == "__main__":
    cart = [
        Item("Book", 12.5, 2),
        Item("Pen", 1.2, 5),
    ]
    print(format_receipt(cart, discount_percent=10))

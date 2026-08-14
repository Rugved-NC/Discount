"""discount.py

A small utility to compute the final price after applying a percentage discount.
This version improves readability, adds input validation, and formats the output.
"""
from typing import Optional


def get_float(prompt: str, min_value: Optional[float] = None, max_value: Optional[float] = None) -> float:
    """Prompt the user for a float and validate an optional range.

    Keeps asking until the user provides a valid number within the specified bounds.
    """
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
            continue

        return value


def calculate_final_price(price: float, discount_percent: float) -> float:
    """Return the price after applying a percentage discount.

    Example: price=100, discount_percent=10 -> returns 90.0
    """
    return price * (1 - discount_percent / 100)


def format_currency(amount: float) -> str:
    """Format a number as a currency string with two decimals and thousand separators."""
    return f"${amount:,.2f}"


def main() -> None:
    print("Discount calculator")

    price = get_float("Enter price: ", min_value=0.0)
    discount = get_float("Enter discount % (0-100): ", min_value=0.0, max_value=100.0)

    final_price = calculate_final_price(price, discount)

    print(f"Final price: {format_currency(final_price)}")


if __name__ == "__main__":
    main()

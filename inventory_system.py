"""Inventory management system module."""

import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add quantity to an item in stock."""
    if not item:
        return
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove quantity from an item in stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Get quantity of an item in stock."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load stock data from JSON file."""
    with open(file, "r", encoding="utf-8") as f:
        global stock_data
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """Save stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Print the current stock data."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Check items with quantity below threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # eval removed for security

main()

"""Inventory management system module."""

import json
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    """Add quantity to an item in stock."""
    if not item:
        return
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def removeItem(item, qty):
    """Remove quantity from an item in stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def getQty(item):
    """Get quantity of an item in stock."""
    return stock_data[item]


def loadData(file="inventory.json"):
    """Load stock data from JSON file."""
    with open(file, "r", encoding="utf-8") as f:
        global stock_data
        stock_data = json.loads(f.read())


def saveData(file="inventory.json"):
    """Save stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def printData():
    """Print the current stock data."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def checkLowItems(threshold=5):
    """Check items with quantity below threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # eval removed for security

main()

# Day 15 - Coffee Machine ☕

## Project Overview

This project is a **coffee machine simulation** built in Python as part of my 100 Days of Python challenge.  
It mimics the functionality of a real coffee machine by allowing the user to order drinks, insert coins, and receive either coffee or a refund depending on resources and payment.

The program features:

- A menu with three drinks: **espresso, latte, and cappuccino**
- A system to **track resources** (water, milk, coffee)
- A **coin processor** that simulates inserting quarters, dimes, nickels, and pennies
- A **transaction system** that calculates change and tracks profits
- A **report command** to print the current machine resources
- An **off command** to shut down the machine

---

## How It Works

1. The machine asks: "What would you like?"
2. The user can:

- Type `report` → See current resources and money earned
- Type `off` → Turn off the machine
- Choose a drink → Insert coins for the selected beverage

3. The machine checks if there are **enough resources** for the order.
4. If payment is sufficient, the machine:

- Deducts resources
- Serves the drink
- Adds profit

5. If payment is insufficient, money is refunded.

---

## Skills Demonstrated

- **Dictionaries** for structured data (menu, resources)
- **Functions** for modular design (resource checking, coin processing, transactions, making coffee)
- **While loops** for continuous operation until shutdown
- **Conditional logic** for handling user input and machine states
- **Global variables** for profit tracking

---

## Files Included

- **`main.py`** → Contains the coffee machine program logic

---

## Author

Sanika Surose

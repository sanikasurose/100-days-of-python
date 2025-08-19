# Day 15 - Object-Oriented Coffee Machine ☕  

## Project Overview  

This project is a **coffee machine simulation** implemented using **Object-Oriented Programming (OOP)** in Python as part of my 100 Days of Python challenge.  
The machine allows users to order drinks, insert coins, and receive coffee, while tracking resources and profits using classes.  

The program is structured with three main classes:  

- `CoffeeMaker` → Manages resources, checks if orders can be made, and makes coffee  
- `Menu` → Stores available drinks and their ingredients/costs  
- `MoneyMachine` → Handles coin input, payment validation, and profit tracking  

---

## How It Works  

1. The machine prompts the user: "What would you like? (latte/espresso/cappuccino): "
2. The user can:  
- Type `report` → Display current resources and money earned  
- Type `off` → Turn off the machine  
- Choose a drink → Insert coins to pay for the selected beverage  
3. The program checks:  
- If enough resources are available (`CoffeeMaker.is_resource_sufficient`)  
- If payment is sufficient (`MoneyMachine.make_payment`)  
4. If all conditions are met:  
- Ingredients are deducted from resources  
- Coffee is served  
- Profit is updated  
5. The process repeats until the user turns off the machine.  

---

## Skills Demonstrated  

- **Object-Oriented Programming**: Classes and objects for modular design  
- **Encapsulation**: Each class manages its own data and methods  
- **Functions & Methods**: Reusable functions for coin processing, resource checking, and serving coffee  
- **Conditional Logic**: Handle user input and machine operations  
- **Loops**: Continuous operation until shutdown  
- **Dictionaries**: Store ingredients, coin values, and menu items  

---

## Files Included  

- **`main.py`** → Runs the coffee machine and connects the classes  
- **`coffee_maker.py`** → Contains the `CoffeeMaker` class  
- **`menu.py`** → Contains the `Menu` and `MenuItem` classes  
- **`money_machine.py`** → Contains the `MoneyMachine` class  

---

## Author  

Sanika Surose  


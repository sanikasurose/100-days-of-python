# Day 09 - Secret Auction

## Project Overview

This project is a **text-based Secret Auction Program** implemented in Python as part of my 100 Days of Python challenge.  
It allows multiple users to place bids in a “secret” auction and automatically determines the winner based on the highest bid.

The program features:

- Collecting multiple bidders’ names and bid amounts
- Storing bids in a dictionary with names as keys and bids as values
- Handling multiple rounds of bidding until no more bidders remain
- Comparing all bids to determine the winner
- Displaying a winner announcement at the end of the auction
- ASCII art logo displayed at the start of the program

---

## How to Use

1. Run the `main.py` file.
2. The logo will display.
3. Enter your **name** and **bid amount**.
4. Indicate whether there are other bidders by typing `yes` or `no`.
5. If there are more bidders, repeat steps 3–4 until no more bidders remain.
6. The program will automatically calculate and display the **winner** and their bid.

---

## Skills Learned

During this project, I applied and strengthened the following Python skills:

- **Dictionaries**: Storing bidder names and bids as key-value pairs
- **Loops**: Using a `while` loop to continuously collect bids until the auction ends
- **Conditionals**: `if`/`elif`/`else` statements to check user input and control program flow
- **Functions**: Creating a reusable function to compare dictionary values and find the highest bidder
- **User Input**: Collecting names, bids, and responses from multiple users
- **Printing & Formatting**: Displaying results clearly and in a user-friendly way
- **Boolean Logic**: Using flags (`start`) to control the auction loop and allow dynamic input

---

## Files Included

- `main.py` — the main auction program
- `art.py` — contains ASCII art for the logo

---

## Author

Sanika Surose

# Day 10 - Calculator Program

## Project Overview

This project is a **text-based Calculator Program** implemented in Python as part of my 100 Days of Python challenge.  
It allows the user to perform **basic arithmetic operations** — addition, subtraction, multiplication, and division — on two numbers.

The program features:

- Functions for the four basic operations: `add`, `subtract`, `multiply`, `divide`
- A dictionary (`operations`) that maps operator symbols (`+`, `-`, `*`, `/`) to their corresponding functions
- A reusable `result()` function to calculate and display the user’s answer
- A `while` loop that lets the program run until the user decides to quit
- ASCII art logo displayed at the start of the program

---

## How to Use

1. Run the `main.py` file.
2. The ASCII art logo will display.
3. You’ll be greeted with:
   - A prompt asking if you’d like to start (`Y` or `N`).
   - If you choose `Y`, enter the **first number** and **second number**.
4. Select the desired operation (`+`, `-`, `*`, `/`).
5. The program will calculate and display the **result**.
6. If you choose `N`, the program ends with a thank-you message.

---

## Skills Learned

During this project, I applied and strengthened the following Python skills:

- **Functions**: Writing reusable functions for each operation and for displaying results
- **Dictionaries**: Mapping operator symbols to functions for cleaner and more dynamic code
- **Loops**: Using a `while` loop to keep the program running until the user decides to stop
- **Conditionals**: Handling user input (`Y` or `N`) to control program flow
- **User Input**: Collecting numbers and operation choices from the user
- **Printing & Formatting**: Clearly displaying results in a user-friendly format
- **Boolean Logic**: Using a program control flag (`program_over`) to stop or continue the loop

---

## Files Included

- `main.py` — the main calculator program
- `art.py` — contains ASCII art for the logo

---

## Author

Sanika Surose

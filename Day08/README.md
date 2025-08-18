# Day 08 - The Caesar Cipher Program

## Project Overview

This project is a **text-based Caesar Cipher** implemented in Python as part of my 100 Days of Python challenge.  
It allows the user to **encode** and **decode** messages by shifting letters forwards or backwards in the alphabet.

The program features:

- Encoding messages with a user-specified shift number
- Decoding messages to retrieve the original text
- Handling spaces, symbols, and numbers without altering them
- A restartable loop, so users can encode/decode multiple messages in one session
- ASCII art logo displayed at the start of the program

---

## How to Use

1. Run the `main.py` file.
2. The logo will display.
3. Choose whether to **start** the program or **quit**.
4. Select `encode` to encrypt a message or `decode` to decrypt a message.
5. Enter your message and the shift number.
6. The program will display the resulting text.
7. You can repeat the process until you decide to quit.

---

## Skills Learned

During this project, I applied and strengthened the following Python skills:

- **Functions**: Creating reusable functions with multiple parameters
- **Loops**: `for` loops for iterating through each character in a string
- **Conditionals**: `if`/`elif`/`else` statements to handle encode/decode logic and non-alphabet characters
- **Lists**: Using lists to represent the alphabet and calculate shifted positions
- **Strings**: Concatenating letters to build the encoded/decoded message
- **Modulo Arithmetic**: Handling wrap-around of letters in the alphabet
- **User Input**: Collecting and validating input with `input()`
- **Boolean Logic**: Using flags (`start`) to control program flow and allow restart
- **Modules and Imports**: Importing ASCII art and external variables from `art.py`

---

## Files Included

- `main.py` — the main cipher program
- `art.py` — contains ASCII art for the logo

---

## Author

Sanika Surose

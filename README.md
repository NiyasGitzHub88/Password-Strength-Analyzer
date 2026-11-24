# Password Strength Analyzer

A beginner-friendly Python project for the Thiranex cybersecurity internship task.

## Project objective

This program evaluates a user-entered password using basic checks and provides suggestions to improve it. It also demonstrates how Python's `secrets` module can generate a random password.

## Features

- Checks whether the password has at least 8 characters.
- Gives an additional point for 12 or more characters.
- Checks for uppercase letters, lowercase letters, digits, and special characters.
- Displays a basic strength category: Weak, Medium, or Strong.
- Suggests improvements.
- Generates a random 16-character example password using Python's `secrets` module.

## Requirements

- Python 3
- No third-party packages are required.

## How to run

1. Download or clone this repository.
2. Open `password_strength_analyzer.py` in Python IDLE or another Python editor.
3. Run the file.
4. Enter a fictional password when prompted.

You can also run it from a terminal:

```bash
python password_strength_analyzer.py
```

## Example test cases

| Test input | Expected category |
|---|---|
| `hello` | Weak |
| `hello123` | Medium |
| `Hello123` | Medium |
| `Hello@123456` | Strong |

The result is based on a simple educational scoring rule, not a guarantee that a password is secure.

## Security and privacy note

- This program analyzes the password locally.
- It does not save, log, or transmit the entered password.
- Use fictional passwords for demonstrations. Never enter a real account password into a learning project.
- The generated password is an example. Store real passwords in a reputable password manager.

## Project structure

```text
Password-Strength-Analyzer/
├── password_strength_analyzer.py
├── README.md
└── screenshots/
```

## Concepts demonstrated

- Python functions
- Conditional statements
- Loops
- String methods
- Sets
- The `string` module
- Secure random selection with the `secrets` module

## Author

Add your name and internship details here before submitting.

# INF 360 Python Coursework Portfolio

## Overview

This repository contains Python coursework projects for INF 360 - Programming in Python. The folder includes several assignments that demonstrate core Python skills, including input/output, variables, arithmetic operators, conditionals, loops, lists, dictionaries, functions, file handling, regular expressions, object-oriented programming, error handling, and logging.

Each project is stored in its own folder and can be run from the command line.

## Folder Structure

```text
Python/
├── README.md
├── proj1/
│   └── danielObazeePrj1.py
├── proj2/
│   └── danbaz_proj2.py
├── proj3/
│   ├── danielObazeeprj3.py
│   └── Screenshot files
├── proj4/
│   ├── danielObazeeproj4.py
│   ├── story.txt
│   └── mystory.txt
├── midtermProj/
│   └── midtermproj.py
└── final_project/
    ├── README.md
    ├── data.py
    ├── main.py
    └── quiz_box.py
```

## Projects

## Project 1: Python Basics

Folder:

```text
proj1/
```

Main file:

```text
proj1/danielObazeePrj1.py
```

This assignment introduces basic Python programming concepts. The program asks the user for their name, displays a welcome message, calculates the length of the name, and then asks for two numbers to demonstrate mathematical operations.

Key concepts used:

- `print()` statements
- `input()` statements
- String concatenation
- Type conversion with `int()` and `str()`
- Basic arithmetic operators
- Multiplication
- Addition
- Modulus/remainder calculations

Run command:

```bash
python3 proj1/danielObazeePrj1.py
```

## Project 2: Treasure Door Challenge

Folder:

```text
proj2/
```

Main file:

```text
proj2/danbaz_proj2.py
```

This assignment is an interactive text-based game. The user chooses one of three doors and receives a different result depending on the choice. The program also uses random events to determine whether the player loses, escapes safely, or gains a magical item.

After the game loop ends, the program prints a list of randomly selected treasures.

Key concepts used:

- `while` loops
- `if`, `elif`, and `else` statements
- `break` and `continue`
- Boolean and comparison logic
- Random number generation with `random.randint()`
- Random list selection with `random.choice()`
- Lists
- `for` loops

Run command:

```bash
python3 proj2/danbaz_proj2.py
```

## Project 3: Ford Vehicle Data

Folder:

```text
proj3/
```

Main file:

```text
proj3/danielObazeeprj3.py
```

This assignment stores information about Ford vehicle models using dictionaries. Each vehicle has details such as name, year introduced, current model production year, generation, and vehicle information.

The program converts a list of vehicle dictionaries into a dictionary keyed by vehicle name, prints the vehicle names alphabetically, and prints the vehicles sorted by year introduced.

Key concepts used:

- Dictionaries
- Lists of dictionaries
- Functions
- Sorting with `sorted()`
- Building a dictionary from a list
- Iterating through dictionary keys and values
- Tuples used for sorting by year
- Formatted output

roj3/danielObazeeprj3.py
```

## Project 4: Sherlock Text Processing

Folder:

```text
proj4/
```

Main file:

```text
proj4/danielObazeeproj4.py
```

Supporting files:

```text
proj4/story.txt
proj4/mystory.txt
```

This assignment reads a text file, processes the contents, replaces occurrences of `Sherlock Holmes` with `Daniel Obazee`, counts occurrences of the word `the`, and writes the modified story to a new output file.

Key concepts used:

- File reading
- File writing
- Relative paths
- Regular expressions with the `re` module
- `re.subn()` for replacement and replacement counts
- `re.findall()` for word counting
- Case-insensitive matching
- Formatted strings

Important note:

Because this script uses relative paths, run it from inside the `proj4` folder:

```bash
cd proj4
python3 danielObazeeproj4.py
```

The script reads `story.txt` and writes the processed result to `mystory.txt`.

## Midterm Project: Freelance Portfolio & Earnings Manager

Folder:

```text
midtermProj/
```

Main file:

```text
midtermProj/midtermproj.py
```

The midterm project is a command-line freelance portfolio and earnings manager. It tracks clients, hourly rates, and hours worked. The user can view a portfolio summary, add or update a client, add new hours, and quit the program through a menu-driven interface.

Key features:

- View current client portfolio
- Calculate earnings per client
- Calculate total portfolio value
- Add a new client
- Update an existing client
- Add hours to a client
- Validate numeric input
- Handle invalid menu choices

Key concepts used:

- Dictionaries
- Lists as dictionary values
- Functions
- Menu loops
- `while True`
- User input validation
- `try`/`except` error handling
- Floating-point calculations
- Formatted currency output

Run command:

```bash
python3 midtermProj/midtermproj.py
```

## Final Project: Computer Science Quiz App

Folder:

```text
final_project/
```

Main file:

```text
final_project/main.py
```

Supporting files:

```text
final_project/data.py
final_project/quiz_box.py
final_project/README.md
```

The final project is a command-line True/False quiz application focused on computer science questions. It asks the user a series of questions, validates answers, checks correctness, tracks the score, and displays a final score when the quiz ends.

Key features:

- True/False quiz interface
- Computer science question data
- Score tracking
- Final score display
- Input validation
- Error handling
- Logging
- Object-oriented structure
- Separate files for data, logic, and main program flow

Key concepts used:

- Classes
- Objects
- Lists of dictionaries
- Modular imports
- `try`/`except` blocks
- Input validation loops
- Logging with Python's `logging` module
- Program entry point with `if __name__ == "__main__"`







## Skills Demonstrated

Across the full folder, the coursework demonstrates:

- Basic Python syntax
- Console input and output
- Variables and type conversion
- Arithmetic operations
- Conditional logic
- Loops
- Lists
- Dictionaries
- Functions
- File handling
- Regular expressions
- Randomization
- Object-oriented programming
- Error handling
- Logging
- Modular program organization

## Generated Files

Python may create `__pycache__` folders when programs are run. These folders contain compiled Python cache files and are not part of the source code.

Generated cache folders should usually be excluded from commits with a `.gitignore` entry such as:

```text
__pycache__/
*.pyc
```

## Author

Daniel Obazee

INF 360 - Programming in Python

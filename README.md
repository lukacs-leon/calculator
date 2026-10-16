Modular Calculator

A modular calculator written in Python, designed to support replaceable mathematical engines.

Features

* Addition, subtraction, multiplication, and division
* Division-by-zero handling
* Modular architecture
* Replaceable mathematical engines
* Automated unit tests
* No external dependencies

Requirements

* Python 3.10 or newer

Project Structure

calculator/
├── calculator/
│   ├── __init__.py
│   ├── constants.py
│   ├── main.py
│   ├── operations.py
│   └── engines/
│       ├── __init__.py
│       ├── base.py
│       └── native.py
├── tests/
│   ├── __init__.py
│   ├── test_engines.py
│   └── test_operations.py
├── .gitignore
└── README.md

Run the Calculator

Run the following command from the project root:

python3 -m calculator.main

Run the Tests

Run all unit tests with:

python3 -m unittest discover -s tests -v

Architecture

calculator/engines/base.py

Defines the abstract MathEngine interface. Every mathematical engine must implement its operations.

calculator/engines/native.py

Implements the interface using Python’s built-in arithmetic operations.

calculator/operations.py

Provides a stable interface between the application and the mathematical engine. The engine can be replaced without changing how the application calls mathematical operations.

calculator/main.py

Contains the command-line interface and handles user input.

calculator/constants.py

Stores shared application constants, such as the application name and version.

Extensibility

The project separates the mathematical engine from the application logic.

Future engines can implement the MathEngine interface and be passed to the Operations class. This allows the calculation backend to change without requiring changes to the main application.

License

No license has been specified yet.
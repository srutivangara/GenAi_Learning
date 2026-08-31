# Python Modules and Packages Assignment

## Overview
This assignment demonstrates the concepts of **Python Modules** and **Packages** by creating custom modules, organizing them into a package, and importing them in different ways.

---

## Project Structure

```
project/
│── main.py
│── math_utils.py
│── string_utils.py
│
└── shop_package/
    │── __init__.py
    │── discount.py
    └── billing.py
```

---

## Task 1: math_utils.py

Created a module containing the following functions:
- `add(a, b)` – Returns the sum of two numbers.
- `subtract(a, b)` – Returns the difference of two numbers.
- `square(n)` – Returns the square of a number.

The module was imported in two different ways:
- `import math_utils`
- `from math_utils import square`

---

## Task 2: string_utils.py

Created a module containing:
- `capitalize_words(text)` – Capitalizes each word in a string.
- `reverse_string(text)` – Returns the reversed string.
- `word_count(text)` – Returns the number of words in the string.

All functions were imported and tested in `main.py`.

---

## Task 3: shop_package

Created a package named **shop_package** with the following modules:

### discount.py
- `apply_discount(price, percent)` – Returns the discounted price.
- `flat_discount(price)` – Subtracts ₹50 from the given price.

### billing.py
- `calculate_total(prices)` – Returns the sum of all prices.
- `apply_tax(amount)` – Adds 5% tax to the amount.

### __init__.py
Used to initialize the package and optionally import package functions.

---

## Task 4: Package Import

Imported the package in `main.py` using:

```python
import shop_package.discount as disc
from shop_package.billing import calculate_total
```

Tested all package functions successfully.

---

## How to Run

1. Place all files in the project folder.
2. Open the folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

---

## Technologies Used

- Python 3.x
- VS Code
- Python Modules
- Python Packages

---

## Learning Outcomes

- Learned how to create custom modules.
- Understood different ways of importing modules.
- Learned how to create and use Python packages.
- Improved code organization using modular programming.

---

## Author

**Sruti Vangara**  
B.Tech CSE (AI & ML)  
Gayatri Vidya Parishad College of Engineering for Women (GVPCEW)
````

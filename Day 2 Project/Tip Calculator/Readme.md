# Day 2: Beginner – Understanding Data Types & String Manipulation  
**Project:** Tip Calculator

## 📋 Key Concepts Learned

### Python Data Types

- **String (`str`)**: Represents textual data, e.g., `"Hello"`, `"123"`.
- **Integer (`int`)**: Whole numbers, e.g., `1`, `42`.
- **Float (`float`)**: Numbers with decimals, e.g., `3.14`, `2.0`.
- **Boolean (`bool`)**: Logical values, `True` or `False`.

#### How to Check Data Types

```python
print(type("hello"))     # 
print(type(123))         # 
print(type(2.5))         # 
print(type(True))        # 
```

### Working with User Input

- **Getting user input:** `input("Prompt message")`
  - Always returns a string.
- **Converting between types:** Use `int()`, `float()`, and `str()` for type conversion as needed.

```python
user_number = input("Enter a number:")
as_integer = int(user_number)
as_float = float(user_number)
as_string =str(user_name)
as_bool = bool(user_number)
```

### String Manipulation

- **Concatenation:** Use `+` to join strings.
- **Indexing:** Access characters with `[]`.
- **Slicing:** Extract substrings, e.g., `text[1:4]`.
- **Useful string methods:**
  - `.upper()`, `.lower()`, `.strip()`, `.replace()`
- **String interpolation:** Use f-strings for formatted output.
  
```python
name = "Sam"
print(name.upper())  # SAM
age = 21
print(f"My age is {age}")
```

### Mathematical Operations & Number Manipulation

- Standard operators: `+`, `-`, `*`, `/`, `**`, and `%`.
- **Order of operations:** Follows PEMDAS/BODMAS.

### Rounding Numbers

- Use `round(number, digits)` for formatting output to a set number of decimal places.

### f-Strings and Formatting

- Embed expressions inside strings easily:

```python
score = 99
print(f"Your score is {score}")
```

## 💡 Project: Tip Calculator

### Project Overview
The Tip Calculator project is designed to practice working with data types and string manipulation by creating a program that:

- Takes user inputs for the total bill amount.
- Asks for the tip percentage the user wants to give.
- Requests the number of people splitting the bill.

### Project Goals
- Calculate the total bill including the tip.
- Divide the total bill evenly among the number of people.
- Display the amount each person needs to pay, rounded to two decimal places.

### Skills Practiced
- Taking and converting user input.
- Performing arithmetic calculations.
- Applying formatting to numeric output.
- Using data types effectively.

## 📝 Summary Table: Skills Practiced

| Concept                 | Example/Usage              | Note                                  |
|-------------------------|----------------------------|---------------------------------------|
| Data types              | `type(variable)`           | Strings, ints, floats, bools          |
| Casting types           | `int()`, `float()`, `str()`| Needed after user input or calculations|
| String concatenation    | `"Hello" + "World"`        | Combine text                          |
| String methods          | `.upper()`, `.lower()`     | Format and clean up strings           |
| f-strings               | `f"Value: {x}"`            | Modern, readable formatting           |
| Arithmetic operators    | `+`, `-`, `*`, `/`, `**`   | For calculations                      |
| Rounding numbers        | `round(num, 2)`            | Helpful for currency/money            |


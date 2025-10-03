# 📘 Python Notes — Day 3: Conditionals & Choose-Your-Own-Adventure

This section expands on **Conditionals, Logical Operators, Code Blocks, Scope, and Namespaces** with explanations and practical examples.

---

## 🔹 Conditional Statements

Conditionals let programs make **decisions** based on certain conditions.

### Syntax

```python
if condition:
    # code runs if condition is True
elif another_condition:
    # runs if first condition was False, but this is True
else:
    # runs if none of the above are True
```

### Example

```python
age = 18
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

Output:

```
Teenager
```

---

## 🔹 Logical Operators

Logical operators combine conditions.

* `and` → True if **both** are True
* `or` → True if **at least one** is True
* `not` → Inverts the result

### Example

```python
has_ticket = True
has_id = False

if has_ticket and has_id:
    print("You may enter.")
else:
    print("Access denied.")
```

Output:

```
Access denied.
```

```python
is_raining = True
umbrella = False

if is_raining and not umbrella:
    print("You’ll get wet!")
```

---

## 🔹 Code Blocks & Indentation

In Python, **indentation** defines a code block. Consistency is key (usually 4 spaces).

### Example

```python
if True:
    print("This line is inside the block")
    print("Still inside block")

print("Outside block")
```

---

## 🔹 Scope (Local vs Global)

Scope decides **where a variable can be accessed**.

* **Local scope**: Inside a function
* **Global scope**: Declared outside any function

### Example

```python
x = 10  # global variable

def func():
    x = 5  # local variable
    print("Inside function:", x)

func()
print("Outside function:", x)
```

Output:

```
Inside function: 5
Outside function: 10
```

If you want to modify a global variable inside a function, use `global` keyword:

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

---

## 🔹 Namespaces

A **namespace** is a mapping of names (variables, functions) to objects.

* **Built-in namespace** → Python keywords & functions (`print`, `len`, etc.)
* **Global namespace** → variables declared at top-level of a script
* **Local namespace** → variables inside a function

### Example

```python
x = 10  # global namespace

def my_func():
    y = 5  # local namespace
    print("Local y:", y)

my_func()
print("Global x:", x)
```

---

## 🔹 Mini Project: Choose-Your-Own-Adventure Game

This simple text-based game shows how conditionals drive branching storylines.

```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive unharmed. There’s a house with 3 doors: red, blue, yellow. Which color? ").lower()
        if choice3 == "yellow":
            print("You found the treasure! 🎉")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You were attacked by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
```

---

✅ With this, you now understand **conditionals, logical operators, indentation, scope, and namespaces** — and how they combine to create interactive programs.

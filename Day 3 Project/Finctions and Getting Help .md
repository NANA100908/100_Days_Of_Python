## 📘 Notes: *“Functions and Getting Help”* (from Colin Morris, Kaggle)

### 1. Functions — What & Why

* A **function** is a reusable block of code that can take inputs (parameters) and return outputs.

* They help you **organize**, **abstract**, **reuse**, and **modularize** code.

* You define a function using `def` in Python:

  ```python
  def function_name(param1, param2):
      """
      (optional) docstring explaining what this does,
      what params are, and return value.
      """
      # body
      result = param1 + param2
      return result
  ```

* Benefits:

  * Avoid repeated code
  * Easier to maintain & test
  * You can think at a higher level (call `compute_score()` instead of rewriting logic)

---

### 2. Function Signatures, Default Arguments & Keyword Arguments

* **Positional arguments**: You pass parameters in a fixed order
* **Default arguments**: You can give parameters default values, so caller can skip them

  ```python
  def greet(name, msg="Hello"):
      print(f"{msg}, {name}")
  ```
* **Keyword arguments**: You can pass by name, e.g. `greet(msg="Hi", name="Alice")`
* You can mix positional + default + `*args`, `**kwargs` in advanced designs
* Use **keyword-only** parameters if needed (Python 3 syntax)

---

### 3. Docstrings & Getting Help

* You should include docstrings (using triple quotes `""" … """`) in your functions: explains what it does, parameters, return, side effects.
* You can access help via:

  * `help(function_name)` in interactive interpreter
  * `function_name?` in Jupyter / IPython
  * Auto-documentation tools can parse docstrings (like Sphinx, etc.)

---

### 4. Nested / Inner Functions & Closures

* You can define a function inside another function.
* The inner function can “capture” variables from the outer function (a closure).
* Use case: customizing behavior, factories, decorators, etc.

---

### 5. Lambda / Anonymous Functions

* Use `lambda` for small, throwaway functions:

  ```python
  f = lambda x, y: x + y
  ```
* But they’re limited: single expression only, no statements, less readable for complex logic. Use named functions for clarity.

---

### 6. Higher-Order Functions & Passing Functions Around

* Functions are first-class citizens in Python: you can pass them as arguments, return them, store in data structures.
* Common patterns: mapping, filtering, callbacks, decorators.

---

### 7. Getting Help & Introspection

* You can introspect a function:

  * `function_name.__doc__` → its docstring
  * `dir(function_name)` → its attributes
  * `inspect` module: `inspect.signature`, `inspect.getsource`, etc.
* Useful to debug, explore APIs, or generate docs.

---

### 8. Good Practices

* Keep functions **short and single-purpose**
* Name them clearly
* Use meaningful parameter names
* Document side effects, expected types, return values
* Avoid deep nesting; break into helpers if needed



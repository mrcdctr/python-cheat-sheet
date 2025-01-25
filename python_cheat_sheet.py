# Create a new PDF with more comprehensive examples
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", size=16, style="B")
pdf.cell(0, 10, "Comprehensive Python Cheat Sheet with Examples", ln=True, align="C")
pdf.ln(10)

# Add Sections with Examples
sections_with_examples = {
    "1. Variables and Data Types": """
- Integer: x = 10
- Float: pi = 3.14
- String: greeting = "Hello, World!"
- Boolean: is_active = True
- List: colors = ["red", "green", "blue"]
- Tuple: point = (5, 10)
- Dictionary: student = {"name": "Alice", "age": 25}
- Set: unique_numbers = {1, 2, 3, 4}
""",
    "Example:":
"""
x = 10
greeting = "Hello, World!"
colors = ["red", "green", "blue"]
print(f"Integer: {x}, Greeting: {greeting}, Colors: {colors}")
""",
    "2. Arithmetic and Logical Operations": """
- Addition: a + b
- Subtraction: a - b
- Multiplication: a * b
- Division: a / b
- Floor Division: a // b
- Modulus: a % b
- Exponentiation: a ** b
- Logical: and, or, not
""",
    "Example:":
"""
a, b = 10, 3
print(f"Sum: {a + b}, Product: {a * b}, Power: {a ** b}")
if a > b and b > 0:
    print("Both conditions are True")
""",
    "3. Conditional Statements": """
if condition:
    # Code block
elif another_condition:
    # Another block
else:
    # Default block
""",
    "Example:":
"""
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 10")
""",
    "4. Loops": """
- For Loop:
for item in iterable:
    # Code block

- While Loop:
while condition:
    # Code block
""",
    "Example:":
"""
# For Loop
for i in range(5):
    print(f"Iteration {i}")

# While Loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
""",
    "5. Functions": """
def function_name(parameters):
    # Code block
    return value
""",
    "Example:":
"""
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
""",
    "6. Classes and Objects": """
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

obj = MyClass("Python")
print(obj.greet())
""",
    "7. File Handling": """
- Reading a File:
with open("file.txt", "r") as file:
    content = file.read()

- Writing to a File:
with open("file.txt", "w") as file:
    file.write("Hello, World!")
""",
    "Example:":
"""
with open("example.txt", "w") as file:
    file.write("This is a test.")

with open("example.txt", "r") as file:
    print(file.read())
""",
    "8. Common Libraries": """
- NumPy: import numpy as np
- Pandas: import pandas as pd
- Matplotlib: import matplotlib.pyplot as plt
- Requests: import requests
""",
    "Example:":
"""
import numpy as np
arr = np.array([1, 2, 3])
print(f"Numpy Array: {arr}")
""",
    "9. List Comprehensions": """
- Syntax: [expression for item in iterable if condition]
""",
    "Example:":
"""
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")
""",
    "10. Error Handling": """
try:
    # Code block that may raise an exception
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code")
""",
    "Example:":
"""
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Execution complete.")
"""
}

# Add sections and examples to PDF
for section, content in sections_with_examples.items():
    if section.endswith("Example:"):
        pdf.set_font("Arial", style="I", size=11)
    else:
        pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, section, ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, content)
    pdf.ln(5)

# Save PDF with Examples
file_path_with_examples = "/mnt/data/Comprehensive_Python_Cheat_Sheet.pdf"
pdf.output(file_path_with_examples)

file_path_with_examples

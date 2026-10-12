"""
Lesson 01 - Python Basics (data types, variables, operators, built-ins)
=======================================================================

Run this file:   python lessons/01_basics.py

This lesson is a cleaned-up, fully explained version of what is in main.py.
Read the comments top to bottom, run the file, and compare the printed output
with what you expected.
"""


def section(title):
    """Print a header so the output is easy to follow."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. DATA TYPES
# ---------------------------------------------------------------------------
# Every value in Python has a *type*. The type decides what you can do with it.
#
#   int    -> whole numbers           5, -3, 1000
#   float  -> decimal numbers         3.14, -0.5, 2.0
#   bool   -> True / False            True, False
#   str    -> text                    "hello", 'hi'
#   list   -> ordered, changeable     [1, 2, 3]
#   tuple  -> ordered, NOT changeable (1, 2, 3)
#   set    -> unordered, unique items {1, 2, 3}
#   dict   -> key -> value pairs      {"name": "Sam", "age": 22}
#   None   -> "nothing / no value"
section("1. Data types")

examples = [5, 3.14, True, "hello", [1, 2], (1, 2), {1, 2}, {"a": 1}, None]
for value in examples:
    # type() tells you the type of any value
    print(f"{value!r:<15} -> {type(value).__name__}")


# ---------------------------------------------------------------------------
# 2. VARIABLES
# ---------------------------------------------------------------------------
# A variable is a *name* that points to a value. You create one with "=".
# Rules for names:
#   - letters, numbers and _ only, cannot start with a number
#   - case sensitive: my_age and my_Age are DIFFERENT names
#   - use snake_case for normal variables (user_name, total_price)
#   - use UPPER_CASE for constants you promise not to change (PI = 3.14)
section("2. Variables")

user_name = "John Doe"
my_age = 25
PI = 3.14  # constant - Python won't stop you changing it, it's a convention

print(user_name, my_age, PI)

# Multiple assignment in one line
a, b = 5, 10
print("a =", a, "b =", b)

# Swap two variables (a classic Python trick - no temp variable needed)
a, b = b, a
print("after swap: a =", a, "b =", b)


# ---------------------------------------------------------------------------
# 3. MATH OPERATORS
# ---------------------------------------------------------------------------
section("3. Math operators")

x, y = 17, 5
print("x + y  =", x + y)    # addition        -> 22
print("x - y  =", x - y)    # subtraction     -> 12
print("x * y  =", x * y)    # multiplication  -> 85
print("x / y  =", x / y)    # division        -> 3.4   (ALWAYS gives a float)
print("x // y =", x // y)   # floor division  -> 3     (drops the decimal part)
print("x % y  =", x % y)    # modulo          -> 2     (the remainder)
print("x ** y =", x ** y)   # power           -> 1419857

# Tip: % is very useful to check even / odd numbers
for n in [4, 7]:
    print(n, "is even" if n % 2 == 0 else "is odd")

# Augmented assignment: shorter way to update a variable
total = 10
total += 5   # same as total = total + 5   -> 15
total -= 3   # same as total = total - 3   -> 12
total *= 2   # same as total = total * 2   -> 24
print("total =", total)


# ---------------------------------------------------------------------------
# 4. STRINGS
# ---------------------------------------------------------------------------
section("4. Strings")

greeting = "Hello World"

# + joins strings, * repeats them
print("Hi" + " " + "there")
print("ha" * 3)

# Careful! "1234" + "5678" joins text, it does NOT add numbers
print("'1234' + '5678' =", "1234" + "5678")
print("int('1234') + int('5678') =", int("1234") + int("5678"))

# Indexing: each character has a position starting at 0
#   H  e  l  l  o     W  o  r  l  d
#   0  1  2  3  4  5  6  7  8  9  10
print("greeting[0]  =", greeting[0])     # first character
print("greeting[-1] =", greeting[-1])    # last character (negative = from end)

# Slicing: text[start:stop:step]  (stop is NOT included)
print("greeting[0:5] =", greeting[0:5])  # 'Hello'
print("greeting[6:]  =", greeting[6:])   # 'World'
print("greeting[::-1] =", greeting[::-1])  # reversed!

# String methods - functions that belong to a string.
# Strings are IMMUTABLE: methods return a NEW string, the original is unchanged.
messy = "   python is FUN   "
print(repr(messy.strip()))        # remove spaces at both ends
print(messy.upper())              # ALL CAPS
print(messy.lower())              # all lower
print(messy.strip().title())      # Every Word Capitalised
print(messy.strip().capitalize()) # Only first letter capitalised
print(messy.replace("FUN", "awesome"))
print("python" in messy)          # True - check if text contains something
print("a,b,c".split(","))         # split text into a list -> ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))  # join a list into text -> 'a-b-c'

# f-strings: the easiest way to put variables inside text
name, age = "Sam", 22
print(f"My name is {name} and next year I will be {age + 1}.")
print(f"PI to 1 decimal place: {PI:.1f}")


# ---------------------------------------------------------------------------
# 5. TYPE CONVERSION (casting)
# ---------------------------------------------------------------------------
section("5. Type conversion")

print(int("42"), type(int("42")))
print(float("3.5"), type(float("3.5")))
print(str(12), type(str(12)))
print(int(9.99))   # int() cuts off the decimal, it does NOT round -> 9
print(round(9.99)) # use round() to round -> 10


# ---------------------------------------------------------------------------
# 6. BOOLEANS and "truthiness"
# ---------------------------------------------------------------------------
# Comparisons give True or False:  ==  !=  <  >  <=  >=
# Combine them with: and, or, not
section("6. Booleans")

print("5 > 3        ->", 5 > 3)
print("5 == 5.0     ->", 5 == 5.0)
print("'a' != 'b'   ->", "a" != "b")
print("True and False ->", True and False)
print("True or False  ->", True or False)
print("not True       ->", not True)

# Every value can be treated as True or False.
# "Empty" or "zero" things are False; everything else is True.
for value in [0, 1, "", "Hello", [], [1, 2, 3], None]:
    print(f"bool({value!r}) = {bool(value)}")

# This is why you can write:  if my_list:   instead of   if len(my_list) > 0:
shopping = ["milk"]
if shopping:
    print("We still need to buy:", shopping)


# ---------------------------------------------------------------------------
# 7. USEFUL BUILT-IN FUNCTIONS
# ---------------------------------------------------------------------------
section("7. Built-in functions")

numbers = [4, 1, 9, 7]
print("len  :", len(numbers))      # how many items
print("min  :", min(numbers))
print("max  :", max(numbers))
print("sum  :", sum(numbers))
print("sorted:", sorted(numbers))  # returns a NEW sorted list
print("abs(-5):", abs(-5))
print("type(3.0):", type(3.0))
# help(str)  <- uncomment to read the manual for any type or function
# dir(str)   <- lists every method a type has


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Make variables for your name and birth year, then print
#    "<name> is <age> years old" using an f-string.
# 2. Given  sentence = "  learning PYTHON is cool  "
#    print it stripped, in title case, and count how many times "o" appears
#    (hint: the .count() method).
# 3. Convert the string "3.75" to a float, multiply by 4, and print the result
#    as an int.
# 4. Use % to print all numbers from 1 to 20 that are divisible by 3.

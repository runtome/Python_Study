"""
Lesson 06 - Functions
=====================

Run this file:   python lessons/06_functions.py

A FUNCTION is a named, reusable block of code.
   def name(parameters):
       ...body...
       return result

Why use functions?
  - Don't Repeat Yourself (DRY): write once, use many times
  - Give a NAME to an idea, which makes code easier to read
  - Easier to test and fix one small piece at a time
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. DEFINING AND CALLING
# ---------------------------------------------------------------------------
section("1. Defining and calling")


def greet(name):
    """Return a greeting. (This text is a 'docstring' - help() shows it.)"""
    return f"Hello, {name}!"


print(greet("BooBoo"))

# print vs return:
#  print  -> shows text on the screen, the function gives back None
#  return -> gives a value back to the caller so it can be used later
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


x = add_print(2, 3)     # prints 5, but x is None
y = add_return(2, 3)    # prints nothing, y is 5
print("x =", x, "| y =", y, "| y * 10 =", y * 10)


# ---------------------------------------------------------------------------
# 2. PARAMETERS: positional, keyword, default
# ---------------------------------------------------------------------------
section("2. Parameters")


def make_profile(name, age, city="Bangkok"):   # city has a DEFAULT value
    return f"{name} ({age}) from {city}"


print(make_profile("Nok", 12))                       # positional
print(make_profile("Ton", 13, "Chiang Mai"))         # override default
print(make_profile(age=11, name="Mai"))              # keyword - any order

# GOTCHA: never use a mutable default like [] or {}
def bad_append(item, items=[]):        # the SAME list is reused every call!
    items.append(item)
    return items


def good_append(item, items=None):
    if items is None:
        items = []                     # a fresh list each call
    items.append(item)
    return items


print("bad: ", bad_append(1), bad_append(2))    # [1, 2] [1, 2]  surprise!
print("good:", good_append(1), good_append(2))  # [1] [2]


# ---------------------------------------------------------------------------
# 3. *args and **kwargs - any number of arguments
# ---------------------------------------------------------------------------
section("3. *args and **kwargs")


def total(*numbers):              # numbers becomes a TUPLE
    return sum(numbers)


def describe_pet(**info):         # info becomes a DICT
    return ", ".join(f"{k}={v}" for k, v in info.items())


print("total(1, 2, 3, 4) =", total(1, 2, 3, 4))
print(describe_pet(name="Mochi", kind="cat", age=3))

# * and ** also UNPACK when calling a function
nums = [5, 6, 7]
settings = {"name": "Rex", "kind": "dog"}
print(total(*nums))
print(describe_pet(**settings))


# ---------------------------------------------------------------------------
# 4. SCOPE - where a variable "lives"
# ---------------------------------------------------------------------------
section("4. Scope")

counter = 0   # global variable


def show_scope():
    counter = 100          # a NEW local variable, does not touch the global
    print("inside :", counter)


show_scope()
print("outside:", counter)

# Better than using 'global': take input as a parameter, give back a result
def increment(value):
    return value + 1


counter = increment(counter)
print("after increment:", counter)


# ---------------------------------------------------------------------------
# 5. FUNCTIONS ARE OBJECTS (just like everything else - see the OOP notebook)
# ---------------------------------------------------------------------------
section("5. Functions are objects")


def double(n):
    return n * 2


def apply_to_all(func, items):
    return [func(item) for item in items]


print(type(double))
print(apply_to_all(double, [1, 2, 3]))
print(apply_to_all(str.upper, ["a", "b"]))

# lambda: a tiny function without a name, for one-off use
print(apply_to_all(lambda n: n ** 2, [1, 2, 3]))

# Built-ins that take functions
nums = [3, -1, 4, -1, 5, -9]
print("map:    ", list(map(abs, nums)))
print("filter: ", list(filter(lambda n: n > 0, nums)))
print("sorted: ", sorted(nums, key=abs))


# ---------------------------------------------------------------------------
# 6. RECURSION - a function that calls itself
# ---------------------------------------------------------------------------
# Every recursive function needs:
#   1) a BASE CASE that stops it
#   2) a step that moves TOWARDS the base case
section("6. Recursion")


def factorial(n):
    if n <= 1:                 # base case
        return 1
    return n * factorial(n - 1)


def countdown(n):
    if n == 0:
        print("Go!")
        return
    print(n, end=" ")
    countdown(n - 1)


print("5! =", factorial(5))
countdown(3)


# ---------------------------------------------------------------------------
# 7. DECORATORS - wrap a function to add extra behaviour
# ---------------------------------------------------------------------------
# You already used decorators in the OOP notebook: @classmethod, @staticmethod.
# Here is how to write your own.
section("7. Decorators")

import time
from functools import wraps


def timer(func):
    @wraps(func)                       # keeps the original name/docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        ms = (time.perf_counter() - start) * 1000
        print(f"  {func.__name__} took {ms:.2f} ms")
        return result
    return wrapper


@timer                                 # same as: slow_sum = timer(slow_sum)
def slow_sum(n):
    return sum(range(n))


print("result:", slow_sum(1_000_000))


# ---------------------------------------------------------------------------
# 8. GENERATORS - functions that 'yield' values one at a time
# ---------------------------------------------------------------------------
section("8. Generators")


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a           # pause here, hand back a, continue next time
        a, b = b, a + b


print("fibonacci < 100:", list(fibonacci(100)))

# Generators save memory: values are made only when needed
squares = (n * n for n in range(1_000_000))  # generator expression - ( )
print("first square > 500:", next(s for s in squares if s > 500))


# ---------------------------------------------------------------------------
# 9. TYPE HINTS - optional labels that make code easier to understand
# ---------------------------------------------------------------------------
section("9. Type hints")


def bmi(weight_kg: float, height_m: float) -> float:
    """Body-mass index. The hints are documentation; Python does not enforce
    them, but editors and tools like mypy can check them for you."""
    return round(weight_kg / height_m ** 2, 1)


print("BMI:", bmi(45, 1.5))


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Write is_palindrome(text) that ignores case and spaces:
#    is_palindrome("Never odd or even") -> True
# 2. Write average(*numbers) that returns 0 if no numbers are given.
# 3. Write a recursive function power(base, exp) without using **.
# 4. Write a decorator @shout that turns a function's string result UPPERCASE.

"""
Lesson 03 - Dictionaries
========================

Run this file:   python lessons/03_dictionaries.py

A DICTIONARY (dict) stores KEY -> VALUE pairs, like a real dictionary
stores word -> meaning.

    student = {"name": "BooBoo", "age": 12, "grade": "A"}

- Look things up by KEY, not by position.
- Keys must be unique and immutable (str, int, tuple ... NOT list).
- Values can be anything, even other dicts or lists.
- Since Python 3.7 dicts remember the order you inserted the keys.
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. CREATING AND READING
# ---------------------------------------------------------------------------
section("1. Creating and reading")

student = {"name": "BooBoo", "age": 12, "grade": "A"}
print(student)
print("name:", student["name"])

# student["email"]  -> KeyError! the key does not exist.
# .get() is the safe way: it returns None (or a default) instead of crashing
print("email:", student.get("email"))
print("email:", student.get("email", "no email yet"))

print("has 'age' key?", "age" in student)   # 'in' checks KEYS
print("number of keys:", len(student))

# Other ways to build a dict
from_pairs = dict([("x", 1), ("y", 2)])
from_kwargs = dict(width=10, height=20)
print(from_pairs, from_kwargs)


# ---------------------------------------------------------------------------
# 2. ADDING, CHANGING, REMOVING
# ---------------------------------------------------------------------------
section("2. Adding, changing, removing")

student["age"] = 13                    # change an existing key
student["email"] = "booboo@example.com"  # add a new key
print("after add/change:", student)

student.update({"grade": "A+", "school": "Python Academy"})  # many at once
print("after update:    ", student)

removed = student.pop("email")         # remove a key and return its value
print("popped:", removed)

del student["school"]                  # remove a key, no return value
print("after del:       ", student)

student.setdefault("hobbies", [])      # add key ONLY if missing
student["hobbies"].append("drawing")
print("setdefault:      ", student)


# ---------------------------------------------------------------------------
# 3. LOOPING
# ---------------------------------------------------------------------------
section("3. Looping")

prices = {"apple": 20, "banana": 10, "mango": 35}

print("keys:  ", list(prices.keys()))
print("values:", list(prices.values()))
print("items: ", list(prices.items()))

# Looping over a dict gives you the KEYS
for fruit in prices:
    print(fruit)

# .items() gives you key AND value - you'll use this the most
for fruit, price in prices.items():
    print(f"{fruit:<8} costs {price} baht")

print("total price:", sum(prices.values()))
print("cheapest:   ", min(prices, key=prices.get))


# ---------------------------------------------------------------------------
# 4. DICT COMPREHENSIONS
# ---------------------------------------------------------------------------
#   {key_expr: value_expr  for item in iterable  if condition}
section("4. Dict comprehensions")

squares = {n: n * n for n in range(1, 6)}
print("squares:", squares)

expensive = {f: p for f, p in prices.items() if p > 15}
print("expensive:", expensive)

with_vat = {f: round(p * 1.07, 2) for f, p in prices.items()}
print("with 7% VAT:", with_vat)

# Swap keys and values
by_price = {p: f for f, p in prices.items()}
print("by price:", by_price)


# ---------------------------------------------------------------------------
# 5. COUNTING THINGS - a classic dictionary job
# ---------------------------------------------------------------------------
section("5. Counting words")

text = "the cat sat on the mat the end"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1   # start at 0 if new, then +1
print(counts)

# The standard library has a ready-made tool for this:
from collections import Counter

print(Counter(text.split()).most_common(2))


# ---------------------------------------------------------------------------
# 6. NESTED DICTIONARIES (like JSON data)
# ---------------------------------------------------------------------------
section("6. Nested data")

classroom = {
    "teacher": "Ms. Py",
    "students": [
        {"name": "BooBoo", "scores": {"math": 90, "english": 75}},
        {"name": "Nok", "scores": {"math": 65, "english": 88}},
        {"name": "Ton", "scores": {"math": 78, "english": 92}},
    ],
}

print("teacher:", classroom["teacher"])
print("first student's math:", classroom["students"][0]["scores"]["math"])

for s in classroom["students"]:
    avg = sum(s["scores"].values()) / len(s["scores"])
    print(f"{s['name']:<7} average = {avg:.1f}")

best_math = max(classroom["students"], key=lambda s: s["scores"]["math"])
print("best at math:", best_math["name"])


# ---------------------------------------------------------------------------
# 7. MERGING DICTS
# ---------------------------------------------------------------------------
section("7. Merging")

defaults = {"theme": "light", "font": 12, "sound": True}
user_settings = {"theme": "dark", "font": 14}

merged = defaults | user_settings          # Python 3.9+, right side wins
print("merged:", merged)
print("also:  ", {**defaults, **user_settings})  # older style, same result


# ---------------------------------------------------------------------------
# 8. MINI PROJECT - Simple phone book
# ---------------------------------------------------------------------------
section("8. Mini project: phone book")

phone_book = {}


def add_contact(book, name, number):
    book[name.title()] = number


def find_contact(book, name):
    return book.get(name.title(), "Not found")


add_contact(phone_book, "booboo", "081-111-1111")
add_contact(phone_book, "nok", "082-222-2222")
print(phone_book)
print("BooBoo ->", find_contact(phone_book, "BOOBOO"))
print("Ton    ->", find_contact(phone_book, "ton"))


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Count how many times each LETTER appears in "mississippi" (no Counter).
# 2. Given grades = {"Sam": 82, "Tom": 45, "Ann": 67},
#    make a new dict that maps each name to "pass" (>= 50) or "fail".
# 3. Invert {"a": 1, "b": 2, "c": 1} so values map to a LIST of keys:
#    {1: ["a", "c"], 2: ["b"]}

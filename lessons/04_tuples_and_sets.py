"""
Lesson 04 - Tuples and Sets
===========================

Run this file:   python lessons/04_tuples_and_sets.py

TUPLE  -> ordered, IMMUTABLE (cannot change after creating)
          point = (3, 4)
SET    -> unordered, NO duplicates, very fast "is it in here?" checks
          colors = {"red", "green", "blue"}

Quick comparison
----------------
            ordered?  changeable?  duplicates?  syntax
  list        yes        yes          yes        [1, 2]
  tuple       yes        no           yes        (1, 2)
  set         no         yes          no         {1, 2}
  dict        yes*       yes       keys: no      {"a": 1}
  (* insertion order)
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ===========================================================================
# PART A - TUPLES
# ===========================================================================

# ---------------------------------------------------------------------------
# 1. Creating and reading tuples
# ---------------------------------------------------------------------------
section("A1. Creating tuples")

point = (3, 4)
rgb = (255, 128, 0)
single = (5,)        # one-item tuple NEEDS the comma!
not_a_tuple = (5)    # this is just the int 5 in brackets
no_brackets = 1, 2, 3  # the commas make the tuple, not the brackets

print(point, rgb, single, no_brackets)
print("type of (5,):", type(single).__name__)
print("type of (5): ", type(not_a_tuple).__name__)

# Reading works exactly like lists
print("rgb[0] =", rgb[0], "| rgb[-1] =", rgb[-1], "| rgb[1:] =", rgb[1:])
print("count/index:", (1, 2, 2, 3).count(2), (1, 2, 2, 3).index(3))


# ---------------------------------------------------------------------------
# 2. Immutability
# ---------------------------------------------------------------------------
section("A2. Tuples cannot be changed")

try:
    point[0] = 10
except TypeError as error:
    print("TypeError:", error)

# You can make a NEW tuple instead
moved = (point[0] + 1, point[1])
print("moved point:", moved)

# Why use a tuple?
#  - It tells readers "this data should not change" (e.g. coordinates, dates)
#  - Tuples can be dict keys / set items; lists cannot
distances = {(0, 0): "home", (3, 4): "school"}
print("what is at (3, 4)?", distances[(3, 4)])


# ---------------------------------------------------------------------------
# 3. Unpacking - the tuple superpower
# ---------------------------------------------------------------------------
section("A3. Unpacking")

x, y = point
print("x =", x, "y =", y)

name, age, city = ("BooBoo", 12, "Bangkok")
print(f"{name} is {age} and lives in {city}")

# * collects "the rest" into a list
first, *middle, last = (1, 2, 3, 4, 5)
print("first:", first, "middle:", middle, "last:", last)

# Functions can return several values - they are actually returning a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([7, 2, 9, 4])
print("low:", low, "high:", high)


# ---------------------------------------------------------------------------
# 4. Named tuples - tuples with field names
# ---------------------------------------------------------------------------
section("A4. namedtuple")

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p, "| p.x =", p.x, "| p[1] =", p[1])
print("distance from origin:", (p.x ** 2 + p.y ** 2) ** 0.5)


# ===========================================================================
# PART B - SETS
# ===========================================================================

# ---------------------------------------------------------------------------
# 1. Creating sets
# ---------------------------------------------------------------------------
section("B1. Creating sets")

colors = {"red", "green", "blue", "red"}   # duplicate 'red' is dropped
print(colors)          # order may look random - sets are unordered
empty_set = set()      # NOT {} - that makes an empty dict!
print("type of {}:   ", type({}).__name__)
print("type of set():", type(empty_set).__name__)

# Most common use: remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
print("unique:", set(numbers))
print("unique as sorted list:", sorted(set(numbers)))


# ---------------------------------------------------------------------------
# 2. Adding and removing
# ---------------------------------------------------------------------------
section("B2. Adding and removing")

colors.add("yellow")
print("add:     ", colors)
colors.discard("purple")  # no error if missing
colors.remove("green")    # KeyError if missing
print("remove:  ", colors)
print("'red' in colors?", "red" in colors)  # very fast, even for huge sets


# ---------------------------------------------------------------------------
# 3. Set maths - union, intersection, difference
# ---------------------------------------------------------------------------
section("B3. Set operations")

python_class = {"BooBoo", "Nok", "Ton", "Mai"}
art_class = {"Nok", "Mai", "Fah"}

print("in either class   (|):", python_class | art_class)    # union
print("in both classes   (&):", python_class & art_class)    # intersection
print("only python       (-):", python_class - art_class)    # difference
print("in exactly one    (^):", python_class ^ art_class)    # symmetric diff

print("is {'Nok'} a subset of art?", {"Nok"} <= art_class)
print("no one in common?", python_class.isdisjoint({"Zed"}))


# ---------------------------------------------------------------------------
# 4. Set comprehension and frozenset
# ---------------------------------------------------------------------------
section("B4. Set comprehension / frozenset")

word = "programming"
vowels_used = {ch for ch in word if ch in "aeiou"}
print("vowels in 'programming':", vowels_used)

# frozenset = an immutable set (can be used as a dict key)
frozen = frozenset({1, 2, 3})
print(frozen)


# ---------------------------------------------------------------------------
# 5. MINI PROJECT - common friends
# ---------------------------------------------------------------------------
section("5. Mini project: friend suggestions")

friends = {
    "BooBoo": {"Nok", "Ton", "Mai"},
    "Nok": {"BooBoo", "Fah", "Mai"},
    "Ton": {"BooBoo", "Fah"},
}


def suggest_friends(person):
    """Friends-of-friends that are not already friends (and not the person)."""
    suggestions = set()
    for friend in friends.get(person, set()):
        suggestions |= friends.get(friend, set())
    return suggestions - friends[person] - {person}


print("Suggest for BooBoo:", suggest_friends("BooBoo"))
print("Common friends of BooBoo & Nok:", friends["BooBoo"] & friends["Nok"])


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Write a function that returns (sum, average) of a list as a tuple,
#    then unpack the result into two variables.
# 2. Given two sentences, print the words they have in common.
# 3. Check if a string is a "pangram" (uses every letter a-z at least once).

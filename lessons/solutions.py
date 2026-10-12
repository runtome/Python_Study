"""
Solutions to the "TRY IT YOURSELF" exercises
=============================================

Run this file:   python lessons/solutions.py

Try each exercise on your own FIRST. There is usually more than one correct
answer - if yours prints the same result, it's right!
Each solution is checked with 'assert', which crashes if the answer is wrong.
"""

import importlib
from functools import wraps


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ===========================================================================
section("Lesson 01 - Basics")
# ===========================================================================
# 1
name, birth_year, this_year = "BooBoo", 2014, 2026
print(f"{name} is {this_year - birth_year} years old")

# 2
sentence = "  learning PYTHON is cool  "
clean = sentence.strip()
print(clean)
print(clean.title())
print("letter o appears", clean.lower().count("o"), "times")
assert clean.lower().count("o") == 3

# 3
result = int(float("3.75") * 4)
print(result)
assert result == 15

# 4
print([n for n in range(1, 21) if n % 3 == 0])


# ===========================================================================
section("Lesson 02 - Lists and matrices")
# ===========================================================================
# 1
nums = [5, 3, 8, 1, 9, 2]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("largest:", largest)
assert largest == 9

# 2
unique = []
for n in [1, 2, 2, 3, 3, 3, 4]:
    if n not in unique:
        unique.append(n)
print("unique in order:", unique)
assert unique == [1, 2, 3, 4]
# Shortcut: dict keys keep order and are unique -> list(dict.fromkeys(data))

# 3
lengths = [len(w) for w in ["python", "is", "really", "fun"]]
print(lengths)
assert lengths == [6, 2, 6, 3]


# 4
def matmul_2x2(a, b):
    # result[r][c] = row r of a  "dot"  column c of b
    return [
        [sum(a[r][k] * b[k][c] for k in range(2)) for c in range(2)]
        for r in range(2)
    ]


product = matmul_2x2([[1, 2], [3, 4]], [[5, 6], [7, 8]])
print(product)
assert product == [[19, 22], [43, 50]]


# ===========================================================================
section("Lesson 03 - Dictionaries")
# ===========================================================================
# 1
letters = {}
for ch in "mississippi":
    letters[ch] = letters.get(ch, 0) + 1
print(letters)
assert letters == {"m": 1, "i": 4, "s": 4, "p": 2}

# 2
grades = {"Sam": 82, "Tom": 45, "Ann": 67}
results = {n: ("pass" if g >= 50 else "fail") for n, g in grades.items()}
print(results)
assert results["Tom"] == "fail"

# 3
original = {"a": 1, "b": 2, "c": 1}
inverted = {}
for key, value in original.items():
    inverted.setdefault(value, []).append(key)
print(inverted)
assert inverted == {1: ["a", "c"], 2: ["b"]}


# ===========================================================================
section("Lesson 04 - Tuples and sets")
# ===========================================================================
# 1
def sum_and_average(numbers):
    s = sum(numbers)
    return s, s / len(numbers)


total, avg = sum_and_average([2, 4, 6])
print("sum:", total, "average:", avg)
assert (total, avg) == (12, 4.0)

# 2
s1 = "the quick brown fox"
s2 = "the lazy brown dog"
common = set(s1.split()) & set(s2.split())
print("common words:", sorted(common))
assert common == {"the", "brown"}


# 3
def is_pangram(text):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(text.lower())


print(is_pangram("The quick brown fox jumps over the lazy dog"))
assert is_pangram("The quick brown fox jumps over the lazy dog")
assert not is_pangram("hello world")


# ===========================================================================
section("Lesson 05 - Control flow")
# ===========================================================================
# 1
for i in range(1, 6):
    print("*" * i)

# 2
power = 1
while power <= 1000:
    power *= 2
print("first power of 2 above 1000:", power)
assert power == 1024


# 3
def sum_positive(numbers):
    total = 0
    for n in numbers:
        if n < 0:
            continue
        total += n
    return total


print(sum_positive([3, -2, 5, -7, 1]))
assert sum_positive([3, -2, 5, -7, 1]) == 9


# 4
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0


assert to_int("42") == 42 and to_int("abc") == 0
print("to_int works")


# ===========================================================================
section("Lesson 06 - Functions")
# ===========================================================================
# 1
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


print(is_palindrome("Never odd or even"))
assert is_palindrome("Never odd or even") and not is_palindrome("Python")


# 2
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


assert average() == 0 and average(1, 2, 3) == 2
print("average works")


# 3
def power_of(base, exp):
    if exp == 0:
        return 1
    return base * power_of(base, exp - 1)


assert power_of(2, 10) == 1024
print("2^10 =", power_of(2, 10))


# 4
def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@shout
def hello(name):
    return f"hello {name}"


print(hello("booboo"))
assert hello("booboo") == "HELLO BOOBOO"


# ===========================================================================
section("Lesson 07 - OOP")
# ===========================================================================
# The lesson file name starts with a number, so we load it with importlib.
rpg = importlib.import_module("07_oop_project")


# 1
class Archer(rpg.Character):
    def attack(self, target):
        hits = [self.roll_dice(4) + 3 for _ in range(2)]
        for damage in hits:
            target.take_damage(damage)
        return f"{self.name} shoots two arrows at {target.name} for {hits}!"


robin = Archer("Robin", 70)
dummy = rpg.Warrior("Dummy", 100)
print(robin.attack(dummy))
print(dummy)
assert dummy.hp <= 100 - 8


# 2
class BetterInventory(rpg.Inventory):
    def remove(self, name):
        for item in self._items:
            if item.name == name:
                self._items.remove(item)
                return item
        return None


bag = BetterInventory()
bag.add(rpg.Item("Sword", 8))
print("removed:", bag.remove("Sword"), "| missing:", bag.remove("Shield"))
assert len(bag) == 0


# 3
class GemItem(rpg.Item):
    def __add__(self, other):
        return GemItem(f"{self.name}+{other.name}", self.power + other.power)


combo = GemItem("Sword", 8) + GemItem("Gem", 2)
print(combo)
assert combo == rpg.Item("Sword+Gem", 10)


# 4
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance -= amount

    def __str__(self):
        return f"{self.owner}'s account: {self.__balance} baht"


account = BankAccount("BooBoo", 100)
account.deposit(50)
account.withdraw(30)
print(account)
try:
    account.withdraw(1000)
except ValueError as error:
    print("ValueError:", error)
assert account.balance == 120

print("\nAll solutions passed their checks!")

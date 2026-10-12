"""
Lesson 05 - Control Flow (if / for / while)
===========================================

Run this file:   python lessons/05_control_flow.py

Control flow decides WHICH lines run and HOW MANY TIMES.
  if / elif / else  -> make decisions
  for               -> repeat for each item in something
  while             -> repeat while a condition is True
  break / continue  -> leave a loop early / skip to the next round
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. IF / ELIF / ELSE
# ---------------------------------------------------------------------------
# Python uses INDENTATION (4 spaces) to know which lines belong to the if.
section("1. if / elif / else")


def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:      # only checked if the first test was False
        return "B"
    elif score >= 60:
        return "C"
    else:                  # runs when nothing above matched
        return "F"


for s in [95, 75, 61, 30]:
    print(s, "->", grade(s))

# Combine conditions with and / or / not
age, has_ticket = 15, True
if age >= 13 and has_ticket:
    print("You can watch the movie")

# Chained comparison - reads like maths
temperature = 25
if 20 <= temperature <= 30:
    print("Nice weather!")

# One-line if (the "ternary" expression)
label = "adult" if age >= 18 else "kid"
print("label:", label)


# ---------------------------------------------------------------------------
# 2. MATCH (Python 3.10+) - a cleaner way to compare one value many times
# ---------------------------------------------------------------------------
section("2. match / case")


def describe(command):
    match command:
        case "start":
            return "Starting..."
        case "stop" | "quit":          # | means "or"
            return "Stopping."
        case _:                        # _ matches anything (like else)
            return f"Unknown command: {command}"


for cmd in ["start", "quit", "jump"]:
    print(cmd, "->", describe(cmd))


# ---------------------------------------------------------------------------
# 3. FOR LOOPS
# ---------------------------------------------------------------------------
section("3. for loops")

# range(stop), range(start, stop), range(start, stop, step)
print("range(5):        ", list(range(5)))
print("range(2, 8):     ", list(range(2, 8)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

# Loop over a string
for letter in "hi!":
    print(letter)

# Multiplication table using a NESTED loop (loop inside a loop)
print("\nTimes table:")
for row in range(1, 6):
    line = ""
    for col in range(1, 6):
        line += f"{row * col:4}"
    print(line)

# Running total
total = 0
for n in range(1, 101):
    total += n
print("\n1 + 2 + ... + 100 =", total)


# ---------------------------------------------------------------------------
# 4. WHILE LOOPS
# ---------------------------------------------------------------------------
# Use while when you don't know in advance how many times to repeat.
# ALWAYS make sure something inside the loop eventually makes it stop!
section("4. while loops")

countdown = 5
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("Lift off!")

# How many times can we halve 1000 before it drops below 1?
value, steps = 1000, 0
while value >= 1:
    value /= 2
    steps += 1
print("halvings needed:", steps)


# ---------------------------------------------------------------------------
# 5. BREAK, CONTINUE and loop ELSE
# ---------------------------------------------------------------------------
section("5. break / continue / else")

# continue -> skip the rest of this round
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n, end=" ")
print("<- multiples of 3 skipped")

# break -> leave the loop completely
for n in [4, 8, 15, 16, 23, 42]:
    if n % 2 == 1:
        print("first odd number:", n)
        break

# for ... else: the else runs only if the loop did NOT break
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            break
    else:
        return True
    return False


print("primes under 30:", [n for n in range(30) if is_prime(n)])


# ---------------------------------------------------------------------------
# 6. ERRORS: try / except
# ---------------------------------------------------------------------------
# Some code can fail (bad input, dividing by zero...). try/except lets your
# program handle the problem instead of crashing.
section("6. try / except")


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  cannot divide {a} by zero")
        return None
    except TypeError:
        print(f"  {a!r} and {b!r} must both be numbers")
        return None
    else:
        return result          # runs only if there was no error
    finally:
        print("  (finished trying)")  # ALWAYS runs


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "x"))


def ask_age(text):
    """Pretend 'text' is what a user typed."""
    try:
        return int(text)
    except ValueError:
        return f"'{text}' is not a whole number"


print(ask_age("12"), "|", ask_age("twelve"))


# ---------------------------------------------------------------------------
# 7. MINI PROJECT - FizzBuzz and a number guessing game
# ---------------------------------------------------------------------------
section("7. Mini projects")

# FizzBuzz: a famous interview question
for n in range(1, 16):
    if n % 15 == 0:
        print("FizzBuzz", end=" ")
    elif n % 3 == 0:
        print("Fizz", end=" ")
    elif n % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(n, end=" ")
print()

# Guessing game - here the "player" is a list of guesses so it runs by itself.
# To play for real, replace the list with:  guess = int(input("Guess: "))
secret = 37
guesses = [50, 25, 37]
for attempt, guess in enumerate(guesses, start=1):
    if guess < secret:
        print(f"Try {attempt}: {guess} is too low")
    elif guess > secret:
        print(f"Try {attempt}: {guess} is too high")
    else:
        print(f"Try {attempt}: {guess} is correct!")
        break


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Print a right-angled triangle of * with 5 rows using a for loop.
# 2. Using a while loop, find the first power of 2 that is bigger than 1000.
# 3. Write a function that takes a list of numbers and returns the sum of only
#    the positive ones. Use 'continue' to skip negatives.
# 4. Write a function that converts a text to int, returning 0 on bad input.

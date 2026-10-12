"""
Lesson 02 - Lists and Matrices
==============================

Run this file:   python lessons/02_lists_and_matrix.py

A LIST is an ordered collection of items that you CAN change (it is mutable).
    fruits = ["apple", "banana", "cherry"]

A MATRIX is just a "list of lists" - think of a table with rows and columns.
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. CREATING AND READING LISTS
# ---------------------------------------------------------------------------
section("1. Creating and reading lists")

fruits = ["apple", "banana", "cherry", "durian"]
mixed = [1, "two", 3.0, True, None]   # a list can hold any types
empty = []

print(fruits)
print("length:", len(fruits))
print("first :", fruits[0])     # index starts at 0
print("last  :", fruits[-1])    # negative index counts from the end
print("slice :", fruits[1:3])   # items at index 1 and 2 (3 is NOT included)
print("mixed :", mixed)
print("empty is falsy:", not empty)


# ---------------------------------------------------------------------------
# 2. CHANGING LISTS (lists are mutable)
# ---------------------------------------------------------------------------
section("2. Changing lists")

fruits[1] = "blueberry"          # replace an item
print("replace :", fruits)

fruits.append("elderberry")      # add ONE item to the end
print("append  :", fruits)

fruits.insert(0, "avocado")      # insert at a position
print("insert  :", fruits)

fruits.extend(["fig", "grape"])  # add MANY items to the end
print("extend  :", fruits)

fruits.remove("cherry")          # remove by VALUE (first match)
print("remove  :", fruits)

last = fruits.pop()              # remove and RETURN the last item
print("pop     :", fruits, "-> popped", last)

second = fruits.pop(1)           # pop by index
print("pop(1)  :", fruits, "-> popped", second)

del fruits[0]                    # delete by index, no return value
print("del [0] :", fruits)


# ---------------------------------------------------------------------------
# 3. SEARCHING, COUNTING, SORTING
# ---------------------------------------------------------------------------
section("3. Searching, counting, sorting")

scores = [70, 95, 82, 70, 60, 88]

print("70 in scores?   ", 70 in scores)
print("index of 82:    ", scores.index(82))
print("count of 70:    ", scores.count(70))

# sorted() -> returns a NEW list, original is unchanged
print("sorted():       ", sorted(scores))
print("original:       ", scores)

# .sort() -> sorts IN PLACE and returns None (a very common beginner trap!)
result = scores.sort()
print(".sort() returns:", result)
print("after .sort():  ", scores)

scores.sort(reverse=True)
print("descending:     ", scores)

scores.reverse()
print("reversed:       ", scores)

# Sort by a rule using key=
words = ["banana", "Kiwi", "apple", "fig"]
print("by length:      ", sorted(words, key=len))
print("ignore case:    ", sorted(words, key=str.lower))


# ---------------------------------------------------------------------------
# 4. COPYING - the most important "gotcha" with lists
# ---------------------------------------------------------------------------
# "b = a" does NOT copy a list. Both names point to the SAME list in memory.
# (This is the same idea as player2 = player1 in the OOP notebook.)
section("4. Copying lists")

a = [1, 2, 3]
b = a              # same list, two names
b.append(4)
print("a:", a, "b:", b, "same object?", a is b)

c = a.copy()       # a real (shallow) copy; a[:] or list(a) also work
c.append(99)
print("a:", a, "c:", c, "same object?", a is c)


# ---------------------------------------------------------------------------
# 5. LOOPING OVER LISTS
# ---------------------------------------------------------------------------
section("5. Looping")

pets = ["cat", "dog", "rabbit"]

for pet in pets:
    print("I have a", pet)

# enumerate() gives you the index AND the item
for i, pet in enumerate(pets):
    print(i, pet)

# zip() walks through two lists together
ages = [3, 5, 1]
for pet, age in zip(pets, ages):
    print(f"The {pet} is {age} years old")


# ---------------------------------------------------------------------------
# 6. LIST COMPREHENSIONS - build a list in one line
# ---------------------------------------------------------------------------
#   [expression  for item in iterable  if condition]
section("6. List comprehensions")

numbers = list(range(1, 11))     # [1, 2, ..., 10]

squares = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
shout = [p.upper() for p in pets]

print("numbers:", numbers)
print("squares:", squares)
print("evens:  ", evens)
print("shout:  ", shout)

# Same as the 'squares' comprehension, written the long way:
squares_long = []
for n in numbers:
    squares_long.append(n * n)
print("same result?", squares == squares_long)


# ---------------------------------------------------------------------------
# 7. MATRICES (list of lists)
# ---------------------------------------------------------------------------
#        col 0  col 1  col 2
# row 0 [  1,     2,     3  ]
# row 1 [  4,     5,     6  ]
# row 2 [  7,     8,     9  ]
section("7. Matrices")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("row 1:          ", matrix[1])        # [4, 5, 6]
print("row 1, col 2:   ", matrix[1][2])     # 6  -> matrix[row][col]
print("rows x cols:    ", len(matrix), "x", len(matrix[0]))

# Print it like a table
print("\nAs a table:")
for row in matrix:
    print(" ".join(f"{value:3}" for value in row))

# Get a column
col_0 = [row[0] for row in matrix]
print("\ncolumn 0:       ", col_0)

# Sum of every number
print("total:          ", sum(sum(row) for row in matrix))

# Diagonal  (row index == column index)
diagonal = [matrix[i][i] for i in range(len(matrix))]
print("diagonal:       ", diagonal)

# Transpose: rows become columns
transposed = [[row[c] for row in matrix] for c in range(len(matrix[0]))]
print("transposed:     ", transposed)
print("transpose (zip):", [list(col) for col in zip(*matrix)])

# Flatten: matrix -> single list
flat = [value for row in matrix for value in row]
print("flattened:      ", flat)

# Add two matrices element by element
other = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
added = [
    [matrix[r][c] + other[r][c] for c in range(3)]
    for r in range(3)
]
print("matrix + other: ", added)

# WARNING: never build a matrix with [[0] * 3] * 3
# It makes 3 references to the SAME row:
bad = [[0] * 3] * 3
bad[0][0] = 1
print("\nbad grid:  ", bad, "<- every row changed!")

good = [[0] * 3 for _ in range(3)]   # a new row each time
good[0][0] = 1
print("good grid: ", good)


# ---------------------------------------------------------------------------
# 8. MINI PROJECT - Tic-Tac-Toe board
# ---------------------------------------------------------------------------
section("8. Mini project: tic-tac-toe winner check")


def winner(board):
    """Return 'X' or 'O' if someone has 3 in a row, otherwise None."""
    lines = []
    lines.extend(board)                                    # 3 rows
    lines.extend([list(col) for col in zip(*board)])       # 3 columns
    lines.append([board[i][i] for i in range(3)])          # diagonal \
    lines.append([board[i][2 - i] for i in range(3)])      # diagonal /
    for line in lines:
        if line[0] != " " and line.count(line[0]) == 3:
            return line[0]
    return None


board = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    ["O", " ", "X"],
]
for row in board:
    print(" | ".join(row))
print("Winner:", winner(board))


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Given nums = [5, 3, 8, 1, 9, 2], print the largest number WITHOUT max()
#    (use a for loop).
# 2. Remove duplicates from [1, 2, 2, 3, 3, 3, 4] but KEEP the original order.
# 3. Using a list comprehension, make a list of the lengths of each word in
#    ["python", "is", "really", "fun"].
# 4. Write a function that multiplies two 2x2 matrices.

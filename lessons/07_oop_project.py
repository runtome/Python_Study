"""
Lesson 07 - OOP in Practice: a Mini RPG Game
============================================

Run this file:   python lessons/07_oop_project.py

The notebook 01_OOP.ipynb taught each OOP idea on its own. This lesson uses
ALL of them together in one small project, so you can see why they matter.

Where each idea appears (search for the tag in this file):
  [CLASS]          class, __init__, self, attributes, methods
  [CLASS-ATTR]     class attribute shared by every object
  [CLASSMETHOD]    @classmethod - an alternative constructor
  [STATICMETHOD]   @staticmethod - a helper that needs no self / cls
  [ENCAPSULATION]  hide data behind methods; _protected and __private
  [PROPERTY]       @property - a method you read like an attribute
  [ABSTRACTION]    abstract base class: "every Character must have attack()"
  [INHERITANCE]    Warrior and Wizard reuse Character's code
  [SUPER]          super().__init__() - call the parent's version
  [POLYMORPHISM]   same method name, different behaviour per class
  [DUNDER]         __str__, __repr__, __eq__, __lt__, __len__, __iter__ ...
  [MULTIPLE/MRO]   a class with two parents and its method resolution order
"""

import random
from abc import ABC, abstractmethod


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# A small helper class: Item
# ---------------------------------------------------------------------------
class Item:                                            # [CLASS]
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):                                # [DUNDER]
        # __repr__ = an unambiguous "developer" view, used inside lists
        return f"Item({self.name!r}, {self.power})"

    def __eq__(self, other):                           # [DUNDER]
        # Without this, two Items with the same data are NOT equal,
        # because == would compare memory locations (like obj1 == obj2
        # in the notebook).
        return isinstance(other, Item) and (self.name, self.power) == (
            other.name, other.power)

    def __lt__(self, other):                           # [DUNDER]
        # Defining < lets us use sorted(), min() and max() on Items
        return self.power < other.power


# ---------------------------------------------------------------------------
# Inventory: shows how dunder methods make your class feel "built-in"
# ---------------------------------------------------------------------------
class Inventory:
    MAX_ITEMS = 5                                      # [CLASS-ATTR]

    def __init__(self):
        self._items = []                               # [ENCAPSULATION]

    def add(self, item):
        if len(self) >= self.MAX_ITEMS:
            print(f"  Bag full! Could not add {item.name}.")
            return False
        self._items.append(item)
        return True

    def best(self):
        return max(self._items) if self._items else None   # uses Item.__lt__

    def __len__(self):                                 # [DUNDER] -> len(bag)
        return len(self._items)

    def __iter__(self):                                # [DUNDER] -> for x in bag
        return iter(self._items)

    def __contains__(self, name):                      # [DUNDER] -> "x" in bag
        return any(item.name == name for item in self._items)

    def __getitem__(self, index):                      # [DUNDER] -> bag[0]
        return self._items[index]


# ---------------------------------------------------------------------------
# The abstract parent: Character
# ---------------------------------------------------------------------------
class Character(ABC):                                  # [ABSTRACTION]
    """Base class for every character. You cannot create a plain Character,
    only a subclass that implements attack()."""

    count = 0                                          # [CLASS-ATTR]

    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp                                 # [ENCAPSULATION]
        self.max_hp = hp
        self.bag = Inventory()
        Character.count += 1

    # --- [PROPERTY] -------------------------------------------------------
    # hp is "read-only" from outside. To change it you must go through
    # take_damage() / heal(), which make sure it stays between 0 and max_hp.
    @property
    def hp(self):
        return self.__hp

    @property
    def is_alive(self):
        return self.__hp > 0

    def take_damage(self, amount):
        self.__hp = max(0, self.__hp - amount)

    def heal(self, amount):
        self.__hp = min(self.max_hp, self.__hp + amount)

    # --- [ABSTRACTION] ----------------------------------------------------
    @abstractmethod
    def attack(self, target):
        """Every subclass MUST write its own attack()."""

    # --- [STATICMETHOD] ---------------------------------------------------
    @staticmethod
    def roll_dice(sides=6):
        # Doesn't need self or cls - it's just a helper that lives here
        return random.randint(1, sides)

    # --- [CLASSMETHOD] ----------------------------------------------------
    @classmethod
    def from_string(cls, text):
        """Alternative constructor: Warrior.from_string("Conan,120")
        'cls' is whatever class this was called on, so it builds a Warrior
        when called on Warrior and a Wizard when called on Wizard."""
        name, hp = text.split(",")
        return cls(name.strip(), int(hp))

    # --- [DUNDER] ---------------------------------------------------------
    def __str__(self):
        # __str__ = the friendly text shown by print()
        bar = "#" * (10 * self.hp // self.max_hp)
        return f"{self.name:<8} [{bar:<10}] {self.hp:>3}/{self.max_hp} HP"

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, {self.max_hp})"


# ---------------------------------------------------------------------------
# Subclasses
# ---------------------------------------------------------------------------
class Warrior(Character):                              # [INHERITANCE]
    def __init__(self, name, hp, strength=10):
        super().__init__(name, hp)                     # [SUPER]
        self.strength = strength                       # extra attribute

    def attack(self, target):                          # [POLYMORPHISM]
        damage = self.strength + self.roll_dice()
        target.take_damage(damage)
        return f"{self.name} swings a sword at {target.name} for {damage}!"


class Wizard(Character):                               # [INHERITANCE]
    def __init__(self, name, hp, mana=30):
        super().__init__(name, hp)                     # [SUPER]
        self.mana = mana

    def attack(self, target):                          # [POLYMORPHISM]
        if self.mana >= 10:
            self.mana -= 10
            damage = 15 + self.roll_dice(8)
            target.take_damage(damage)
            return (f"{self.name} casts a fireball at {target.name} "
                    f"for {damage}! (mana left: {self.mana})")
        self.mana += 5
        return f"{self.name} is out of mana and meditates (+5 mana)."


class Healer:
    """Not a Character - a 'mixin' that adds healing to any class."""

    def heal_ally(self, ally, amount=15):
        ally.heal(amount)
        return f"{self.name} heals {ally.name} for {amount}."


class Paladin(Warrior, Healer):                        # [MULTIPLE/MRO]
    def attack(self, target):
        # Reuse Warrior.attack via super(), then add something extra
        message = super().attack(target)               # [SUPER]
        self.heal(3)
        return message + f" ({self.name} feels holy +3 HP)"


# ===========================================================================
# DEMO
# ===========================================================================
if __name__ == "__main__":
    random.seed(7)  # same "random" numbers every run, so output is repeatable

    section("1. Abstraction: you cannot create a plain Character")
    try:
        Character("Nobody", 10)
    except TypeError as error:
        print("TypeError:", error)

    section("2. Creating characters (normal and @classmethod)")
    conan = Warrior("Conan", 120, strength=12)
    merlin = Wizard.from_string("Merlin, 80")          # [CLASSMETHOD]
    arthur = Paladin("Arthur", 100)
    team = [conan, merlin, arthur]
    print(team)                                        # uses __repr__
    print("characters created:", Character.count)      # class attribute

    section("3. Encapsulation and @property")
    print(conan)                                       # uses __str__
    print("conan.hp =", conan.hp)
    try:
        conan.hp = 9999                                # property has no setter
    except AttributeError as error:
        print("AttributeError:", error)
    conan.take_damage(500)
    print("after 500 damage:", conan.hp, "(never below 0)")
    conan.heal(1000)
    print("after big heal:  ", conan.hp, "(never above max)")
    # Name mangling: __hp is stored as _Character__hp. It's hidden, not secret.
    print("mangled name exists?", hasattr(conan, "_Character__hp"))

    section("4. Dunder methods make Inventory act like a list")
    for item in [Item("Stick", 1), Item("Sword", 8), Item("Axe", 6)]:
        conan.bag.add(item)
    print("len(bag):       ", len(conan.bag))
    print("bag[0]:         ", conan.bag[0])
    print("'Sword' in bag: ", "Sword" in conan.bag)
    print("sorted(bag):    ", sorted(conan.bag))
    print("best item:      ", conan.bag.best())
    print("Item == Item?   ", Item("Axe", 6) == Item("Axe", 6))

    section("5. Polymorphism: same call, different behaviour")
    dragon = Warrior("Dragon", 200, strength=8)
    for hero in team:
        print(hero.attack(dragon))                     # [POLYMORPHISM]
    print(dragon)

    section("6. Multiple inheritance and MRO")
    print(arthur.heal_ally(merlin))
    print("isinstance(arthur, Healer)?", isinstance(arthur, Healer))
    print("Paladin MRO:", [cls.__name__ for cls in Paladin.__mro__])

    section("7. A short battle")
    round_no = 0
    while dragon.is_alive and any(h.is_alive for h in team):
        round_no += 1
        print(f"-- Round {round_no} --")
        for hero in team:
            if hero.is_alive and dragon.is_alive:
                print(" ", hero.attack(dragon))
        if dragon.is_alive:
            victim = random.choice([h for h in team if h.is_alive])
            print(" ", dragon.attack(victim))
    print()
    for character in team + [dragon]:
        print(character)
    print("\nThe heroes win!" if not dragon.is_alive else "\nThe dragon wins!")


# ---------------------------------------------------------------------------
# TRY IT YOURSELF  (answers in lessons/solutions.py)
# ---------------------------------------------------------------------------
# 1. Add an Archer(Character) whose attack() hits twice for roll_dice(4) + 3.
# 2. Give Inventory a remove(name) method that returns the removed Item
#    (or None if it isn't there).
# 3. Add __add__ to Item so Item("Sword", 8) + Item("Gem", 2) returns
#    Item("Sword+Gem", 10).
# 4. Create a BankAccount class with a private __balance, a read-only
#    balance @property, deposit() and withdraw() that refuse invalid amounts.

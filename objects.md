# Python Lists - Beginner's Guide

This document explains clearly and simply how to **create and work with lists in Python**.

---

## What is a Python List?

A **Python list** is a collection of items stored in a specific order. Lists are mutable (you can change them), flexible, and powerful.

---

## How to Create a List

Creating a Python list is easy:

```python
# Creating a simple list
fruits = ["apple", "banana", "cherry"]

# List with numbers
numbers = [1, 2, 3, 4, 5]

# Mixed data types
mixed = ["Ali", 25, True]
```

---

## Accessing List Elements

List elements are accessed using an **index**. Remember, Python indexes start from **0**.

```python
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # apple
print(fruits[2])  # cherry
```

---

## Modifying List Elements

Lists are mutable. You can change the elements easily.

```python
fruits = ["apple", "banana", "cherry"]

# Change "banana" to "kiwi"
fruits[1] = "kiwi"

print(fruits)  # ["apple", "kiwi", "cherry"]
```

---

## Adding and Removing Items

You can add new items or remove existing ones.

### Adding items:

```python
fruits = ["apple", "banana"]

# Add new fruit at end
fruits.append("cherry")

# Insert item at specific position
fruits.insert(1, "kiwi")

print(fruits)  # ["apple", "kiwi", "banana", "cherry"]
```

### Removing items:

```python
fruits = ["apple", "banana", "cherry"]

# Remove item by value
fruits.remove("banana")

# Remove item by index
removed_item = fruits.pop(0)

print(fruits)  # ["cherry"]
print(removed_item)  # apple
```

---

## List Length

Find the number of items using `len()`:

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3
```

---

## Practical Exercise

Create your own list of favorite books and perform the following:

- Print the first book.
- Change the second book.
- Add a new book.
- Remove the last book.

```python
books = ["Book1", "Book2", "Book3"]

# Your practice here...
```

---

You're now ready to confidently use Python lists!

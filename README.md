![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
# Python Basics
Welcome to the Python Basics section of the Python Learning Repository. This section will introduce you to the fundamental concepts of Python programming. Each concept is explained with examples and exercises to reinforce your understanding.

## Table of Contents

**Basics**
1. [Hello World](#hello-world)
2. [Variables and Data Types](#variables-and-data-types) 
3. [Basic Operators](#basic-operators)
4. [String Manipulation](#string-manipulation) 
5. [Lists](#lists)
6. [Tuples](#tuples)
7. [Dictionaries](#dictionaries)
8. [Sets](#sets)
9. [Conditionals](#conditionals)
10. [Loops](#loops)

**[Code Challenges](./code_challenge)**

## Hello World
The "Hello World" program is a simple script that prints "Hello, World!" to the screen. 

It is often used as a first step in learning a new programming language.


```python

# This is a comment. Comments are ignored by the Python interpreter.
# Print "Hello, World!" to the console

print("Hello, World!")
```

## Variables and Data Types
Variables are used to store data, and data types define the type of data a variable can hold.


```python
# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

print(age)
print(height)
print(name)
print(is_student)
```

## Basic Operators
Python supports various operators for arithmetic, comparison, and logical operations.


```python
# Arithmetic Operators
a = 10
b = 5

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division

# Comparison Operators
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than

# Logical Operators
x = True
y = False

print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT
```

## String Manipulation
Strings are sequences of characters. Python provides various methods to manipulate strings.


```python

# String concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)

# String methods
print(message.lower())
print(message.upper())
print(message.replace("Alice", "Bob"))

# Slicing
print(message[0:5])  # Hello
print(message[7:12]) # Alice
```

## Lists
Lists are ordered collections of items that are mutable.


```python
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[0])  # apple
print(fruits[1])  # banana

# Adding elements
fruits.append("date")
print(fruits)

# Removing elements
fruits.remove("banana")
print(fruits)
```

## Tuples
Tuples are ordered collections of items that are immutable.


```python
# Creating a tuple
coordinates = (10, 20)
print(coordinates)

# Accessing elements
print(coordinates[0])  # 10
print(coordinates[1])  # 20

# Tuples are immutable
# coordinates[0] = 15  # This will raise an error
```

## Dictionaries
Dictionaries are collections of key-value pairs.


```python
# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)

# Accessing values
print(person["name"])  # Alice
print(person["age"])   # 25

# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person)

# Removing a key-value pair
del person["age"]
print(person)
```

## Sets
Sets are unordered collections of unique items.


```python
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Adding an element
fruits.add("date")
print(fruits)

# Removing an element
fruits.remove("banana")
print(fruits)

# Sets are unordered
# print(fruits[0])  # This will raise an error
```
## Conditionals
Conditional statements allow you to execute code based on certain conditions.


```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Elif
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```
## Loops
Loops are used to repeat a block of code multiple times.


```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
## License
This repository is licensed under the Apache License. See the [LICENSE](./LICENSE) file for more information.

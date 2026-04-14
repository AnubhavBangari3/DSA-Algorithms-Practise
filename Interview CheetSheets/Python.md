# Python Fundamentals

Very high priority
Almost always asked in interview screening rounds

---

## Data Types in Python

Python provides built in data structures to store and manipulate data

### List

Ordered, mutable collection that allows duplicate elements

Example

```python
my_list = [1, 2, 3, 2]
my_list.append(4)
print(my_list)
```

Key Points
Ordered
Allows duplicates
Mutable

---

### Tuple

Ordered, immutable collection

Example

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10 will raise error
```

Key Points
Ordered
Allows duplicates
Immutable

---

### Set

Unordered collection of unique elements

Example

```python
my_set = {1, 2, 3, 2}
print(my_set)
```

Key Points
No duplicates
Unordered
Mutable

---

### Dictionary

Key value pair data structure

Example

```python
my_dict = {"name": "Anubhav", "age": 25}
print(my_dict["name"])
```

Key Points
Key value pairs
Keys must be immutable
Fast lookup

---

## Mutable vs Immutable

Very important interview topic

Mutable objects can be changed after creation
Immutable objects cannot be changed after creation

Examples

Mutable

```python
my_list = [1, 2, 3]
my_list[0] = 10
```

Immutable

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10 will raise error
```

Common Types

Mutable
list
set
dict

Immutable
int
float
str
tuple

Interview Insight
Mutable objects store reference and allow in place modification
Immutable objects create new memory on modification

---

## Variable Scope

Defines where a variable can be accessed

### Local Scope

Variable declared inside a function

```python
def func():
    x = 10
    print(x)
```

### Global Scope

Declared outside all functions

```python
x = 100

def func():
    print(x)
```

### Nonlocal Scope

Used inside nested functions

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)
```

Interview Insight
Local variables have highest priority
Global keyword is used to modify global variable
Nonlocal is used for enclosing scope

---

## Type Checking

Used to verify type of variable

### type

Returns exact type

```python
x = 10
print(type(x))
```

### isinstance

Checks inheritance as well

```python
x = 10
print(isinstance(x, int))
```

Interview Insight
type checks exact type
isinstance is preferred because it supports inheritance

---

## Input and Output Basics

### Input

```python
name = input("Enter your name ")
print(name)
```

### Output

```python
print("Hello World")
```

Formatted Output

```python
name = "Anubhav"
age = 25
print(f"My name is {name} and age is {age}")
```

---

## Global Interpreter Lock GIL

GIL is a mutex that allows only one thread to execute Python bytecode at a time

Why it exists
Simplifies memory management
Prevents race conditions

Impact
Multithreading does not give true parallelism for CPU bound tasks

Better for
I O bound tasks

Example

```python
import threading

def task():
    print("Running")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
```

Interview Insight
Use multiprocessing for CPU intensive tasks
Use multithreading for I O tasks

---

## Memory Management in Python

Python uses automatic memory management

Two main components

### Reference Counting

Each object keeps count of references

```python
a = [1, 2, 3]
b = a
```

Both a and b point to same object

When reference count becomes zero memory is freed

---

### Garbage Collection

Handles cyclic references

Example

```python
import gc
gc.collect()
```

---

### Memory Allocation

Small objects are managed by private heap
Python uses memory pools for efficiency

---

Interview Insight

Python manages memory automatically
Developer does not need manual allocation or deallocation
Understanding reference behavior helps avoid memory issues

---

## Quick Summary for Interview

List tuple set dict are core data structures
Mutable vs immutable is frequently asked
Scope local global nonlocal is very important
Prefer isinstance over type
GIL affects multithreading performance
Memory management is automatic using reference counting and garbage collection

# Python Interview Questions

---

# 1. Explain Time Complexity

## Answer

Time Complexity tells us **how the execution time of an algorithm grows as the input size increases.**

It helps us compare the efficiency of different algorithms.

### Common Time Complexities

| Complexity | Meaning | Example |
|------------|---------|---------|
| O(1) | Constant Time | Dictionary Lookup |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Loop through a list |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Nested Loops |

### Example

```python
nums = [10,20,30,40]

for num in nums:
    print(num)
```

**Time Complexity:** **O(n)**

Because the loop runs once for every element.

---

# 2. Explain Space Complexity

## Answer

Space Complexity tells us **how much extra memory an algorithm uses while executing.**

It includes variables, temporary data structures, recursion stack, etc.

### Example

```python
nums = [1,2,3]

total = 0

for num in nums:
    total += num
```

Extra memory used is only one variable (`total`).

**Space Complexity:** **O(1)**

---

Another example:

```python
nums = [1,2,3]

copy = []

for num in nums:
    copy.append(num)
```

Extra list is created.

**Space Complexity:** **O(n)**

---

# 3. Explain Dictionaries vs Lists

## Answer

| Dictionary | List |
|------------|------|
| Stores data as **key-value pairs** | Stores ordered values |
| Access by key | Access by index |
| Keys must be unique | Duplicate values allowed |
| Lookup is O(1) | Search is O(n) |
| Uses `{}` | Uses `[]` |

### Dictionary Example

```python
student = {
    "name": "Anubhav",
    "age": 26
}

print(student["name"])
```

Output

```
Anubhav
```

---

### List Example

```python
numbers = [10,20,30]

print(numbers[1])
```

Output

```
20
```

---

# 4. Explain Sets

## Answer

A **Set** is an unordered collection of **unique elements**.

- No duplicate values
- Fast lookup
- Useful for removing duplicates

### Example

```python
numbers = {1,2,2,3,3,4}

print(numbers)
```

Output

```
{1,2,3,4}
```

### Common Operations

```python
nums = {1,2,3}

nums.add(4)

nums.remove(2)

print(3 in nums)
```

---

# 5. Explain Thread Safety

## Answer

Thread Safety means **multiple threads can access shared data without causing incorrect results or data corruption.**

We usually use **Lock** to make code thread-safe.

### Without Lock

```python
count = 0

# Thread A
count += 1

# Thread B
count += 1
```

Both threads may update `count` at the same time, causing an incorrect value.

---

### With Lock

```python
import threading

lock = threading.Lock()

count = 0

with lock:
    count += 1
```

Only one thread can update `count` at a time.

This prevents race conditions.

---

# 6. Explain OOP Concepts

## Answer

OOP (Object-Oriented Programming) organizes code using **Classes** and **Objects**.

### Four Main Concepts

### 1. Encapsulation

Keeping data and methods together inside a class.

```python
class Employee:

    def __init__(self,name):
        self.name = name
```

---

### 2. Inheritance

One class inherits properties from another.

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

Dog().sound()
```

Output

```
Animal Sound
```

---

### 3. Polymorphism

Same method behaves differently.

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")
```

---

### 4. Abstraction

Hide implementation details and expose only necessary functionality.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

# 7. Explain Decorators

## Answer

A **Decorator** is a function that **adds extra functionality to another function without modifying its original code.**

### Example

```python
def logger(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper


@logger
def greet():
    print("Hello")


greet()
```

Output

```
Before Function
Hello
After Function
```

Common Uses

- Logging
- Authentication
- Authorization
- Timing Functions
- Caching

---

# 8. Explain Generators

## Answer

A **Generator** generates values **one at a time** using the `yield` keyword.

It saves memory because it does not store all values at once.

### Example

```python
def numbers():

    yield 1
    yield 2
    yield 3


for num in numbers():
    print(num)
```

Output

```
1
2
3
```

### Benefits

- Memory Efficient
- Lazy Loading
- Used for large datasets and file processing

---

# 9. Explain Iterators

## Answer

An **Iterator** is an object that returns one element at a time using `next()`.

Every generator is an iterator.

### Example

```python
nums = [10,20,30]

iterator = iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output

```
10
20
30
```

### Difference Between Iterable and Iterator

| Iterable | Iterator |
|-----------|----------|
| Can be looped over | Returns one value at a time |
| Uses `iter()` | Uses `next()` |
| Example: List, Tuple, Set | Object returned by `iter()` |

---

# Interview One-Liners

### Time Complexity
Measures how execution time grows as input size increases.

### Space Complexity
Measures how much extra memory an algorithm uses.

### Dictionary
Stores data as key-value pairs with O(1) average lookup.

### List
Stores ordered elements accessed by index.

### Set
Stores unique unordered values and removes duplicates automatically.

### Thread Safety
Ensures multiple threads access shared data safely using synchronization like `Lock`.

### OOP
Programming based on Classes and Objects using Encapsulation, Inheritance, Polymorphism, and Abstraction.

### Decorator
Adds functionality to a function without changing its original code.

### Generator
Produces values one at a time using `yield`, making it memory efficient.

### Iterator
Returns one element at a time using `next()`.
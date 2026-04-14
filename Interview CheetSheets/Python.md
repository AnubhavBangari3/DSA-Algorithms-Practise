# Python Fundamentals

Very high priority
Almost always asked in interview screening rounds

---
## Section 1
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


---

## GIL affects multithreading performance

GIL stands for Global Interpreter Lock

It is a lock inside the Python interpreter that allows only one thread to execute Python bytecode at a time

Even if you create multiple threads, only one thread runs at a time on CPU

### Why GIL exists

Python uses simple memory management based on reference counting
To keep it safe and avoid race conditions, GIL ensures only one thread modifies objects at a time

This makes Python easier and safer internally

### Impact on Performance

CPU bound tasks
Multiple threads do not run in parallel
No real performance gain

Example

```python
import threading

def task():
    for _ in range(10000000):
        pass

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
```

Even with 2 threads, execution is almost same as single thread

Reason
GIL allows only one thread to execute at a time

---

I O bound tasks
Threads work efficiently

Example

```python
import threading
import time

def task():
    time.sleep(2)
    print("Done")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
```

Both threads run concurrently because while one is waiting for I O, GIL is released

---

### Interview Insight

GIL is the reason why Python multithreading is not suitable for CPU heavy tasks

Use multiprocessing for CPU bound work
Use multithreading for I O operations

---

## Memory management using reference counting and garbage collection

Python automatically manages memory
You do not need to manually allocate or free memory

It mainly uses two techniques

---

### Reference Counting

Each object in Python has a reference count
This count represents how many variables are pointing to that object

Example

```python
a = [1, 2, 3]
b = a
```

Now both a and b point to same object
Reference count becomes 2

If we delete one reference

```python
del a
```

Reference count becomes 1

When reference count becomes 0
Python automatically deletes the object and frees memory

---

### Problem with reference counting

It cannot handle cyclic references

Example

```python
a = []
b = []

a.append(b)
b.append(a)
```

Here both objects reference each other
Reference count never becomes zero
Memory is not freed

---

### Garbage Collection

To solve this, Python uses garbage collection

It detects such cyclic references and removes them

Example

```python
import gc
gc.collect()
```

Garbage collector finds unused objects and frees memory

---

### How Python stores memory

All objects are stored in a private heap
Python internally manages allocation and deallocation

It also uses memory pools to optimize performance

---

### Interview Insight

Python memory is automatic


Reference counting handles most cases


Garbage collection handles cyclic references


Understanding references is important to avoid memory leaks

---

### Simple One Line Summary

GIL allows only one thread to execute Python code at a time which limits CPU parallelism

Memory management in Python is automatic using reference counting and garbage collection to free unused objects

---
## Section 2
# Collections Deep Dive Cheat Sheet

Interview focused quick revision with tables and clear examples

---

## List vs Tuple Cheat Sheet

| Feature        | List            | Tuple       |
| -------------- | --------------- | ----------- |
| Mutability     | Mutable         | Immutable   |
| Syntax         | square brackets | parentheses |
| Performance    | Slower          | Faster      |
| Memory         | More memory     | Less memory |
| Modification   | Allowed         | Not allowed |
| Use Case       | Dynamic data    | Fixed data  |
| Dictionary Key | Not allowed     | Allowed     |

Example

```python
my_list = [1, 2, 3]
my_list.append(4)

my_tuple = (1, 2, 3)
```

Interview Insight
Tuple is preferred when data should not change and performance matters
List is preferred when frequent updates are required

---

## Set Operations Cheat Sheet

| Operation    | Symbol       | Description            | Example   |
| ------------ | ------------ | ---------------------- | --------- |
| Union        | vertical bar | Combines elements      | a or b    |
| Intersection | ampersand    | Common elements        | a and b   |
| Difference   | minus        | Elements in a not in b | a minus b |

Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
```

Interview Insight
Set operations are fast because they use hashing
Useful for removing duplicates and checking membership

---

## Dictionary Operations Cheat Sheet

| Operation      | Method      | Description                 | Example         |
| -------------- | ----------- | --------------------------- | --------------- |
| Access safely  | get         | Avoids error if key missing | d.get key       |
| Update         | update      | Add or modify values        | d.update        |
| Default values | defaultdict | Auto assign default         | defaultdict int |

Example

```python
my_dict = {"name": "Anubhav", "age": 25}

print(my_dict.get("name"))
print(my_dict.get("city", "Not Found"))

my_dict.update({"age": 26})

from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
```

Interview Insight
get prevents KeyError
defaultdict is very useful in counting problems

---

## Shallow Copy vs Deep Copy

| Feature        | Shallow Copy      | Deep Copy                 |
| -------------- | ----------------- | ------------------------- |
| Copy Level     | Top level only    | Full nested copy          |
| Nested Objects | Shared reference  | Independent               |
| Performance    | Faster            | Slower                    |
| Use Case       | Simple structures | Complex nested structures |

---

### Shallow Copy Example

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 10

print(a)
```

Explanation
Inner list is shared
Changing b also changes a

---

### Deep Copy Example

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 10

print(a)
```

Explanation
Completely separate objects
Changing b does not affect a

---

Interview Insight
Shallow copy copies reference
Deep copy copies actual data

---

## Time Complexity Cheat Sheet

### List

| Operation           | Complexity |
| ------------------- | ---------- |
| Membership check    | O of n     |
| Insert at end       | O of 1     |
| Insert at beginning | O of n     |
| Delete              | O of n     |

---

### Set

| Operation        | Complexity |
| ---------------- | ---------- |
| Membership check | O of 1     |
| Insert           | O of 1     |
| Delete           | O of 1     |

---

### Dictionary

| Operation        | Complexity |
| ---------------- | ---------- |
| Membership check | O of 1     |
| Insert           | O of 1     |
| Delete           | O of 1     |

---

Interview Insight

List is slower for search and insert at beginning

Set and Dictionary are faster due to hashing

---

## Final Quick Summary

Tuple is faster and immutable

List is flexible and mutable

Set is best for uniqueness and fast lookup

Dictionary is best for key value mapping

Use deep copy when working with nested structures

Time complexity is important for writing optimized code
---

## Section 3

# Python Functions Deep Dive

Important interview topic
Focus on understanding behavior and real use cases

---

## Types of Arguments in Python

Python supports multiple types of arguments in functions

### Positional Arguments

Values are assigned based on position

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

---

### Keyword Arguments

Arguments are passed using parameter names

```python
def add(a, b):
    return a + b

print(add(a=2, b=3))
```

---

### Default Arguments

Default value is used if no argument is passed

```python
def greet(name="Guest"):
    print(name)

greet()
greet("Anubhav")
```

---

### args

Used to pass variable number of positional arguments

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))
```

---

### kwargs

Used to pass variable number of keyword arguments

```python
def details(**kwargs):
    print(kwargs)

details(name="Anubhav", age=25)
```

---

## Argument Types Cheat Sheet

| Type       | How Passed          | Flexibility    | Example             |
| ---------- | ------------------- | -------------- | ------------------- |
| Positional | By position         | Fixed          | add(2, 3)           |
| Keyword    | By name             | Flexible order | add(a=2, b=3)       |
| Default    | Predefined value    | Optional       | greet()             |
| args       | Multiple positional | Very flexible  | total(1, 2, 3)      |
| kwargs     | Multiple keyword    | Very flexible  | details(name value) |

---

### Interview Insight

args is used when number of inputs is unknown
kwargs is used when input is key value pairs
Default arguments avoid errors when values are missing

---

## Lambda Functions

Anonymous functions without name

Used for short and simple operations

```python
square = lambda x: x * x
print(square(5))
```

---

### With Sorting

```python
data = [(1, 3), (2, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
```

---

### Interview Insight

Used when function is small and used once
Cannot contain multiple statements
Mostly used with map filter sorted

---

## First Class Functions

Functions are treated like variables

They can be assigned passed or returned

```python
def greet():
    return "Hello"

x = greet
print(x())
```

---

### Passing Function as Argument

```python
def apply(func, value):
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))
```

---

### Interview Insight

Python treats functions as objects
This enables higher order programming

---

## Closures

A closure is a function that remembers variables from its outer scope even after the outer function has finished execution

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))
```

---

### Explanation

outer function creates variable x
inner function uses x
Even after outer finishes inner still remembers x

---

### Real Use Case

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(10))
```

---

### Interview Insight

Closures help in data hiding
Used in decorators and functional programming

---

## Section 4

# Python OOP Concepts



---

## Class and Object

Class is a blueprint
Object is an instance of a class

Example

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Anubhav")
print(p1.name)
```

Interview Insight
Class defines structure
Object holds actual data

---

## Multithreading vs Multiprocessing

Both are used for parallel execution but behave differently

### Multithreading

Runs multiple threads within same process

Example

```python
import threading
import time

def task():
    time.sleep(2)
    print("Task done")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
```

---

### Multiprocessing

Runs multiple processes using separate memory

Example

```python
from multiprocessing import Process

def task():
    print("Running process")

p1 = Process(target=task)
p2 = Process(target=task)

p1.start()
p2.start()
```

---

### Difference Table

| Feature    | Multithreading | Multiprocessing  |
| ---------- | -------------- | ---------------- |
| Memory     | Shared         | Separate         |
| GIL impact | Affected       | Not affected     |
| Best for   | I O tasks      | CPU tasks        |
| Speed      | Limited by GIL | True parallelism |

---

## init and Constructor Behavior

init is a special method called when object is created

Example

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Anubhav")
```

Explanation
init initializes object attributes
Constructor creates object and init initializes it

---

## Instance vs Class Variables

### Instance Variables

Unique for each object

### Class Variables

Shared across all objects

Example

```python
class Employee:
    company = "TCS"

    def __init__(self, name):
        self.name = name

e1 = Employee("A")
e2 = Employee("B")

print(e1.company)
print(e2.company)
```

---

### Difference Table

| Feature | Instance Variable | Class Variable |
| ------- | ----------------- | -------------- |
| Scope   | Per object        | Shared         |
| Memory  | Separate copy     | Single copy    |
| Access  | self.variable     | Class.variable |

---

## Inheritance

Allows one class to acquire properties of another

### Single Inheritance

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass
```

---

### Multiple Inheritance

```python
class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class C(A, B):
    pass
```

---

### Interview Insight

Promotes code reuse
Python uses method resolution order to resolve conflicts

---

## Method Overriding

Child class provides its own implementation of parent method

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

c = Child()
c.show()
```

---

## Encapsulation

Binding data and methods together and restricting access

Example

```python
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

### Interview Insight

Private variables use double underscore
Provides data protection

---

## Polymorphism

Same method name behaves differently

Example

```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()
```

---

### Interview Insight

Achieved using method overriding or duck typing

---

## Abstraction using ABC module

Hides implementation details and shows only essential features

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4 * 4
```

---

### Interview Insight

Cannot instantiate abstract class
Child must implement abstract methods

---

## Magic Methods

Special methods that define behavior of objects

### str

User friendly string representation

### repr

Developer friendly representation

Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name is {self.name}"

    def __repr__(self):
        return f"Person({self.name})"

p = Person("Anubhav")
print(p)
print(repr(p))
```

---

### Interview Insight

str is for users
repr is for debugging

# OOP Comparison Cheat Sheets

Interview focused comparison tables for quick revision

---

## Method Overloading vs Method Overriding

| Feature           | Method Overloading                         | Method Overriding                          |
| ----------------- | ------------------------------------------ | ------------------------------------------ |
| Definition        | Same method name with different parameters | Same method name in parent and child class |
| Support in Python | Not true overloading                       | Fully supported                            |
| How achieved      | Using default args or args                 | Using inheritance                          |
| Class Involvement | Usually same class                         | Requires parent and child class            |
| Behavior          | Depends on arguments                       | Child replaces parent behavior             |
| Runtime           | Compile time concept in other languages    | Runtime concept                            |

Example Overloading style in Python

```python id="m6z6n9"
class Calc:
    def add(self, a, b=0, c=0):
        return a + b + c

c = Calc()
print(c.add(2))
print(c.add(2, 3))
print(c.add(2, 3, 4))
```

Example Overriding

```python id="vtcm9k"
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

Interview Insight
Python does not support true method overloading
Method overriding is widely used in OOP

---

## Encapsulation vs Abstraction

| Feature        | Encapsulation                      | Abstraction                   |
| -------------- | ---------------------------------- | ----------------------------- |
| Definition     | Hiding data and restricting access | Hiding implementation details |
| Focus          | Data protection                    | Simplifying interface         |
| How achieved   | Private variables and methods      | Abstract classes and methods  |
| Module used    | No special module required         | abc module                    |
| Access control | Yes                                | Partial                       |
| Example        | Bank account balance               | Shape interface               |

---

Example Encapsulation

```python id="jex1xv"
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

Example Abstraction

```python id="plk0po"
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

Interview Insight
Encapsulation protects data
Abstraction hides complexity

---

## Inheritance vs Composition

| Feature      | Inheritance          | Composition          |
| ------------ | -------------------- | -------------------- |
| Relationship | Is a relationship    | Has a relationship   |
| Example      | Dog is Animal        | Car has Engine       |
| Reusability  | Through parent class | Through object usage |
| Flexibility  | Less flexible        | More flexible        |
| Coupling     | Tight coupling       | Loose coupling       |

---

Example Inheritance

```python id="ap2d5d"
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    pass
```

---

Example Composition

```python id="8v33qz"
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```

---

Interview Insight
Prefer composition over inheritance for flexibility

---

## Class vs Instance Variables

| Feature       | Class Variable        | Instance Variable  |
| ------------- | --------------------- | ------------------ |
| Scope         | Shared across objects | Unique per object  |
| Memory        | Single copy           | Multiple copies    |
| Access        | Class level           | Object level       |
| Change impact | Affects all objects   | Affects one object |

---

## Multithreading vs Multiprocessing

| Feature     | Multithreading  | Multiprocessing  |
| ----------- | --------------- | ---------------- |
| Execution   | Threads         | Processes        |
| Memory      | Shared          | Separate         |
| GIL impact  | Yes             | No               |
| Best for    | I O bound tasks | CPU bound tasks  |
| Performance | Limited         | True parallelism |

---

## str vs repr

| Feature | str           | repr               |
| ------- | ------------- | ------------------ |
| Purpose | User readable | Developer readable |
| Usage   | print         | debugging          |
| Output  | Clean         | Detailed           |

---




---
## Section 5
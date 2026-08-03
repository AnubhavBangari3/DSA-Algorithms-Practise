# 42. Explain Decorators

### Explanation
A decorator is a function that adds extra functionality to another function without changing its code.

### Example
```python
def logger(func):
    def wrapper():
        print("Function started")
        func()
    return wrapper

@logger
def greet():
    print("Hello")

greet()
```

---

# 43. Explain Generators

### Explanation
A generator returns values one at a time using `yield` instead of returning everything at once. It saves memory.

### Example
```python
def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)
```

---

# 44. Explain Iterators

### Explanation
An iterator is an object that returns one item at a time using `next()`.

### Example
```python
nums = iter([1, 2, 3])

print(next(nums))  # 1
print(next(nums))  # 2
```

---

# 45. Explain Context Managers

### Explanation
A context manager automatically manages resources like files using the `with` statement.

### Example
```python
with open("test.txt", "r") as file:
    data = file.read()
```

---

# 46. List vs Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Slower | Faster |
| More memory | Less memory |

### Example
```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
```

---

# 47. Dictionary vs Set

| Dictionary | Set |
|------------|-----|
| Stores key-value pairs | Stores unique values |
| Uses `{key: value}` | Uses `{value}` |
| Keys are unique | Values are unique |

### Example
```python
student = {"name": "John", "age": 25}

nums = {1, 2, 3}
```

---

# 48. Mutable vs Immutable

### Mutable
Can be modified after creation.

Examples:
- List
- Dictionary
- Set

### Immutable
Cannot be modified after creation.

Examples:
- String
- Tuple
- Integer

### Example
```python
lst = [1, 2]
lst.append(3)

name = "John"
# name[0] = "A" ❌
```

---

# 49. Explain the GIL

### Explanation
GIL (Global Interpreter Lock) allows only one thread to execute Python bytecode at a time.

- Good for I/O-bound tasks
- Limits CPU-bound multithreading

### Example
Two threads calculating large numbers won't run truly in parallel in CPython.

---

# 50. Thread vs Process

| Thread | Process |
|---------|---------|
| Shares memory | Separate memory |
| Lightweight | Heavyweight |
| Faster | Slower |
| Best for I/O tasks | Best for CPU tasks |

### Example
- Downloading files → Thread
- Image processing → Process

---

# 51. Async vs Threading

| Async | Threading |
|--------|-----------|
| Single thread | Multiple threads |
| Uses event loop | Uses OS threads |
| Best for many I/O tasks | Good for blocking I/O |

### Example
- API calls → Async
- Reading multiple files → Threading

---

# 52. Multiprocessing

### Explanation
Multiprocessing creates multiple processes to achieve true parallel execution.

Used for CPU-intensive tasks.

### Example
```python
from multiprocessing import Process

def task():
    print("Running")

p = Process(target=task)
p.start()
p.join()
```

---

# 53. Lambda Functions

### Explanation
A lambda is a small anonymous function written in one line.

### Example
```python
square = lambda x: x * x

print(square(5))
```

---

# 54. Map, Filter, Reduce

### map()
Applies a function to every element.

```python
nums = [1, 2, 3]
print(list(map(lambda x: x*2, nums)))
```

### filter()
Returns elements matching a condition.

```python
nums = [1,2,3,4]
print(list(filter(lambda x: x%2==0, nums)))
```

### reduce()
Combines all values into one.

```python
from functools import reduce

nums = [1,2,3,4]
print(reduce(lambda x,y: x+y, nums))
```

---

# 55. Deep Copy vs Shallow Copy

### Shallow Copy
Copies only the outer object.
Nested objects are shared.

### Deep Copy
Copies everything, including nested objects.

### Example
```python
import copy

a = [[1,2]]
b = copy.copy(a)
c = copy.deepcopy(a)
```

---

# 56. *args and **kwargs

### *args
Accepts multiple positional arguments.

```python
def add(*args):
    print(args)

add(1,2,3)
```

### **kwargs
Accepts multiple keyword arguments.

```python
def info(**kwargs):
    print(kwargs)

info(name="John", age=25)
```

---

# 57. Explain OOP Concepts

### Encapsulation
Bundle data and methods together.

### Abstraction
Hide implementation details.

### Inheritance
One class inherits another class.

### Polymorphism
Same method behaves differently for different objects.

### Example
```python
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
```

---

# 58. Explain SOLID Principles

### S - Single Responsibility
One class should have one responsibility.

### O - Open/Closed
Open for extension, closed for modification.

### L - Liskov Substitution
Child class should replace parent without issues.

### I - Interface Segregation
Don't force classes to implement unused methods.

### D - Dependency Inversion
Depend on abstractions, not concrete classes.

---

# 59. Exception Handling

### Explanation
Exceptions prevent program crashes by handling errors gracefully.

### Example
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```

---

# 60. Memory Management

### Explanation
Python automatically allocates and frees memory.

It uses:
- Reference counting
- Garbage Collector

### Example
```python
a = [1,2,3]
b = a

del a
```

Memory is freed when no references remain.

---

# 61. Garbage Collection

### Explanation
Garbage Collection removes objects that are no longer used, especially circular references.

### Example
```python
import gc

gc.collect()
```

**Interview Tip:** Python mainly uses reference counting, while the Garbage Collector cleans up circular references.
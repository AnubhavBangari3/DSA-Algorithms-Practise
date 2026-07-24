# Django Interview Questions (3-4 Years Experience)

---

# 1. Explain Django ORM (Object Relational Mapper)

## Answer

Django ORM (Object Relational Mapper) allows us to interact with the database using **Python code instead of writing SQL queries**.

Instead of writing SQL like:

```sql
SELECT * FROM employee;
```

we write:

```python
Employee.objects.all()
```

The ORM converts Python code into SQL automatically.

### Benefits

- No need to write SQL manually.
- Database independent (MySQL, PostgreSQL, SQLite, Oracle).
- Prevents SQL Injection.
- Easy to read and maintain.

### Example

### Model

```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
```

### Create

```python
Employee.objects.create(
    name="Anubhav",
    salary=50000
)
```

### Read

```python
Employee.objects.all()
```

### Filter

```python
Employee.objects.filter(salary__gt=40000)
```

### Update

```python
emp = Employee.objects.get(id=1)
emp.salary = 60000
emp.save()
```

### Delete

```python
Employee.objects.get(id=1).delete()
```

---

# 2. Explain Serializers

## Answer

A **Serializer** converts complex Django model objects into JSON and also validates incoming JSON before saving it into the database.

Serializers are mainly used in **Django REST Framework (DRF).**

### Example

### Model

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
```

### Serializer

```python
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"
```

### Serialize Object

```python
employee = Employee.objects.first()

serializer = EmployeeSerializer(employee)

print(serializer.data)
```

Output

```json
{
    "id":1,
    "name":"Anubhav",
    "salary":50000
}
```

### Save Data

```python
serializer = EmployeeSerializer(data=request.data)

if serializer.is_valid():
    serializer.save()
```

### Benefits

- Converts Model → JSON
- Converts JSON → Model
- Performs validation
- Easy API development

---

# 3. Explain Middleware

## Answer

Middleware is a layer that executes **before and after every request and response**.

It sits between the client and the Django view.

```
Request
   ↓
Middleware
   ↓
View
   ↓
Middleware
   ↓
Response
```

### Common Uses

- Authentication
- Logging
- CORS
- Session Management
- Request Timing
- Security

### Example

```python
class RequestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("Before View")

        response = self.get_response(request)

        print("After View")

        return response
```

Register in

```python
settings.py
```

```python
MIDDLEWARE = [
    "myapp.middleware.RequestMiddleware",
]
```

---

# 4. Explain Signals

## Answer

Signals allow Django to automatically execute code when certain events occur.

Example events

- User Created
- Object Saved
- Object Deleted

Common Signals

- post_save
- pre_save
- post_delete
- pre_delete

### Example

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Employee)
def employee_created(sender, instance, created, **kwargs):

    if created:
        print("New Employee Created")
```

Whenever a new Employee is saved

```python
Employee.objects.create(
    name="John",
    salary=50000
)
```

Output

```
New Employee Created
```

### Common Uses

- Send Welcome Email
- Create User Profile
- Audit Logs
- Notifications

---

# 5. Explain Authentication

## Answer

Authentication is the process of **verifying the identity of a user.**

It answers the question:

> **Who are you?**

Django provides built-in authentication.

### Example

Login

```python
from django.contrib.auth import authenticate

user = authenticate(
    username="admin",
    password="1234"
)
```

If credentials are correct

```python
user
```

will contain the User object.

Otherwise

```python
None
```

### DRF Authentication

- Session Authentication
- Basic Authentication
- Token Authentication
- JWT Authentication

Example

```python
from rest_framework_simplejwt.authentication import JWTAuthentication
```

---

# 6. Explain Transactions

## Answer

A Transaction ensures that **multiple database operations succeed or fail together.**

If one operation fails, all previous changes are rolled back.

### Without Transaction

```python
Order.objects.create(...)

Payment.objects.create(...)

Shipment.objects.create(...)
```

If Shipment fails,

Order and Payment are already saved.

Database becomes inconsistent.

### With Transaction

```python
from django.db import transaction

with transaction.atomic():

    Order.objects.create(...)

    Payment.objects.create(...)

    Shipment.objects.create(...)
```

If Shipment fails,

Everything is rolled back.

### Benefits

- Maintains Data Consistency
- Prevents Partial Updates
- Supports Rollback

---

# 7. Explain Model Relationships

## Answer

Model Relationships define how one model is related to another.

### One-to-One

One User has one Profile.

```python
class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
```

---

### One-to-Many (ForeignKey)

One Author can have many Books.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):

    title = models.CharField(max_length=100)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
```

Example

```
Author
  |
  |---- Book 1
  |---- Book 2
  |---- Book 3
```

---

### Many-to-Many

One Student can join many Courses.

One Course can have many Students.

```python
class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):

    name = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course)
```

---

# 8. Explain Query Optimization

## Answer

Query Optimization means writing efficient database queries to improve application performance.

### Bad Example (N+1 Problem)

```python
books = Book.objects.all()

for book in books:
    print(book.author.name)
```

This executes

```
1 query for books

+

1 query for every author
```

If there are 100 books,

Total Queries = 101

---

### Optimized

```python
books = Book.objects.select_related("author")

for book in books:
    print(book.author.name)
```

Now Django performs only **1 SQL query**.

---

### Many-to-Many Optimization

```python
students = Student.objects.prefetch_related("courses")
```

Instead of multiple queries.

---

### Other Optimization Techniques

Use `only()`

```python
Employee.objects.only("name")
```

Retrieve only required fields.

---

Use `values()`

```python
Employee.objects.values("name","salary")
```

Returns dictionaries instead of model objects.

---

Use `exists()`

```python
Employee.objects.filter(id=1).exists()
```

Instead of

```python
Employee.objects.filter(id=1).count()
```

when only checking existence.

---

Use `bulk_create()`

```python
Employee.objects.bulk_create(employee_list)
```

Instead of inserting one object at a time.

---

# Interview One-Liners

### Django ORM
Allows us to interact with the database using Python objects instead of writing SQL queries.

### Serializers
Convert Django model objects to JSON and validate JSON before saving to the database.

### Middleware
Executes before and after every request/response to process requests globally.

### Signals
Automatically execute code when specific events occur, such as saving or deleting a model.

### Authentication
Verifies the identity of a user before allowing access to protected resources.

### Transactions
Ensure multiple database operations succeed or fail together using `transaction.atomic()`.

### Model Relationships
Define how models are connected using `OneToOneField`, `ForeignKey`, and `ManyToManyField`.

### Query Optimization
Improves database performance using techniques like `select_related()`, `prefetch_related()`, `only()`, `values()`, `exists()`, and `bulk_create()`.
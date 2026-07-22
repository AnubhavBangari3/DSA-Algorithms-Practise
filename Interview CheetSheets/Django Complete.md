## What is Django?

Django is a **high-level, open-source Python web framework** used to build secure, scalable, and maintainable web applications quickly.

It follows the **MTV (Model-Template-View)** architecture and the **DRY (Don't Repeat Yourself)** principle, which helps developers write clean, reusable, and organized code.

Django comes with many built-in features like an **ORM, authentication system, admin panel, form handling, security, and caching**, allowing developers to focus more on business logic instead of reinventing common functionalities.

---

## Why is Django Popular?

- Rapid application development
- Clean and reusable code
- Built-in security features
- Excellent scalability
- Large community support
- Rich package ecosystem
- Easy database management using ORM

---

## Key Features of Django

### 1. Object Relational Mapper (ORM)

Django ORM allows you to interact with the database using Python code instead of writing raw SQL queries.

Example

```python
employees = Employee.objects.filter(salary__gt=50000)
```

**Interview Insight**

ORM improves readability, reduces SQL injection risks, and supports multiple databases.

---

### 2. Built-in Admin Panel

Django automatically generates an admin interface for your models.

Example

```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```

You can perform CRUD operations directly from the admin panel without writing extra code.

---

### 3. URL Routing

Django maps URLs to specific views using the `urls.py` file.

Example

```python
from django.urls import path
from .views import home

urlpatterns = [
    path("", home),
]
```

This keeps URL management clean and organized.

---

### 4. Template Engine

Django's template engine separates frontend (HTML) from backend (Python logic).

Example

```html
<h1>Welcome {{ user.username }}</h1>
```

This makes applications easier to maintain.

---

### 5. Form Handling

Django provides built-in support for creating, validating, and processing forms.

Example

```python
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
```

---

### 6. Built-in Security

Django protects applications against common web attacks.

It provides protection against:

- SQL Injection
- Cross Site Scripting (XSS)
- Cross Site Request Forgery (CSRF)
- Clickjacking

---

### 7. Middleware

Middleware processes requests before they reach the view and responses before they are returned to the client.

Common uses

- Authentication
- Logging
- CORS
- Security
- Request tracking

---

### 8. Simplified Database Queries

Django provides a high-level QuerySet API.

Example

```python
Employee.objects.filter(department="IT")
```

No need to write SQL for most operations.

---

### 9. Reusable Applications

Django encourages creating reusable apps.

Example

```
project/
    accounts/
    products/
    orders/
```

Each app can be reused in different projects.

---

### 10. File Handling

Django provides built-in support for uploading and serving files.

Example

```python
profile_image = models.ImageField(upload_to="profiles/")
```

---

### 11. Asynchronous Support

Modern Django supports asynchronous views using `async` and `await`.

Example

```python
async def home(request):
    return HttpResponse("Hello")
```

Useful for I/O-bound operations and improving application performance.

---

### 12. Scalability

Django can scale from small websites to large enterprise applications.

Popular companies using Django include:

- Instagram
- Pinterest
- Disqus
- Mozilla

---

### 13. Built-in Caching

Django supports multiple caching backends such as:

- Redis
- Memcached
- Local Memory Cache

Caching helps improve application performance.

---

### 14. Internationalization (i18n)

Django provides built-in support for multiple languages and localization.

Useful for applications with global users.

---

### 15. Django REST Framework Support

Although Django REST Framework (DRF) is a separate package, it integrates seamlessly with Django for building REST APIs.

Example

```python
class EmployeeAPIView(APIView):
    def get(self, request):
        ...
```

---

## Advantages of Django

- Fast development
- Clean project structure
- Excellent documentation
- Secure by default
- Powerful ORM
- Built-in admin panel
- Highly scalable
- Large community support
- Easy API development using DRF

---

## Real World Example

Suppose you are building an **E-commerce website**.

Using Django, you can:

- Store products using Models
- Manage products from the Admin Panel
- Display products using Views and Templates
- Handle user registration using Authentication
- Process orders using Forms
- Cache frequently visited pages using Redis
- Build REST APIs using DRF

Most of these features are available with minimal configuration.

---

## Interview Insight

A common interview question is:

**Why do companies prefer Django over Flask?**

A good answer is:

> Django is a batteries-included framework. It comes with features like ORM, authentication, admin panel, security, form handling, middleware, and caching out of the box, allowing developers to build production-ready applications much faster than lightweight frameworks like Flask.

---

## Common Mistakes

- Saying Django is a programming language (It is a Python web framework.)
- Confusing MTV with MVC.
- Thinking Django REST Framework is part of Django (DRF is a separate package built on top of Django.)

---

## Quick Summary

- Django is a high-level Python web framework.
- It follows the MTV architecture and DRY principle.
- It provides built-in features like ORM, Admin Panel, Authentication, Security, Forms, Middleware, and Caching.
- Django supports rapid development, scalability, and secure web applications.
- Django REST Framework is commonly used with Django to build REST APIs.


## Explain the MTV (Model-Template-View) Architecture Pattern in Django

Django follows the **MTV (Model-Template-View)** architecture.

It is very similar to the traditional **MVC (Model-View-Controller)** architecture, but the naming is different.

The goal of MTV is to separate the application into different layers, making the code clean, reusable, and easier to maintain.

---

## Components of MTV

### 1. Model

The **Model** is responsible for interacting with the database.

It defines the database structure and contains the business logic related to data.

Example

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
```

Responsibilities

- Database operations
- Business logic
- Data validation
- Relationships between tables

---

### 2. Template

The **Template** is the presentation layer.

It is responsible for displaying data to the user using HTML and Django Template Language (DTL).

Example

```html
<h2>{{ employee.name }}</h2>
<p>{{ employee.salary }}</p>
```

Responsibilities

- UI rendering
- Display dynamic data
- Keep HTML separate from Python code

---

### 3. View

The **View** acts as the bridge between the Model and Template.

It receives the request, processes business logic, fetches data from the Model, and returns the appropriate response.

Example

```python
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employees.html", {"employees": employees})
```

Responsibilities

- Receive HTTP requests
- Interact with Models
- Pass data to Templates
- Return HTTP responses

---

# Django Request-Response Lifecycle

```
Client
   │
   ▼
Browser Request
   │
   ▼
urls.py
   │
   ▼
View
   │
   ▼
Model (Database)
   │
   ▼
View
   │
   ▼
Template
   │
   ▼
HTML Response
   │
   ▼
Browser
```

---

## Step-by-Step Flow

### Step 1

The client sends an HTTP request.

Example

```
GET /employees/
```

---

### Step 2

`urls.py` matches the URL with the appropriate view.

```python
path("employees/", views.employee_list)
```

---

### Step 3

The View receives the request.

```python
def employee_list(request):
```

---

### Step 4

The View fetches data using the Model.

```python
employees = Employee.objects.all()
```

---

### Step 5

The View sends the data to the Template.

```python
return render(request, "employees.html", {"employees": employees})
```

---

### Step 6

The Template generates HTML.

```html
{% for employee in employees %}
    {{ employee.name }}
{% endfor %}
```

---

### Step 7

The generated HTML is returned to the browser.

---

# MTV vs MVC

| MVC | Django MTV | Responsibility |
|------|------------|----------------|
| Model | Model | Database and Business Logic |
| View | Template | User Interface (HTML) |
| Controller | View | Handles requests and responses |

---

## Why Does Django Use MTV Instead of MVC?

Django automatically handles many controller responsibilities internally.

Instead of creating a separate Controller, Django uses:

- URL Dispatcher (`urls.py`)
- View Functions / Class-Based Views
- Middleware

Because of this, Django's **View behaves more like the Controller in MVC**, while the **Template behaves like the View in MVC**.

---

## MVC vs MTV Comparison

| Feature | MVC | Django MTV |
|---------|-----|------------|
| Model | Database Logic | Database Logic |
| View | User Interface | Template |
| Controller | Handles Requests | Django View |
| URL Routing | Controller | urls.py |
| HTML Rendering | View | Template |
| Business Logic | Controller | View |

---

## Real World Example

Suppose a user opens:

```
https://example.com/employees/
```

Flow

```
Request
      ↓
urls.py
      ↓
employee_list View
      ↓
Employee Model
      ↓
Database
      ↓
View
      ↓
employees.html Template
      ↓
Browser Response
```

---

## Interview Insight

A very common interview question is:

**Does Django follow MVC?**

Answer:

> Django follows the **MTV (Model-Template-View)** architecture. It is conceptually similar to MVC. In Django, the **View acts like the Controller**, while the **Template acts like the MVC View**.

---

## Common Mistakes

- Saying Django follows MVC (officially it follows MTV).
- Confusing Django View with MVC View.
- Thinking Templates contain business logic (they should only handle presentation).

---

## Quick Summary

- Django follows the **MTV architecture**.
- **Model** → Database and Business Logic.
- **View** → Handles requests, business logic, and responses.
- **Template** → Displays data to the user.
- Django's **View is equivalent to the Controller in MVC**.
- Django's **Template is equivalent to the View in MVC**.


## What is a Django Project and how is it Different from a Django App?

A **Django Project** is the complete web application that contains all the configurations, settings, and one or more Django apps.

A **Django App** is a standalone module that is built to perform a specific functionality. A project can contain multiple apps, and each app can be reused in different projects.

---

## Django Project

A Django Project acts as the **main container** of the application.

It contains:

- Project settings
- URL configurations
- WSGI/ASGI configuration
- Installed apps
- Database configuration
- Middleware
- Static and media settings

A project can have one or many Django apps.

---

## Key Components of a Django Project

### settings.py

Contains all project configurations.

Examples

- Database
- Installed Apps
- Middleware
- Authentication
- Static Files

---

### urls.py

Defines the project's URL routing.

Example

```python
urlpatterns = [
    path("employees/", include("employees.urls")),
]
```

---

### wsgi.py

Entry point for deploying the Django project using **WSGI-compatible servers** like Gunicorn or uWSGI.

---

### asgi.py

Entry point for **ASGI-compatible servers**.

Supports:

- Async Views
- WebSockets
- Django Channels

---

## Django App

A Django App is a **self-contained module** that provides a specific feature or business functionality.

Examples

- Authentication App
- Employee App
- Product App
- Orders App
- Payments App

Each app has its own models, views, URLs, and templates.

---

## Key Components of a Django App

### models.py

Defines database tables.

---

### views.py

Contains business logic.

---

### templates/

Contains HTML templates.

---

### urls.py

Defines URLs specific to the app.

---

### admin.py

Registers models in the Django Admin Panel.

---

### apps.py

Stores the application's configuration.

---

## Project Structure

```text
myproject/                 # Django Project
│
├── manage.py
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── employees/             # Django App
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── templates/
│
├── products/              # Another Django App
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
└── manage.py
```

---

## Django Project vs Django App

| Feature | Django Project | Django App |
|----------|----------------|------------|
| Definition | Complete web application | A module providing a specific functionality |
| Purpose | Holds the entire project configuration | Implements one business feature |
| Contains | Multiple apps | Models, Views, URLs, Templates |
| Reusability | Not reusable | Can be reused in other projects |
| Configuration | settings.py, urls.py, wsgi.py, asgi.py | models.py, views.py, admin.py, apps.py, urls.py |
| Quantity | Usually one | One or more inside a project |

---

## Real World Example

Suppose you are building an **E-commerce Website**.

**Project**

```
Ecommerce
```

**Apps**

```
accounts
products
orders
payments
cart
reviews
notifications
```

Each app handles a specific business functionality while the project manages the overall application.

---

## Interview Insight

A common interview question is:

**Can a Django Project have multiple apps?**

**Answer:**

Yes. A Django project can contain multiple apps, and each app is responsible for a specific feature. This modular approach improves code organization, maintainability, and reusability.

Another common question:

**Can a Django App be reused?**

Yes. Since a Django app is self-contained, it can be reused in different Django projects with minimal changes.

---

## Quick Summary

- A **Django Project** is the complete web application.
- A **Django App** is a reusable module that provides a specific functionality.
- A project can contain multiple apps.
- Apps contain **Models, Views, URLs, Templates, and Admin**.
- Projects contain **settings.py, urls.py, wsgi.py, and asgi.py**.

## What is the Purpose of `settings.py` in Django?

`settings.py` is the **central configuration file** of a Django project.

It contains all the project-wide settings such as database configuration, installed apps, middleware, security, static files, and more.

---

## Common Configurations in `settings.py`

### Installed Apps

Registers all Django, third-party, and custom apps.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "rest_framework",
    "employees",
]
```

---

### Database Configuration

Defines which database the project uses.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "company_db",
    }
}
```

---

### Middleware

Defines middleware executed for every request and response.

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
]
```

---

### URL Configuration

Specifies the root URL file.

```python
ROOT_URLCONF = "project.urls"
```

---

### Static & Media Files

Used for CSS, JavaScript, Images, and File Uploads.

```python
STATIC_URL = "static/"
MEDIA_URL = "media/"
```

---

### Security Settings

Controls project security.

Examples

```python
DEBUG = False

ALLOWED_HOSTS = ["example.com"]
```

---

### Environment Variables

Sensitive data like secret keys should be stored using environment variables.

```python
SECRET_KEY = os.getenv("SECRET_KEY")
```

---

## Why is `settings.py` Important?

- Centralized project configuration
- Easy environment-specific settings (Development, Testing, Production)
- Better security using environment variables
- Easy integration of third-party packages
- Consistent configuration across the project

---

## Common Use Cases

- Configure Database
- Register Installed Apps
- Add Middleware
- Configure Static & Media Files
- Security Settings
- Internationalization
- Third-party Integrations (DRF, Celery, CORS, etc.)

---

## Interview Insight

A common interview question is:

**Why should we use environment variables in `settings.py`?**

**Answer:**

To keep sensitive information like **SECRET_KEY, Database Passwords, API Keys, and JWT Secrets** out of the source code and improve security.

---

## Quick Summary

- `settings.py` is the **main configuration file** of a Django project.
- It manages **database, apps, middleware, security, URLs, static files, and environment variables**.
- It helps keep project configuration centralized, secure, and easy to manage.

## What is the Role of `urls.py` in a Django Project?

The `urls.py` file is responsible for **routing incoming HTTP requests to the appropriate view**.

It acts as a **URL dispatcher**, mapping URLs to view functions or class-based views.

---

## Types of `urls.py`

### 1. Project URLs (`project/urls.py`)

The main `urls.py` of the project.

It includes URLs from different apps.

Example

```python
from django.urls import path, include

urlpatterns = [
    path("employees/", include("employees.urls")),
    path("products/", include("products.urls")),
]
```

---

### 2. App URLs (`app/urls.py`)

Handles URLs specific to that app.

Example

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("about/", views.about),
]
```

---

## URL Patterns

### `path()`

Used for simple URL routing.

```python
path("employees/", views.employee_list)
```

---

### `re_path()`

Used for complex URL patterns with regular expressions.

```python
from django.urls import re_path

re_path(r"^articles/[0-9]{4}/$", views.article)
```

---

## URL Parameters

Parameters can be passed directly from the URL.

Example

```python
path("employees/<int:id>/", views.employee_detail)
```

View

```python
def employee_detail(request, id):
    return HttpResponse(id)
```

Request

```
/employees/10/
```

Output

```
10
```

---

## Best Practices

- Keep app-specific URLs inside each app.
- Use `include()` for modular routing.
- Use `name` for reverse URL lookup.
- Use meaningful and RESTful URL names.

Example

```python
path("employees/", views.employee_list, name="employee-list")
```

---

## Interview Insight

**Difference between `path()` and `re_path()`?**

- `path()` → Simple and readable URL patterns.
- `re_path()` → Used when regular expressions are required.

---

## Quick Summary

- `urls.py` maps URLs to Views.
- Every Django project has a **project-level** `urls.py`.
- Every app can have its own `urls.py`.
- `path()` is used for simple URLs.
- `re_path()` is used for regex-based URLs.
- `include()` helps organize app-specific routes.

## Explain Django ORM (Object Relational Mapping)

Django ORM (Object Relational Mapping) is a feature that allows you to interact with the database using **Python objects instead of writing SQL queries**.

It converts Python code into SQL behind the scenes.

---

## Core Components

### 1. Model

A Model represents a database table.

```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
```

---

### 2. Model Instance

Each object represents one row in the database.

```python
emp = Employee(name="Anubhav", salary=80000)
emp.save()
```

---

### 3. QuerySet

A QuerySet is a collection of database queries.

```python
employees = Employee.objects.all()
```

QuerySets are **lazy**, meaning the SQL query executes only when the data is actually needed.

---

## Common ORM Operations

### Create

```python
Employee.objects.create(
    name="Rahul",
    salary=50000
)
```

---

### Retrieve

```python
Employee.objects.all()

Employee.objects.get(id=1)

Employee.objects.filter(salary__gt=50000)
```

---

### Update

```python
emp = Employee.objects.get(id=1)
emp.salary = 90000
emp.save()
```

or

```python
Employee.objects.filter(id=1).update(salary=90000)
```

---

### Delete

```python
Employee.objects.get(id=1).delete()
```

---

## Why Use ORM?

- No need to write SQL
- Database independent (SQLite, MySQL, PostgreSQL, etc.)
- Prevents SQL Injection
- Cleaner and more readable code
- Faster development

---

## ORM Example

Model

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Query

```python
books = Book.objects.filter(author__name="Anubhav")
```

Equivalent SQL

```sql
SELECT *
FROM book
JOIN author
ON book.author_id = author.id
WHERE author.name = 'Anubhav';
```

---

## Interview Insight

**Does Django ORM execute queries immediately?**

No.

Django ORM uses **lazy evaluation**.

Example

```python
employees = Employee.objects.filter(salary__gt=50000)
```

No SQL is executed yet.

The query runs only when:

```python
for emp in employees:
    print(emp.name)
```

or

```python
list(employees)
```

---

## Advantages of ORM

- Easy CRUD operations
- Supports complex queries
- Database portability
- Built-in SQL injection protection
- Improves developer productivity

---

## Quick Summary

- Django ORM lets you interact with the database using Python code.
- **Model** → Database Table
- **Model Instance** → One Record (Row)
- **QuerySet** → Collection of Queries
- ORM is **lazy**, secure, and database-independent.
- It automatically converts Python code into SQL.

## What is a Django Model and how is it Defined?

A **Django Model** is a Python class that represents a **database table**.

Each attribute in the model represents a **column** in the table, and each object represents a **row** in the database.

All Django models inherit from `models.Model`.

---

## Basic Model Syntax

```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name
```

---

## Components of a Model

### Fields

Fields define the columns of the database table.

Example

```python
name = models.CharField(max_length=100)
salary = models.IntegerField()
joined_on = models.DateField()
```

Common Field Types

- CharField
- IntegerField
- BooleanField
- DateField
- DateTimeField
- EmailField
- ForeignKey
- ManyToManyField
- OneToOneField

---

### Meta Class

Used to configure model behavior.

```python
class Meta:
    ordering = ["name"]
    db_table = "employees"
```

Common Meta Options

- `db_table`
- `ordering`
- `verbose_name`
- `unique_together`

---

### Model Methods

Methods add custom functionality to the model.

```python
def __str__(self):
    return self.name
```

`__str__()` defines how the object appears in the Django Admin Panel.

---

## Example

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

Here,

- `Author` and `Book` are models.
- `ForeignKey` creates a **one-to-many relationship**.
- If an Author is deleted, all related Books are deleted because of `CASCADE`.

---

## Interview Insight

**What happens after creating a model?**

After defining a model, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the corresponding table in the database.

---

## Quick Summary

- A Django Model represents a **database table**.
- Each attribute represents a **table column**.
- Models inherit from `models.Model`.
- `Meta` is used for additional model configuration.
- `__str__()` provides a readable object representation.
- After creating a model, use **makemigrations** and **migrate** to apply changes.

## Describe the Purpose of Django's Admin Interface

The **Django Admin Interface** is a built-in web application that provides an easy way to **manage database records** without creating custom CRUD pages.

It is mainly used by **developers and administrators** to manage application data.

---

## Key Features

- Automatic CRUD operations
- Model-based interface
- Search and filtering
- Data validation
- Authentication & Permissions
- Relationship management (ForeignKey, ManyToMany)

---

## Registering a Model

```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```

Now the `Employee` model will appear in the Django Admin Panel.

---

## Custom Admin

```python
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "salary")
    search_fields = ("name",)
    list_filter = ("salary",)
```

This customizes how data appears in the admin panel.

---

## Admin URL

The admin interface is enabled through `urls.py`.

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

Access it at:

```
http://127.0.0.1:8000/admin/
```

---

## When to Use Admin?

- Internal admin dashboards
- Data management
- Testing and debugging
- Rapid prototyping
- Quick CRUD operations

---

## When Not to Use Admin?

- Customer-facing websites
- Complex business workflows
- Custom UI/UX requirements

For these cases, create your own **Views + Templates** or **DRF APIs**.

---

## Interview Insight

**Can Django Admin be customized?**

Yes.

Using `ModelAdmin`, you can customize:

- `list_display`
- `search_fields`
- `list_filter`
- `ordering`
- `readonly_fields`
- Custom actions

---

## Quick Summary

- Django Admin is a **built-in administration panel**.
- It provides automatic **CRUD operations** for models.
- Models are registered using `admin.site.register()`.
- It is ideal for **internal management**, not customer-facing applications.
- It can be customized using `ModelAdmin`.

## What is a Django View and how is it Created?

A **Django View** is a Python function or class that receives an HTTP request, processes it, and returns an HTTP response.

Views contain the **business logic** of the application.

---

## Types of Views

### 1. Function-Based View (FBV)

A simple Python function that handles requests.

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django")
```

---

### 2. Class-Based View (CBV)

A Python class that provides a structured way to handle different HTTP methods.

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):

    def get(self, request):
        return HttpResponse("GET Request")

    def post(self, request):
        return HttpResponse("POST Request")
```

---

## Mapping View to URL

Every view must be mapped in `urls.py`.

```python
from django.urls import path
from .views import home, HomeView

urlpatterns = [
    path("home/", home),
    path("dashboard/", HomeView.as_view()),
]
```

---

## Request Flow

```
Browser
    │
    ▼
urls.py
    │
    ▼
View
    │
    ▼
Model (if required)
    │
    ▼
Template / JSON
    │
    ▼
HTTP Response
```

---

## Function-Based View vs Class-Based View

| Feature | Function-Based View (FBV) | Class-Based View (CBV) |
|---------|----------------------------|-------------------------|
| Definition | Python Function | Python Class |
| Simplicity | Easy | Slightly Complex |
| Best For | Small applications | Medium & Large applications |
| Code Reusability | Less | More |
| HTTP Methods | if/else | Separate `get()`, `post()`, etc. |
| Inheritance | No | Yes |

---

## When to Use?

### Use FBV

- Simple APIs
- Small projects
- Less business logic

### Use CBV

- CRUD operations
- Large projects
- Reusable code
- Multiple HTTP methods

---

## Interview Insight

**Which one is preferred in production?**

For larger projects, **Class-Based Views (CBVs)** are generally preferred because they are reusable, support inheritance, and reduce code duplication.

For simple endpoints, **Function-Based Views (FBVs)** are perfectly acceptable and easier to understand.

---

## Quick Summary

- A **View** handles HTTP requests and returns HTTP responses.
- Views contain the application's business logic.
- Django supports **Function-Based Views (FBVs)** and **Class-Based Views (CBVs)**.
- Every view must be connected to a URL using `urls.py`.
- **FBVs** are simple, while **CBVs** are more reusable and scalable.

## Explain the Concept of URL Patterns in Django

URL patterns define **which View should handle a particular URL request**.

They are defined inside `urls.py` using `path()`, `re_path()`, and `include()`.

---

## Basic URL Pattern

```python
from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list),
]
```

Request

```
/employees/
```

will call

```python
views.employee_list
```

---

## URL Parameters

You can capture values directly from the URL.

```python
path("employees/<int:id>/", views.employee_detail)
```

Request

```
/employees/10/
```

View

```python
def employee_detail(request, id):
    return HttpResponse(id)
```

---

## `include()`

Used to split URLs into different apps.

Project `urls.py`

```python
urlpatterns = [
    path("employees/", include("employees.urls")),
]
```

App `urls.py`

```python
urlpatterns = [
    path("", views.employee_list),
]
```

---

## `path()` vs `re_path()`

| Feature | `path()` | `re_path()` |
|----------|-----------|-------------|
| Matching | Simple URLs | Regular Expressions |
| Readability | Easy | Complex |
| Recommended | Yes (Most Cases) | Only when regex is needed |

Example

```python
path("articles/<int:year>/", views.article)
```

```python
re_path(r"^articles/[0-9]{4}/$", views.article)
```

---

## Best Practices

- Keep URLs clean and meaningful.
- Use `include()` for app-level routing.
- Give URLs a `name` for reverse lookup.

```python
path("employees/", views.employee_list, name="employee-list")
```

---

## Interview Insight

**Why use named URLs?**

Named URLs allow you to use `reverse()` or `{% url %}` instead of hardcoding paths, making your application easier to maintain.

---

## Quick Summary

- URL patterns map **URLs to Views**.
- `path()` is used for most routing.
- `re_path()` is used for regex-based routing.
- `include()` keeps large projects modular.
- Use **named URLs** to avoid hardcoding paths.

## What is a Database Migration in Django?

A **migration** is Django's way of applying changes made in models to the database schema.

Whenever you create or modify a model, Django generates migration files that update the database accordingly.

---

## Why are Migrations Important?

- Keeps database schema in sync with models.
- Tracks database changes in Git.
- Makes deployments easier.
- Allows multiple developers to work on the same project.

---

## Migration Workflow

### Step 1: Create or Modify a Model

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
```

---

### Step 2: Generate Migration

```bash
python manage.py makemigrations
```

Creates a migration file.

---

### Step 3: Apply Migration

```bash
python manage.py migrate
```

Creates or updates the database tables.

---

## Useful Migration Commands

Generate migrations

```bash
python manage.py makemigrations
```

Apply migrations

```bash
python manage.py migrate
```

View migration status

```bash
python manage.py showmigrations
```

Rollback to a previous migration

```bash
python manage.py migrate app_name 0001
```

---

## Interview Insight

**What is the difference between `makemigrations` and `migrate`?**

| Command | Purpose |
|----------|---------|
| `makemigrations` | Creates migration files from model changes. |
| `migrate` | Executes those migration files on the database. |

---

## Quick Summary

- Migrations keep **models and database schema synchronized**.
- `makemigrations` creates migration files.
- `migrate` applies those changes to the database.
- `showmigrations` displays migration status.
- Migration files should be committed to Git.

## Explain the Difference Between `ForeignKey` and `ManyToManyField`

Both are used to create relationships between Django models, but they represent different types of relationships.

---

## ForeignKey (One-to-Many)

A `ForeignKey` means **one object belongs to one parent**, but a parent can have many child objects.

### Example

One **Department** can have many **Employees**, but an Employee belongs to only one Department.

```python
class Department(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
```

### Data

| Employee | Department |
|----------|------------|
| Anubhav | IT |
| Rahul | IT |
| Priya | HR |

Here,

- IT → Anubhav, Rahul
- HR → Priya
- One Employee cannot belong to multiple departments.

---

## ManyToManyField (Many-to-Many)

A `ManyToManyField` means **both models can have multiple relationships with each other**.

### Example

A **Student** can enroll in multiple **Courses**, and a **Course** can have many Students.

```python
class Course(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
```

### Data

| Student | Courses |
|----------|---------|
| Anubhav | Python, Django |
| Rahul | Django, React |
| Priya | Python |

Here,

- **Python** → Anubhav, Priya
- **Django** → Anubhav, Rahul

This is a **many-to-many** relationship.

---

## ManyToMany with Extra Fields (`through`)

Suppose employees work on multiple projects, and you also want to store **their role** in each project.

```python
class Employee(models.Model):
    name = models.CharField(max_length=100)


class Project(models.Model):
    name = models.CharField(max_length=100)


class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
```

### Data

| Employee | Project | Role |
|----------|---------|------|
| Anubhav | Banking App | Backend Developer |
| Anubhav | AI Chatbot | Team Lead |
| Rahul | Banking App | Frontend Developer |

The `Assignment` table stores the relationship **plus additional information (`role`)**.

---

## ForeignKey vs ManyToManyField

| Feature | ForeignKey | ManyToManyField |
|----------|------------|-----------------|
| Relationship | One-to-Many | Many-to-Many |
| Extra Table | No | Yes (Automatically Created) |
| One object linked to | One parent | Multiple objects |
| Example | Employee → Department | Student ↔ Course |

---

## Interview Insight

**When should you use `ForeignKey`?**

Use it when an object belongs to **only one parent**.

Example:

- Employee → Department
- Book → Author
- Order → Customer

**When should you use `ManyToManyField`?**

Use it when **both sides can have multiple relationships**.

Example:

- Student ↔ Course
- User ↔ Role
- Product ↔ Category

---

## Quick Summary

- `ForeignKey` = **One-to-Many** relationship.
- `ManyToManyField` = **Many-to-Many** relationship.
- `ManyToManyField` creates an intermediate table automatically.
- Use `through` when you need extra fields in the relationship.

## How do you define a Custom Model Field in Django?

A **Custom Model Field** is created when Django's built-in fields are not sufficient.

It allows you to define your own data type, validation, and database behavior.

---

## Basic Structure

```python
from django.db import models

class UpperCaseField(models.CharField):

    def to_python(self, value):
        if value:
            return value.upper()
        return value
```

Now use it like any other field.

```python
class Employee(models.Model):
    name = UpperCaseField(max_length=100)
```

If you save

```
anubhav
```

it becomes

```
ANUBHAV
```

---

## When do we create Custom Fields?

- Custom validation
- Custom data conversion
- Special business logic
- Custom database types

---

## Important Methods

| Method | Purpose |
|---------|---------|
| `to_python()` | Convert DB value to Python object |
| `get_prep_value()` | Convert Python object before saving |
| `db_type()` | Specify custom database type |

---

## Interview Insight

Most projects **do not require custom model fields**.

Usually, custom **validators**, **properties**, or **model methods** are enough.

---

## Quick Summary

- Custom fields extend Django's built-in fields.
- Used when built-in fields are insufficient.
- Common methods are `to_python()`, `get_prep_value()`, and `db_type()`.
- Rarely required in day-to-day Django development.

## What is a QuerySet in Django?

A **QuerySet** is a collection of database queries returned by Django ORM.

It allows you to retrieve, filter, update, and delete data using Python instead of SQL.

---

## Creating a QuerySet

```python
employees = Employee.objects.all()
```

This returns all employees.

---

## Common QuerySet Methods

### Get all records

```python
Employee.objects.all()
```

---

### Filter records

```python
Employee.objects.filter(salary__gt=50000)
```

---

### Get a single record

```python
Employee.objects.get(id=1)
```

---

### Exclude records

```python
Employee.objects.exclude(salary__lt=30000)
```

---

### Order data

```python
Employee.objects.order_by("-salary")
```

---

### Count records

```python
Employee.objects.count()
```

---

### Check if data exists

```python
Employee.objects.exists()
```

---

### Update records

```python
Employee.objects.filter(id=1).update(salary=90000)
```

---

### Delete records

```python
Employee.objects.filter(id=1).delete()
```

---

## QuerySet is Lazy

```python
employees = Employee.objects.filter(salary__gt=50000)
```

No SQL query is executed here.

The query runs only when you use the data.

```python
for emp in employees:
    print(emp.name)
```

or

```python
list(employees)
```

---

## `select_related()` vs `prefetch_related()`

| Method | Used For |
|----------|----------|
| `select_related()` | ForeignKey & OneToOneField |
| `prefetch_related()` | ManyToMany & Reverse ForeignKey |

Example

```python
Book.objects.select_related("author")
```

```python
Student.objects.prefetch_related("courses")
```

---

## Interview Insight

**Difference between `get()` and `filter()`?**

| `get()` | `filter()` |
|----------|------------|
| Returns one object | Returns a QuerySet |
| Raises exception if not found | Returns empty QuerySet if no match |
| Used when exactly one record is expected | Used for multiple records |

---

## Quick Summary

- A **QuerySet** represents database queries in Django.
- It is **lazy**, meaning SQL executes only when needed.
- Common methods are `all()`, `get()`, `filter()`, `exclude()`, `update()`, `delete()`, `count()`, and `exists()`.
- Use `select_related()` for **ForeignKey/OneToOne** and `prefetch_related()` for **ManyToMany** relationships.

## `select_related()` vs `prefetch_related()`

### Models

```python
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
```

---

## 1. `select_related()` (ForeignKey / OneToOne)

Without `select_related()`

```python
books = Book.objects.all()

for book in books:
    print(book.title, book.author.name)
```

Suppose there are **100 books**.

Queries executed:

```
1 query -> Fetch Books
100 queries -> Fetch each Author

Total = 101 Queries ❌
```

Using `select_related()`

```python
books = Book.objects.select_related("author")

for book in books:
    print(book.title, book.author.name)
```

Queries executed:

```
1 JOIN Query ✅
```

---

## 2. `prefetch_related()` (ManyToMany)

Without `prefetch_related()`

```python
students = Student.objects.all()

for student in students:
    print(student.name)

    for book in student.books.all():
        print(book.title)
```

Suppose there are **50 students**.

Queries:

```
1 query -> Students
50 queries -> Books for each student

Total = 51 Queries ❌
```

Using `prefetch_related()`

```python
students = Student.objects.prefetch_related("books")

for student in students:
    print(student.name)

    for book in student.books.all():
        print(book.title)
```

Queries:

```
1 query -> Students
1 query -> All Books

Total = 2 Queries ✅
```

---

## Easy Interview Trick

```
ForeignKey / OneToOne
        ↓
select_related()
        ↓
SQL JOIN
        ↓
1 Query


ManyToMany / Reverse FK
        ↓
prefetch_related()
        ↓
Separate Queries + Python Mapping
        ↓
2 Queries
```

## What is an API?

An **API (Application Programming Interface)** allows two applications to communicate with each other.

It defines **how a client sends a request and how the server responds**.

### Example

A mobile app requests:

```
GET /employees/1
```

API Response

```json
{
    "id": 1,
    "name": "Anubhav"
}
```

---

## Interview Insight

Think of an API as a **messenger** between the client and the server.

---

## Quick Summary

- API enables communication between applications.
- It defines requests and responses.

## What is a Web API?

A **Web API** is an API that works over the **HTTP/HTTPS protocol**.

It exposes data through URLs (endpoints).

Example

```
GET /api/employees/
POST /api/employees/
```

---

## Quick Summary

- Works over HTTP/HTTPS.
- Uses URLs (endpoints).
- Returns data, usually JSON.

## What is a REST API?

A **REST API** is a Web API that follows REST principles.

### Characteristics

- Stateless
- Uses HTTP methods (GET, POST, PUT, DELETE)
- Uses URLs to identify resources
- Usually returns JSON

Example

```
GET /employees/
POST /employees/
PUT /employees/1/
DELETE /employees/1/
```

---

## Quick Summary

- REST is an architectural style.
- Stateless.
- Uses HTTP methods.
- Usually returns JSON.

## What is an Endpoint?

An **Endpoint** is the URL through which an API can be accessed.

Example

```
GET /employees/
```

Here,

```
/employees/
```

is the endpoint.

---

## Quick Summary

- Endpoint = API URL.
- Each endpoint performs a specific operation.

## What are HTTP Verbs?

HTTP Verbs define **what action should be performed** on a resource.

| Method | Purpose |
|----------|---------|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update entire object |
| PATCH | Partial update |
| DELETE | Delete data |

Example

```
GET    /employees/
POST   /employees/
PUT    /employees/1/
PATCH  /employees/1/
DELETE /employees/1/
```

---

## Quick Summary

- HTTP methods define CRUD operations.
- GET = Read
- POST = Create
- PUT/PATCH = Update
- DELETE = Delete

## Difference between HTTP and HTTPS

| HTTP | HTTPS |
|------|-------|
| Not Secure | Secure |
| No Encryption | Encrypted using SSL/TLS |
| Port 80 | Port 443 |
| Faster | Slightly slower due to encryption |
| Used for testing | Used in production |

---

## Interview Insight

Always use **HTTPS** in production because it encrypts data between the client and the server.

---

## Quick Summary

- HTTP → Unsecured communication.
- HTTPS → Secure encrypted communication using SSL/TLS.
- Production applications should always use HTTPS.


## What are HTTP Status Codes?

HTTP Status Codes indicate the result of an HTTP request.

| Code | Meaning |
|------|---------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Error |
| 5xx | Server Error |

### Common Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 OK | Request successful |
| 201 Created | Resource created |
| 204 No Content | Success, no response body |
| 400 Bad Request | Invalid request |
| 401 Unauthorized | Authentication required |
| 403 Forbidden | Permission denied |
| 404 Not Found | Resource not found |
| 500 Internal Server Error | Server error |

---

## Quick Summary

- **2xx** → Success
- **3xx** → Redirect
- **4xx** → Client mistake
- **5xx** → Server mistake

## Difference Between Authentication and Authorization

| Authentication | Authorization |
|---------------|---------------|
| Verifies **who you are** | Verifies **what you can access** |
| Happens first | Happens after authentication |
| Uses username/password, JWT, OAuth | Uses roles and permissions |

### Example

- Login with username & password → **Authentication**
- Access Admin Dashboard → **Authorization**

---

## Interview Insight

**Authentication = Identity**

**Authorization = Permission**

---

## Quick Summary

- Authentication verifies the user.
- Authorization determines what the user is allowed to do.

## What is a Browsable API?

A **Browsable API** is a feature of **Django REST Framework (DRF)** that provides a **web-based interface** for testing APIs directly from the browser.

Instead of using Postman, you can send GET, POST, PUT, and DELETE requests from your browser.

Example

```
http://127.0.0.1:8000/api/employees/
```

---

## Benefits

- Easy API testing
- No need for Postman during development
- Great for debugging

---

## Quick Summary

- Built-in DRF feature.
- Browser-based API testing interface.
- Mainly used during development.

## What is CORS?

**CORS (Cross-Origin Resource Sharing)** is a security mechanism that allows a frontend hosted on one domain to access a backend hosted on another domain.

### Example

Frontend

```
http://localhost:3000
```

Backend

```
http://localhost:8000
```

Without CORS, the browser blocks the request.

---

## Quick Summary

- Allows communication between different origins.
- Controlled by the server using HTTP headers.

## How do you Fix CORS Error in Django?

The recommended way is to use **django-cors-headers**.

### Step 1: Install

```bash
pip install django-cors-headers
```

---

### Step 2: Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    "corsheaders",
]
```

---

### Step 3: Add Middleware

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]
```

---

### Step 4: Allow Frontend

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

---

## Interview Insight

During development, many developers use:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

**Never use this in production** because it allows requests from any origin.

---

## Quick Summary

- Install `django-cors-headers`.
- Add it to `INSTALLED_APPS`.
- Add `CorsMiddleware`.
- Configure `CORS_ALLOWED_ORIGINS`.
- Avoid `CORS_ALLOW_ALL_ORIGINS=True` in production.

## Difference Between Stateful and Stateless

A **Stateful** application remembers previous requests, while a **Stateless** application treats every request as a completely new request.

---

## Example

### Stateful (Session Authentication)

```
1. User logs in
        ↓
Server creates Session
        ↓
Session ID stored on Server
        ↓
Browser sends Session ID with every request
        ↓
Server checks its Session
```

Example

```
Login
↓

Server:
Session ID = ABC123

↓

GET /profile

Cookie:
sessionid=ABC123

↓

Server checks Session ID
↓

Returns Profile
```

The server **remembers** the user.

---

### Stateless (JWT Authentication)

```
1. User logs in
        ↓
Server generates JWT Token
        ↓
Client stores Token
        ↓
Client sends Token with every request
        ↓
Server validates Token
```

Example

```
Login
↓

JWT Token

↓

GET /profile

Authorization:
Bearer eyJhbGciOi...

↓

Server verifies Token

↓

Returns Profile
```

The server **does not remember** the user.

---

## Stateful vs Stateless

| Feature | Stateful | Stateless |
|----------|-----------|-----------|
| Stores user state | Server | Client (Token) |
| Session required | Yes | No |
| Server memory | Required | Not Required |
| Scalability | Lower | Higher |
| Best Example | Session Authentication | JWT Authentication |
| Every request | Depends on previous requests | Independent |

---

## Interview Insight

**Why are REST APIs Stateless?**

REST requires that **every request contains all the information needed** to process it.

The server should **not remember previous requests**.

This makes REST APIs easier to scale.

---

## Quick Summary

- **Stateful** → Server remembers the user (Session Authentication).
- **Stateless** → Server does not remember the user; the client sends a JWT/token with every request.
- Most modern REST APIs use **Stateless (JWT)** authentication.


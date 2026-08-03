# DRF Hands-on: Find Mistakes in this API

### What to Check
- Missing authentication
- Missing permissions
- No serializer validation
- Too many DB queries
- No pagination
- Poor error handling

**Interview Tip:** Mention security, validation, and performance.

---

# DRF Hands-on: Optimize this Serializer

### Improvements
- Use `ModelSerializer`
- Select only required fields
- Avoid nested serializers if unnecessary
- Use `select_related()` / `prefetch_related()`

### Example
```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]
```

---

# DRF Hands-on: Improve this QuerySet

### Improvements
- Use `select_related()`
- Use `prefetch_related()`
- Filter only required data
- Use `.only()` if needed

### Example
```python
Book.objects.select_related("author")
```

---

# DRF Hands-on: Explain the N+1 Query Problem

### Explanation
N+1 happens when Django executes one query for the main data and one extra query for each related object.

### Bad Example
```python
books = Book.objects.all()

for book in books:
    print(book.author.name)
```

### Solution
```python
Book.objects.select_related("author")
```

---

# DRF Hands-on: Remove Duplicate Queries

### Solution
- Use `select_related()`
- Use `prefetch_related()`
- Cache repeated queries

### Example
```python
Author.objects.prefetch_related("books")
```

---

# DRF Hands-on: Add Pagination

### Example
```python
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 10
```

---

# DRF Hands-on: Add JWT Authentication

### Settings
```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

### Request Header
```
Authorization: Bearer <token>
```

---

# DRF Hands-on: Add Permissions

### Example
```python
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):
    permission_classes = [IsAuthenticated]
```

---

# DRF Hands-on: Improve API Response Time

### Ways to Improve
- Optimize queries
- Add caching
- Use pagination
- Fetch only required fields
- Avoid unnecessary serializer nesting

---

# DRF Hands-on: Handle Transactions Correctly

### Example
```python
from django.db import transaction

with transaction.atomic():
    order.save()
    payment.save()
```

If one fails, everything rolls back.

---

# DRF Hands-on: Add Validation

### Example
```python
class UserSerializer(serializers.Serializer):
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Must be 18+")
        return value
```

---

# DRF Hands-on: Fix Race Conditions

### Solution
Use database transactions and row locking.

### Example
```python
with transaction.atomic():
    product = Product.objects.select_for_update().get(id=1)
    product.stock -= 1
    product.save()
```

---

# DRF Hands-on: Design a POST API

### Example
```
POST /api/users/
```

### Request
```json
{
    "name": "John",
    "email": "john@test.com"
}
```

### Response
```json
{
    "id": 1,
    "message": "User created"
}
```

---

# DRF Hands-on: Design a GET API

### Example
```
GET /api/users/1
```

### Response
```json
{
    "id": 1,
    "name": "John",
    "email": "john@test.com"
}
```

---

# DRF Hands-on: Design a File Upload API

### Endpoint
```
POST /api/upload/
```

### Serializer
```python
class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
```

### Request
```
multipart/form-data
```

---

# DRF Hands-on: Design a Login API

### Endpoint
```
POST /api/login/
```

### Request
```json
{
    "username": "john",
    "password": "123456"
}
```

### Response
```json
{
    "access": "<jwt_token>",
    "refresh": "<refresh_token>"
}
```

---

# Interview Tips

### N+1 Query
- Problem: Too many database queries
- Solution: `select_related()` / `prefetch_related()`

### Performance
- Optimize QuerySet
- Use Pagination
- Cache data
- Fetch only required fields

### Security
- JWT Authentication
- Permissions
- Input Validation

### Database
- `transaction.atomic()`
- `select_for_update()` for race conditions
# Explain the Django Request Lifecycle

### Explanation
The request lifecycle is the journey of an HTTP request through Django.

**Flow:**
```
Client
   ↓
URL Routing
   ↓
Middleware
   ↓
View
   ↓
Model (if needed)
   ↓
Template/Serializer
   ↓
Response
   ↓
Middleware
   ↓
Client
```

---

# Middleware

### Explanation
Middleware is code that runs before and after every request/response.

**Common Uses**
- Authentication
- Logging
- CORS
- Security

### Example
```python
class MyMiddleware:
    def __call__(self, request):
        response = self.get_response(request)
        return response
```

---

# Authentication

### Explanation
Authentication verifies **who the user is**.

**Common Types**
- Session Authentication
- JWT Authentication
- Token Authentication

---

# JWT Authentication

### Explanation
JWT (JSON Web Token) authenticates users using a signed token instead of sessions.

**Flow**
```
Login
   ↓
Server returns JWT
   ↓
Client stores token
   ↓
Token sent in Authorization header
```

### Example
```
Authorization: Bearer <token>
```

---

# Session Authentication

### Explanation
Uses server-side sessions.

- User logs in
- Session ID stored in cookie
- Server validates session

Best for web applications.

---

# Permissions

### Explanation
Permissions decide **what an authenticated user can do**.

**Examples**
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly

---

# Serializers

### Explanation
Serializers convert Django model objects to JSON and validate incoming data.

### Example
```python
class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
```

---

# ModelSerializer

### Explanation
Automatically creates serializer fields from a Django model.

### Example
```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
```

---

# GenericAPIView

### Explanation
Provides reusable functionality like:
- queryset
- serializer_class
- pagination
- filtering

Less code than APIView.

---

# APIView

### Explanation
Base DRF class for creating custom APIs.

You manually write GET, POST, PUT, DELETE methods.

### Example
```python
class UserView(APIView):
    def get(self, request):
        return Response({"msg": "Hello"})
```

---

# ViewSets

### Explanation
ViewSet groups CRUD operations into one class.

### Example
```python
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

---

# Routers

### Explanation
Routers automatically generate URLs for ViewSets.

### Example
```python
router.register("users", UserViewSet)
```

---

# ORM Optimization

### Explanation
Reduce database queries to improve performance.

**Common methods**
- select_related()
- prefetch_related()
- only()
- defer()

---

# select_related()

### Explanation
Fetches related ForeignKey objects using SQL JOIN.

Best for **ForeignKey** and **OneToOne**.

### Example
```python
Book.objects.select_related("author")
```

---

# prefetch_related()

### Explanation
Fetches related objects using separate queries.

Best for **ManyToMany** and reverse ForeignKey.

### Example
```python
Author.objects.prefetch_related("books")
```

---

# annotate()

### Explanation
Adds calculated fields to each object.

### Example
```python
Book.objects.annotate(total=Count("reviews"))
```

---

# aggregate()

### Explanation
Returns a single summarized value.

### Example
```python
Book.objects.aggregate(Avg("price"))
```

---

# transaction.atomic()

### Explanation
Makes multiple database operations execute as one transaction.

If one fails, everything rolls back.

### Example
```python
with transaction.atomic():
    user.save()
    profile.save()
```

---

# Signals

### Explanation
Signals execute code automatically when certain events occur.

Common signals:
- post_save
- pre_save
- post_delete

### Example
```python
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    pass
```

---

# Custom Middleware

### Explanation
Middleware written for project-specific tasks.

### Example
```python
class LogMiddleware:
    def __call__(self, request):
        print(request.path)
        return self.get_response(request)
```

---

# Pagination

### Explanation
Returns data in smaller pages instead of all records.

### Example
```
GET /users?page=2
```

---

# Filtering

### Explanation
Returns records matching conditions.

### Example
```
GET /users?department=IT
```

---

# Searching

### Explanation
Searches records using keywords.

### Example
```
GET /users?search=john
```

---

# Caching

### Explanation
Stores frequently used data in memory to improve performance.

Common backends:
- Redis
- Memcached

### Example
```python
cache.set("key", value)
```

---

# Celery

### Explanation
Celery executes background tasks asynchronously.

**Use Cases**
- Sending emails
- Reports
- Notifications

---

# Redis

### Explanation
Redis is an in-memory database.

Used for:
- Cache
- Celery Broker
- Sessions

---

# File Upload APIs

### Explanation
DRF supports uploading files using serializers.

### Example
```python
class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
```

---

# Rate Limiting

### Explanation
Limits how many API requests a client can make.

Example:
```
100 requests/minute
```

---

# Versioning

### Explanation
Supports multiple API versions.

### Example
```
/api/v1/users/
/api/v2/users/
```

---

# Custom Permissions

### Explanation
Create your own permission logic.

### Example
```python
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
```

---

# Logging

### Explanation
Stores application events for debugging and monitoring.

**Logs**
- Errors
- Requests
- Exceptions

### Example
```python
import logging

logger = logging.getLogger(__name__)
logger.info("User logged in")
```

---

# Exception Handling

### Explanation
Handles errors gracefully and returns proper HTTP responses.

### Example
```python
try:
    user.save()
except Exception:
    return Response({"error": "Failed"})
```

---

# DRF Throttling

### Explanation
Throttling limits API requests to prevent abuse.

**Built-in Classes**
- AnonRateThrottle
- UserRateThrottle
- ScopedRateThrottle

### Example
```python
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle"
    ],
    "DEFAULT_THROTTLE_RATES": {
        "user": "100/day"
    }
}
```

**Interview Tip:**  
- **Authentication** → Who are you?  
- **Permissions** → What can you do?  
- **Throttling/Rate Limiting** → How often can you do it?
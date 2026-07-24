# Backend Interview Questions

---

# 1. Explain REST APIs

## Answer

REST (Representational State Transfer) is an architectural style used to build web services that allow communication between a client and a server using HTTP methods.

The client sends an HTTP request, and the server processes it and returns an HTTP response, usually in JSON format.

```
React Frontend
      |
HTTP Request
      |
Django REST API
      |
Database
```

### Common HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve Data |
| POST | Create Data |
| PUT | Update Entire Record |
| PATCH | Partial Update |
| DELETE | Delete Data |

### Example

### GET

```
GET /api/employees/
```

Response

```json
[
    {
        "id":1,
        "name":"Anubhav"
    }
]
```

---

### POST

```
POST /api/employees/
```

Request

```json
{
    "name":"Rahul",
    "salary":50000
}
```

---

### PUT

```
PUT /api/employees/1/
```

Updates the entire resource.

---

### PATCH

```
PATCH /api/employees/1/
```

Updates only selected fields.

---

### DELETE

```
DELETE /api/employees/1/
```

Deletes the employee.

### Characteristics of REST APIs

- Stateless
- Client-Server Architecture
- Uses HTTP Methods
- Uses JSON/XML
- Cacheable
- Uniform Interface

### Interview One-Liner

REST APIs are stateless web services that allow communication between clients and servers using HTTP methods like GET, POST, PUT, PATCH, and DELETE.

---

# 2. Explain Authentication

## Answer

Authentication is the process of verifying the identity of a user.

It answers the question:

> **Who are you?**

Example

```
Username + Password
        ↓
Authentication
        ↓
User Verified
```

### Types of Authentication

- Session Authentication
- Token Authentication
- JWT Authentication
- OAuth Authentication
- API Key Authentication

### Django Example

```python
from django.contrib.auth import authenticate

user = authenticate(
    username="admin",
    password="password123"
)

if user:
    print("Login Successful")
```

### Authentication vs Authorization

| Authentication | Authorization |
|---------------|---------------|
| Who are you? | What are you allowed to access? |
| Login | Permissions |
| Happens first | Happens after authentication |

### Interview One-Liner

Authentication verifies a user's identity before allowing access to the application.

---

# 3. Explain JWT (JSON Web Token)

## Answer

JWT (JSON Web Token) is a token-based authentication mechanism commonly used in REST APIs.

Instead of storing sessions on the server, the server returns a token after successful login.

The client sends this token with every request.

```
Login
   ↓
Server verifies credentials
   ↓
Server generates JWT
   ↓
Client stores JWT
   ↓
Client sends JWT in every request
```

### Request Header

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### JWT Structure

```
Header
   .
Payload
   .
Signature
```

### Django Example

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view()
    ),
]
```

### Advantages

- Stateless
- Fast
- Scalable
- Suitable for REST APIs
- Works well with React, Angular, Mobile Apps

### Disadvantages

- Cannot easily invalidate before expiry
- Token size is larger than session IDs
- Must be stored securely

### Interview One-Liner

JWT is a stateless authentication mechanism where the server issues a signed token that the client sends with every request.

---

# 4. Explain Docker

## Answer

Docker is a containerization platform that packages an application along with its dependencies so it runs consistently across different environments.

Instead of saying

> "It works on my machine."

Docker ensures

> "It works everywhere."

```
Application
+ Python
+ Django
+ Libraries
+ Dependencies
------------------
Docker Container
```

### Dockerfile Example

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
```

### Common Docker Commands

Build Image

```bash
docker build -t myapp .
```

Run Container

```bash
docker run -p 8000:8000 myapp
```

List Containers

```bash
docker ps
```

Stop Container

```bash
docker stop <container_id>
```

### Advantages

- Consistent Environment
- Easy Deployment
- Lightweight
- Faster than Virtual Machines
- Easy Scaling

### Interview One-Liner

Docker packages an application and all its dependencies into a container, ensuring it runs consistently across different environments.

---

# 5. Explain CI/CD

## Answer

CI/CD stands for

- **CI** → Continuous Integration
- **CD** → Continuous Delivery / Continuous Deployment

It automates building, testing, and deploying applications.

```
Developer
     |
Push Code
     |
GitHub
     |
CI Pipeline
     |
Build
     |
Run Tests
     |
Deploy
     |
Production
```

### Continuous Integration (CI)

Every code commit automatically

- Builds the application
- Runs Unit Tests
- Detects bugs early

### Continuous Delivery (CD)

Application is automatically prepared for deployment.

Deployment requires manual approval.

### Continuous Deployment

Every successful build is deployed automatically.

### Common CI/CD Tools

- GitHub Actions
- Jenkins
- GitLab CI/CD
- Azure DevOps
- CircleCI

### Example GitHub Actions

```yaml
name: Django CI

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - run: pip install -r requirements.txt

      - run: python manage.py test
```

### Benefits

- Faster Releases
- Automated Testing
- Reduced Human Errors
- Continuous Delivery

### Interview One-Liner

CI/CD automates building, testing, and deploying applications, making software delivery faster and more reliable.

---

# 6. Explain Deployment Basics and AWS

## Answer

Deployment is the process of moving an application from the development environment to a production server so that users can access it.

Typical deployment flow

```
Developer
     ↓
GitHub
     ↓
CI/CD Pipeline
     ↓
Build Docker Image
     ↓
Deploy to Server / AWS
     ↓
Users Access Application
```

### Basic Deployment Steps

1. Push code to GitHub.
2. Install dependencies.
3. Run database migrations.
4. Collect static files (Django).
5. Configure environment variables.
6. Start the application server.
7. Configure reverse proxy (Nginx).
8. Monitor logs and application health.

### Common AWS Services

| Service | Purpose |
|----------|----------|
| EC2 | Virtual Server to host applications |
| S3 | Store static files, images and backups |
| RDS | Managed MySQL/PostgreSQL database |
| IAM | Manage users, roles and permissions |
| VPC | Private network for AWS resources |
| CloudWatch | Logs, monitoring and alerts |
| Route 53 | DNS and domain management |
| Elastic Load Balancer (ELB) | Distributes traffic across servers |
| Auto Scaling | Automatically increases or decreases servers based on traffic |
| ECS / EKS | Run Docker containers |

### Django Deployment Example

```
React Frontend
       |
Nginx
       |
Gunicorn
       |
Django
       |
PostgreSQL (AWS RDS)
       |
Static Files (AWS S3)
```

### Interview One-Liner

Deployment is the process of making an application available to users. On AWS, services like EC2, S3, RDS, IAM, CloudWatch, and Load Balancers are commonly used to build secure, scalable, and reliable applications.

---

# Interview Summary

| Topic | Interview Answer |
|--------|------------------|
| REST APIs | Stateless APIs that use HTTP methods like GET, POST, PUT, PATCH, and DELETE to communicate between client and server. |
| Authentication | Verifies a user's identity before granting access to the application. |
| JWT | A stateless token-based authentication mechanism where the client sends a signed token with every request. |
| Docker | Packages an application and its dependencies into containers for consistent execution across environments. |
| CI/CD | Automates building, testing, and deploying applications for faster and more reliable releases. |
| Deployment & AWS | Deployment makes an application available to users. AWS services like EC2, RDS, S3, IAM, CloudWatch, ELB, and Auto Scaling help build scalable cloud applications. |
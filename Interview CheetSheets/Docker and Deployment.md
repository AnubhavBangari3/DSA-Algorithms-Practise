# Docker / Deployment Interview Notes

## 1. Docker

### What is Docker?

Docker is used to package an application along with its dependencies so that it runs the same way on every environment.

### Use

* Package application with dependencies
* Avoid "works on my machine" issues
* Easy deployment
* Easy environment setup

### Example

For a Django application:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Basic Steps

```bash
# Build image
docker build -t myapp .

# Run container
docker run -p 8000:8000 myapp

# Check running containers
docker ps

# Stop container
docker stop <container_id>
```

### Interview Answer

> I use Docker to containerize my backend application with all required dependencies. I create a Dockerfile, build the image, test it locally, and then deploy the container to a cloud platform.

---

# 2. Azure App Service

### What is Azure App Service?

Azure App Service is a managed platform used to deploy web applications and REST APIs without managing servers manually.

### Use

* Deploy Django / Flask / Node.js applications
* Automatic scaling
* Environment variables
* Logging and monitoring
* HTTPS support

### Example

I can deploy a Django REST API to Azure App Service.

```text
Django Application
        ↓
GitHub / Docker Image
        ↓
Azure App Service
        ↓
Public API URL
```

### Basic Steps

1. Create an App Service in Azure.
2. Select runtime like Python or Docker.
3. Configure deployment source.
4. Add environment variables.
5. Configure startup command.
6. Deploy application.
7. Test the public URL.

### Django Startup Command

```bash
gunicorn project.wsgi:application
```

### Interview Answer

> I used Azure App Service to deploy Django REST APIs. I configured environment variables, database connection settings, startup commands, and deployed the backend as a managed web application.

---

# 3. Azure Blob Storage

### What is Azure Blob Storage?

Azure Blob Storage is object storage used for storing files such as images, PDFs, videos, CSV files, and uploaded documents.

### Use

* Store user uploads
* Store images
* Store generated reports
* Store SWIFT files
* Store large static files

### Example

```text
User uploads SWIFT file
        ↓
Django API
        ↓
Azure Blob Storage
        ↓
Blob URL stored in database
```

### Basic Steps

1. Create a Storage Account.
2. Create a Blob Container.
3. Get connection credentials.
4. Configure them in the application.
5. Upload files using Azure SDK.
6. Store the blob URL or file path.

### Python Example

```python
from azure.storage.blob import BlobServiceClient

connection_string = "AZURE_CONNECTION_STRING"

blob_service = BlobServiceClient.from_connection_string(
    connection_string
)

container = blob_service.get_container_client("uploads")

with open("sample.txt", "rb") as file:
    container.upload_blob(
        name="sample.txt",
        data=file,
        overwrite=True
    )
```

### Interview Answer

> I use Azure Blob Storage for storing uploaded files and generated assets. The backend uploads files to Blob Storage and stores the blob URL or file reference in the database.

---

# 4. Azure SQL

### What is Azure SQL?

Azure SQL is Microsoft's managed cloud relational database based on SQL Server.

### Use

* Store structured application data
* User data
* Transactions
* Application records
* Relationships between tables

### Example

```text
Django Backend
      ↓
Azure SQL
      ↓
Users
Trades
SWIFT Messages
Audit Logs
```

### Basic Steps

1. Create Azure SQL Server.
2. Create SQL Database.
3. Configure firewall/network rules.
4. Create username and password.
5. Add database connection details to Django.
6. Run migrations.

### Django Example

```python
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "mydb",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "myserver.database.windows.net",
        "PORT": "1433",
    }
}
```

### Run Migrations

```bash
python manage.py migrate
```

### Interview Answer

> I use Azure SQL as the relational database for storing structured application data. The Django backend connects to it using environment-based database credentials and Django ORM.

---

# 5. Google Cloud Run

### What is Google Cloud Run?

Google Cloud Run is a serverless platform used to deploy Docker containers.

### Use

* Deploy containerized APIs
* Automatic scaling
* Pay only when application is running
* No server management
* HTTPS endpoint automatically provided

### Example

```text
Django REST API
      ↓
Docker Container
      ↓
Google Cloud Run
      ↓
Public HTTPS API
```

### Basic Steps

1. Create Dockerfile.
2. Build Docker image.
3. Push image to Google Artifact Registry.
4. Deploy image to Cloud Run.
5. Configure environment variables.
6. Allow authentication or public access.
7. Test generated URL.

### Example Command

```bash
gcloud run deploy my-api \
  --source . \
  --region asia-south1
```

### Important Cloud Run Point

Cloud Run expects the application to listen on the provided port.

```python
PORT = 8080
```

Example Gunicorn command:

```bash
gunicorn project.wsgi:application \
  --bind 0.0.0.0:$PORT
```

### Interview Answer

> I used Google Cloud Run to deploy containerized Django APIs. I built the Docker image, deployed it to Cloud Run, configured environment variables, and exposed the API using the generated HTTPS endpoint.

---

# 6. Google Cloud Storage

### What is Google Cloud Storage?

Google Cloud Storage is object storage used to store files such as images, audio, videos, and documents.

### Use

* Images
* Audio
* PDFs
* User uploads
* Generated AI media

### Example

```text
Gemini generates story
        ↓
Imagen generates image
        ↓
Google Cloud Storage
        ↓
Image URL returned to frontend
```

### Basic Steps

1. Create a GCP project.
2. Create a Storage Bucket.
3. Configure permissions.
4. Create service account credentials.
5. Connect application using Google Cloud SDK.
6. Upload files.
7. Generate public or signed URLs.

### Python Example

```python
from google.cloud import storage

client = storage.Client()

bucket = client.bucket("my-bucket")

blob = bucket.blob("images/story.png")

blob.upload_from_filename("story.png")
```

### Signed URL

Signed URLs allow temporary secure access to private files.

```text
Private File
    ↓
Generate Signed URL
    ↓
Temporary Access
```

### Interview Answer

> I use Google Cloud Storage for generated media such as images and audio. The backend uploads the files to a bucket and returns either a public URL or a signed URL to the frontend.

---

# 7. Vercel

### What is Vercel?

Vercel is a cloud platform mainly used to deploy frontend applications, especially Next.js.

### Use

* Deploy Next.js
* Deploy React frontend
* Automatic deployment from GitHub
* HTTPS
* CDN
* Environment variables

### Example

```text
GitHub
   ↓
Vercel
   ↓
Next.js Frontend
   ↓
Calls Django Backend API
```

### Basic Steps

1. Push frontend code to GitHub.
2. Login to Vercel.
3. Import GitHub repository.
4. Configure environment variables.
5. Click Deploy.
6. Vercel builds and deploys automatically.

### Example Environment Variable

```env
NEXT_PUBLIC_API_URL=https://api.example.com
```

### Interview Answer

> I use Vercel mainly for deploying Next.js frontends. I connect the GitHub repository, configure environment variables, and Vercel automatically builds and deploys the frontend.

---

# 8. Render

### What is Render?

Render is a cloud platform used to deploy backend applications, frontend applications, databases, and background services.

### Use

* Deploy Django API
* Deploy Flask or FastAPI
* PostgreSQL hosting
* Background workers
* Simple GitHub-based deployment

### Example

```text
GitHub
   ↓
Render
   ↓
Django Backend
   ↓
Render PostgreSQL
```

### Basic Steps

1. Push code to GitHub.
2. Create a Web Service in Render.
3. Connect GitHub repository.
4. Add build command.
5. Add start command.
6. Configure environment variables.
7. Deploy.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn project.wsgi:application
```

### Interview Answer

> I use Render when I want quick deployment of Django applications. I connect the GitHub repository, configure build and startup commands, add environment variables, and deploy the service.

---

# Docker vs Cloud Platforms

| Technology           | Main Use                               |
| -------------------- | -------------------------------------- |
| Docker               | Package application                    |
| Azure App Service    | Deploy backend/web application         |
| Azure Blob Storage   | Store files                            |
| Azure SQL            | Relational database                    |
| Google Cloud Run     | Deploy Docker containers               |
| Google Cloud Storage | Store files/media                      |
| Vercel               | Deploy Next.js frontend                |
| Render               | Deploy backend/full-stack applications |

---

# Simple Deployment Architecture Example

```text
User
 ↓
Vercel
Next.js Frontend
 ↓
Django REST API
 ↓
Cloud Run / Azure App Service
 ↓
Database
Azure SQL / PostgreSQL
 ↓
File Storage
Azure Blob / Google Cloud Storage
```

---

# Common Interview Question: How Do You Deploy a Django Application?

### Answer

```text
1. Push code to GitHub.
2. Create requirements.txt.
3. Configure environment variables.
4. Create Dockerfile if required.
5. Build and test Docker container locally.
6. Deploy backend to Cloud Run / Azure App Service / Render.
7. Configure database.
8. Run Django migrations.
9. Configure static/media storage.
10. Deploy frontend to Vercel.
11. Configure frontend API URL.
12. Test APIs and application.
```

### Short Interview Answer

> I first prepare the Django application with requirements, environment variables, and production settings. If required, I containerize it using Docker. Then I deploy the backend to Cloud Run or Azure App Service, configure the database and storage, run migrations, and finally deploy the Next.js frontend on Vercel.

---

# Important Deployment Commands

```bash
# Generate requirements
pip freeze > requirements.txt

# Django checks
python manage.py check

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Build Docker image
docker build -t myapp .

# Run Docker container
docker run -p 8000:8000 myapp

# Production Django server
gunicorn project.wsgi:application
```

---

# One-Line Revision

```text
Docker → Package the application.

Azure App Service → Deploy web/backend applications.

Azure Blob Storage → Store files and documents.

Azure SQL → Managed relational database.

Google Cloud Run → Run Docker containers serverlessly.

Google Cloud Storage → Store images, audio and files.

Vercel → Deploy Next.js frontend.

Render → Simple backend and database deployment.
```

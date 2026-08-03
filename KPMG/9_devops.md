# Git: Git Merge

### Explanation
Combines changes from one branch into another.

### Example
```bash
git checkout main
git merge feature
```

---

# Git: Git Rebase

### Explanation
Moves your branch commits on top of another branch, creating a cleaner history.

### Example
```bash
git checkout feature
git rebase main
```

**Merge vs Rebase**
- **Merge** → Preserves history.
- **Rebase** → Creates a linear history.

---

# Git: Cherry Pick

### Explanation
Copies a specific commit from one branch to another.

### Example
```bash
git cherry-pick <commit_id>
```

---

# Git: Resolve Merge Conflicts

### Steps
1. Open conflicting file.
2. Remove conflict markers.
3. Keep the correct code.
4. Commit the changes.

### Example
```bash
git add .
git commit
```

---

# Git: Git Stash

### Explanation
Temporarily saves uncommitted changes.

### Example
```bash
git stash
git stash pop
```

---

# Git: Git Reset vs Revert

| Reset | Revert |
|--------|--------|
| Removes commits | Creates a new commit to undo changes |
| Rewrites history | Keeps history |
| Use for local commits | Use for shared branches |

### Example
```bash
git reset HEAD~1

git revert HEAD
```

---

# Git: Branching Strategy

### Common Branches
- `main` → Production
- `develop` → Development
- `feature/*` → New features
- `bugfix/*` → Bug fixes
- `release/*` → Release preparation

---

# Docker: Dockerfile

### Explanation
A Dockerfile contains instructions to build a Docker image.

### Example
```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]
```

---

# Docker: Docker Compose

### Explanation
Runs multiple containers together.

### Example
```yaml
services:
  web:
    build: .

  db:
    image: postgres
```

---

# Docker: Multi-stage Builds

### Explanation
Uses multiple build stages to reduce final image size.

### Example
```dockerfile
FROM python:3.12 AS builder

FROM python:3.12-slim
COPY --from=builder /app /app
```

---

# Docker: Volumes

### Explanation
Volumes store data outside the container so it persists even if the container is deleted.

### Example
```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

---

# Docker: Networks

### Explanation
Networks allow containers to communicate with each other.

### Example
```yaml
services:
  web:
  db:
```

The `web` container can connect to `db`.

---

# Docker: Environment Variables

### Explanation
Store configuration without hardcoding values.

### Example
```yaml
environment:
  - DEBUG=True
```

or

```env
SECRET_KEY=abc123
```

---

# Docker: Container Lifecycle

### Lifecycle
```
Create
   ↓
Start
   ↓
Running
   ↓
Stop
   ↓
Restart/Delete
```

---

# Cloud: What is AWS?

### Explanation
AWS (Amazon Web Services) is a cloud platform providing compute, storage, databases, networking, AI, and many other services.

---

# Cloud: EC2

### Explanation
EC2 (Elastic Compute Cloud) provides virtual servers in the cloud.

**Use Case**
- Host websites
- Run applications

---

# Cloud: S3

### Explanation
S3 (Simple Storage Service) stores files and objects.

**Use Cases**
- Images
- Videos
- Backups
- Static websites

---

# Cloud: Load Balancer

### Explanation
Distributes incoming traffic across multiple servers to improve availability and performance.

```
Users
   ↓
Load Balancer
   ↓
Server1  Server2  Server3
```

---

# Cloud: Auto Scaling

### Explanation
Automatically increases or decreases the number of servers based on traffic.

**Benefit**
- Saves cost
- Handles high traffic

---

# Cloud: Google Cloud Run

### Explanation
Cloud Run is a serverless service that deploys and runs containers without managing servers.

**Best For**
- APIs
- Microservices

---

# Cloud: Azure App Service

### Explanation
Azure App Service is a Platform as a Service (PaaS) used to deploy web applications and REST APIs.

**Supports**
- Python
- Django
- Node.js
- .NET
- Java

---

# Cloud: Azure Blob Storage

### Explanation
Blob Storage stores unstructured data like images, videos, PDFs, and backups.

**Use Cases**
- File uploads
- Media storage
- Logs

---

# Cloud: CDN

### Explanation
CDN (Content Delivery Network) caches content on servers close to users for faster delivery.

**Examples**
- Images
- CSS
- JavaScript
- Videos

---

# Cloud: VPC Basics

### Explanation
A VPC (Virtual Private Cloud) is a private network inside the cloud.

It lets you control:
- IP addresses
- Subnets
- Firewalls
- Security Groups

---

# Interview Tips

## Merge vs Rebase

| Merge | Rebase |
|--------|--------|
| Keeps commit history | Creates clean linear history |
| Safer for shared branches | Best before merging feature branch |

---

## Reset vs Revert

- **Reset** → Deletes/rewrites commits.
- **Revert** → Safely undoes changes with a new commit.

---

## S3 vs EC2

| EC2 | S3 |
|-----|----|
| Virtual Server | Object Storage |
| Runs applications | Stores files |

---

## Azure App Service vs Cloud Run

| Azure App Service | Cloud Run |
|-------------------|-----------|
| Deploy web apps directly | Deploy Docker containers |
| PaaS | Serverless Containers |
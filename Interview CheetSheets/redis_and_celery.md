# Redis / Celery Interview Notes

---

# 1. What is Redis?

### Answer

Redis is an **in-memory key-value database** used for **caching**, **message brokering**, and **fast data access**.

Since it stores data in RAM, it is much faster than traditional databases.

### Uses

* Caching
* Session storage
* Rate limiting
* Queue management
* Celery Message Broker
* Pub/Sub
* Real-time applications

### Example

```text
User requests dashboard
        ↓
Check Redis Cache
        ↓
Found? → Return immediately
Not Found? → Fetch from DB → Store in Redis → Return
```

---

# 2. What is Celery?

### Answer

Celery is a distributed task queue used to execute long-running tasks asynchronously in the background.

Instead of making users wait, the task runs separately while the API responds immediately.

### Uses

* Send emails
* Generate reports
* Image processing
* AI model inference
* File uploads
* Notifications
* Scheduled jobs

---

# 3. Why do we use Redis with Celery?

### Answer

Celery needs a **message broker** to store tasks.

Redis acts as the broker.

```text
Django API
     ↓
Send Task
     ↓
Redis Queue
     ↓
Celery Worker
     ↓
Execute Task
```

---

# 4. What is a Background Task?

### Answer

A background task is a task that runs separately from the main request.

The user gets an immediate response while the work continues in the background.

### Example

Instead of making the user wait 30 seconds for a PDF:

```text
User clicks Generate Report
        ↓
API returns "Processing..."
        ↓
Celery generates PDF
        ↓
Store PDF
        ↓
Notify User
```

---

# 5. What is Async Processing?

### Answer

Async processing means executing tasks without blocking the main application.

The API remains responsive while long-running operations execute separately.

### Example

Without Async

```text
User Request
      ↓
Generate Report (30 sec)
      ↓
Return Response
```

With Async

```text
User Request
      ↓
Create Celery Task
      ↓
Return Response Immediately

Background:
Redis
   ↓
Celery
   ↓
Generate Report
```

---

# 6. Difference between Sync and Async

| Synchronous         | Asynchronous                   |
| ------------------- | ------------------------------ |
| Waits for task      | Doesn't wait                   |
| User blocks         | User gets response immediately |
| Slow for long tasks | Better user experience         |
| Simple              | Better scalability             |

---

# 7. What is a Message Broker?

### Answer

A message broker temporarily stores tasks until a worker processes them.

Redis is commonly used as the broker.

```text
API
 ↓
Broker (Redis)
 ↓
Worker (Celery)
```

---

# 8. What is a Celery Worker?

### Answer

A Celery Worker is a separate process that continuously listens for new tasks in Redis and executes them.

---

# 9. Explain Redis + Celery Flow

```text
User uploads image
        ↓
Django API
        ↓
Create Celery Task
        ↓
Redis Queue
        ↓
Celery Worker
        ↓
Resize Image
        ↓
Save Image
        ↓
Update Database
```

---

# 10. Give a Real Project Example

### Wexa Analytics

* User schedules report
* API creates Celery task
* Redis stores task
* Celery generates PDF
* Report becomes available for download

---

### Creative Storyteller

* User requests story
* Images generated
* Audio generated
* Media uploaded
* These heavy tasks can run in the background using Celery

---

### SEO Audit System

* User starts website audit
* Celery crawls pages
* Generates audit report
* User doesn't wait for completion

---

# 11. Why not execute everything inside the API?

### Answer

If heavy tasks run inside the API:

* Slow response
* Request timeout
* Poor user experience
* Less scalability

Background processing solves these problems.

---

# 12. What happens if Redis is down?

### Answer

Celery cannot receive new tasks because the broker is unavailable.

Existing running tasks may continue, but new tasks cannot be queued until Redis is available again.

---

# 13. Can Celery work without Redis?

### Answer

Yes.

Celery supports multiple brokers.

Examples:

* Redis
* RabbitMQ
* Amazon SQS

Redis is popular because it is simple and fast.

---

# 14. Why choose Redis over RabbitMQ?

### Interview Answer

Redis

* Easy to configure
* Very fast
* Good for most applications

RabbitMQ

* More advanced routing
* Better for enterprise messaging
* Supports complex queues

For most Django projects, Redis is sufficient.

---

# 15. What kinds of tasks should use Celery?

Good examples:

* Send emails
* Generate reports
* Export Excel
* AI inference
* Image processing
* Video processing
* Notifications
* Data import/export

Avoid using Celery for:

* Simple CRUD operations
* Quick database queries
* Small validations

---

# 16. How does Django call a Celery task?

Instead of:

```python
send_email(user)
```

Use:

```python
send_email.delay(user.id)
```

`.delay()` sends the task to Redis.

---

# 17. Basic Celery Task

```python
from celery import shared_task

@shared_task
def send_email(user_id):
    print(f"Sending email to {user_id}")
```

Calling the task

```python
send_email.delay(10)
```

---

# 18. Start Redis

```bash
redis-server
```

---

# 19. Start Celery Worker

```bash
celery -A project worker --loglevel=info
```

---

# 20. Start Celery Beat (Scheduled Tasks)

```bash
celery -A project beat --loglevel=info
```

---

# 21. What is Celery Beat?

### Answer

Celery Beat is the scheduler.

It automatically triggers tasks at specific intervals.

### Example

Every day at 9 AM

* Generate reports
* Send reminder emails
* Clean expired sessions

---

# 22. Difference between Worker and Beat

| Worker            | Beat                   |
| ----------------- | ---------------------- |
| Executes tasks    | Schedules tasks        |
| Runs continuously | Triggers tasks on time |
| Processes queue   | Creates scheduled jobs |

---

# 23. Interview Question

### Why did you use Redis?

**Answer**

> I used Redis as an in-memory cache and as the Celery message broker. It improves performance and allows background tasks to execute asynchronously.

---

# 24. Interview Question

### Why did you use Celery?

**Answer**

> I used Celery for long-running tasks like report generation, notifications, and file processing so that users receive an immediate API response while heavy work executes in the background.

---

# 25. Interview Question

### Explain Redis + Celery in one minute.

**Answer**

> When a request needs a heavy operation, the Django API doesn't execute it directly. Instead, it sends a task to Redis using Celery. Redis stores the task in a queue, and a Celery Worker picks it up and executes it in the background. This keeps the API fast and improves scalability.

---

# Quick Revision

```text
Redis
→ In-memory database
→ Cache
→ Message Broker

Celery
→ Background task queue

Redis + Celery
→ Django creates task
→ Redis stores task
→ Celery Worker executes task

Celery Beat
→ Scheduler

Worker
→ Executes tasks

Common Uses
→ Emails
→ Reports
→ Image Processing
→ AI Tasks
→ Notifications
→ Scheduled Jobs
```

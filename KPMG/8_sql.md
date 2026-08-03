# SQL: Joins

### Explanation
Joins combine data from multiple tables.

| Join | Purpose |
|------|---------|
| INNER JOIN | Matching rows only |
| LEFT JOIN | All rows from left table |
| RIGHT JOIN | All rows from right table |
| FULL JOIN | All rows from both tables |

### Example
```sql
SELECT e.name, d.department_name
FROM Employee e
INNER JOIN Department d
ON e.department_id = d.id;
```

---

# SQL: GROUP BY

### Explanation
Groups rows having the same values.

### Example
```sql
SELECT department, COUNT(*)
FROM Employee
GROUP BY department;
```

---

# SQL: HAVING

### Explanation
Filters grouped data after `GROUP BY`.

### Example
```sql
SELECT department, COUNT(*)
FROM Employee
GROUP BY department
HAVING COUNT(*) > 5;
```

---

# SQL: Window Functions

### Explanation
Perform calculations across rows without grouping them.

Common functions:
- ROW_NUMBER()
- RANK()
- DENSE_RANK()

### Example
```sql
SELECT name,
       salary,
       ROW_NUMBER() OVER(ORDER BY salary DESC)
FROM Employee;
```

---

# SQL: ROW_NUMBER()

### Explanation
Assigns a unique number to every row.

### Example
```sql
SELECT name,
ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
FROM Employee;
```

---

# SQL: RANK()

### Explanation
Assigns ranks with gaps when values are tied.

### Example
| Salary | Rank |
|--------|------|
| 100 | 1 |
| 100 | 1 |
| 90 | 3 |

```sql
SELECT salary,
RANK() OVER(ORDER BY salary DESC)
FROM Employee;
```

---

# SQL: DENSE_RANK()

### Explanation
Assigns ranks without gaps.

### Example
| Salary | Rank |
|--------|------|
| 100 | 1 |
| 100 | 1 |
| 90 | 2 |

```sql
SELECT salary,
DENSE_RANK() OVER(ORDER BY salary DESC)
FROM Employee;
```

---

# SQL: Indexes

### Explanation
Indexes improve query performance by speeding up data retrieval.

**Pros**
- Faster SELECT

**Cons**
- Slower INSERT/UPDATE/DELETE
- Extra storage

### Example
```sql
CREATE INDEX idx_name
ON Employee(name);
```

---

# SQL: Clustered Index

### Explanation
Stores table data physically in index order.

- Only **one** clustered index per table.

### Example
Primary Key is usually clustered.

---

# SQL: Composite Index

### Explanation
An index created on multiple columns.

### Example
```sql
CREATE INDEX idx_emp
ON Employee(department, salary);
```

---

# SQL: Transactions

### Explanation
A transaction is a group of SQL statements executed as one unit.

**ACID Properties**
- Atomicity
- Consistency
- Isolation
- Durability

### Example
```sql
BEGIN;

UPDATE Account
SET balance = balance - 100
WHERE id = 1;

UPDATE Account
SET balance = balance + 100
WHERE id = 2;

COMMIT;
```

---

# SQL: Isolation Levels

### Explanation
Isolation levels control how transactions interact.

| Level | Dirty Reads |
|--------|-------------|
| Read Uncommitted | Yes |
| Read Committed | No |
| Repeatable Read | No |
| Serializable | No (Highest Isolation) |

---

# SQL: Deadlocks

### Explanation
A deadlock occurs when two transactions wait for each other indefinitely.

### Example
- Transaction A locks Row 1, waits for Row 2.
- Transaction B locks Row 2, waits for Row 1.

**Solution**
- Access tables in the same order.
- Keep transactions short.

---

# SQL: Query Optimization

### Explanation
Improving SQL performance by reducing execution time.

### Best Practices
- Use indexes
- Avoid `SELECT *`
- Filter early with `WHERE`
- Use proper joins
- Optimize subqueries

### Example
```sql
SELECT id, name
FROM Employee
WHERE department = 'IT';
```

---

# SQL: Explain the Execution Plan

### Explanation
Execution Plan shows how the database executes a query.

It helps identify:
- Table scans
- Index usage
- Join methods
- Costly operations

### Example
```sql
EXPLAIN
SELECT *
FROM Employee
WHERE department = 'IT';
```

---

# Interview Tips

### ROW_NUMBER vs RANK vs DENSE_RANK

| Function | Duplicate Values | Gap in Ranking |
|----------|------------------|----------------|
| ROW_NUMBER() | No | No |
| RANK() | Yes | Yes |
| DENSE_RANK() | Yes | No |

### GROUP BY vs HAVING

- **WHERE** → Filters rows **before** grouping.
- **HAVING** → Filters groups **after** grouping.

### Clustered vs Composite Index

| Clustered Index | Composite Index |
|-----------------|-----------------|
| Physical data order | Multiple columns |
| One per table | Many allowed |

### Query Optimization

- Use indexes
- Avoid `SELECT *`
- Use `WHERE` clause
- Analyze execution plan
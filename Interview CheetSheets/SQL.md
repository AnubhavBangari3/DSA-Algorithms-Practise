# SQL Interview Questions

---

# 1. Explain Joins

## Answer

A **JOIN** is used to combine data from two or more tables based on a related column.

Suppose we have two tables:

### Employee

| id | name | dept_id |
|----|------|---------|
| 1 | Anubhav | 1 |
| 2 | Rahul | 2 |
| 3 | Aman | NULL |

### Department

| id | department |
|----|------------|
| 1 | IT |
| 2 | HR |
| 3 | Finance |

---

## Types of Joins

### 1. INNER JOIN

Returns only matching records from both tables.

```sql
SELECT e.name,
       d.department
FROM Employee e
INNER JOIN Department d
ON e.dept_id = d.id;
```

Output

| name | department |
|------|------------|
| Anubhav | IT |
| Rahul | HR |

---

### 2. LEFT JOIN

Returns all records from the left table and matching records from the right table.

```sql
SELECT e.name,
       d.department
FROM Employee e
LEFT JOIN Department d
ON e.dept_id = d.id;
```

Output

| name | department |
|------|------------|
| Anubhav | IT |
| Rahul | HR |
| Aman | NULL |

---

### 3. RIGHT JOIN

Returns all records from the right table and matching records from the left table.

```sql
SELECT e.name,
       d.department
FROM Employee e
RIGHT JOIN Department d
ON e.dept_id = d.id;
```

Output

| name | department |
|------|------------|
| Anubhav | IT |
| Rahul | HR |
| NULL | Finance |

---

### 4. FULL OUTER JOIN

Returns all records from both tables.

```sql
SELECT e.name,
       d.department
FROM Employee e
FULL OUTER JOIN Department d
ON e.dept_id = d.id;
```

Output

| name | department |
|------|------------|
| Anubhav | IT |
| Rahul | HR |
| Aman | NULL |
| NULL | Finance |

---

## Interview One-Liner

A JOIN combines data from multiple tables based on a common column.

---

# 2. Explain GROUP BY

## Answer

`GROUP BY` is used to group rows having the same values and usually works with aggregate functions.

### Employee

| name | department | salary |
|------|------------|--------|
| A | IT | 50000 |
| B | IT | 60000 |
| C | HR | 40000 |

### Example

```sql
SELECT department,
       COUNT(*) AS total_employees
FROM Employee
GROUP BY department;
```

Output

| department | total_employees |
|------------|-----------------|
| IT | 2 |
| HR | 1 |

---

Another Example

```sql
SELECT department,
       AVG(salary) AS average_salary
FROM Employee
GROUP BY department;
```

Output

| department | average_salary |
|------------|----------------|
| IT | 55000 |
| HR | 40000 |

---

## Interview One-Liner

`GROUP BY` groups rows having the same values and is commonly used with aggregate functions.

---

# 3. Explain Aggregate Functions

## Answer

Aggregate Functions perform calculations on multiple rows and return a single result.

### Common Aggregate Functions

| Function | Purpose |
|----------|----------|
| COUNT() | Counts rows |
| SUM() | Calculates total |
| AVG() | Calculates average |
| MAX() | Finds highest value |
| MIN() | Finds lowest value |

---

### COUNT

```sql
SELECT COUNT(*)
FROM Employee;
```

---

### SUM

```sql
SELECT SUM(salary)
FROM Employee;
```

---

### AVG

```sql
SELECT AVG(salary)
FROM Employee;
```

---

### MAX

```sql
SELECT MAX(salary)
FROM Employee;
```

---

### MIN

```sql
SELECT MIN(salary)
FROM Employee;
```

---

### GROUP BY with Aggregate

```sql
SELECT department,
       COUNT(*),
       AVG(salary)
FROM Employee
GROUP BY department;
```

---

## Interview One-Liner

Aggregate Functions calculate a single result from multiple rows, such as COUNT, SUM, AVG, MAX, and MIN.

---

# 4. Explain Indexes

## Answer

An **Index** is a database object that improves the speed of data retrieval.

Without an index, the database scans every row.

With an index, the database can quickly locate the required records.

Think of it like the index of a book.

Without an index:

```
Read every page.
```

With an index:

```
Go directly to the required page.
```

---

### Create Index

```sql
CREATE INDEX idx_employee_name
ON Employee(name);
```

---

### Drop Index

```sql
DROP INDEX idx_employee_name;
```

---

### Advantages

- Faster SELECT queries
- Faster WHERE filtering
- Faster JOIN operations
- Faster ORDER BY

---

### Disadvantages

- Uses extra storage
- INSERT, UPDATE and DELETE become slightly slower because the index must also be updated

---

## Interview One-Liner

An Index improves query performance by allowing the database to find rows quickly instead of scanning the entire table.

---

# 5. Explain Query Optimization

## Answer

Query Optimization means writing SQL queries that execute faster and use fewer database resources.

---

## 1. Use Indexes

❌ Bad

```sql
SELECT *
FROM Employee
WHERE name = 'Anubhav';
```

No index on `name`.

---

✅ Better

```sql
CREATE INDEX idx_name
ON Employee(name);
```

Now

```sql
SELECT *
FROM Employee
WHERE name='Anubhav';
```

becomes much faster.

---

## 2. Select Required Columns

❌ Bad

```sql
SELECT *
FROM Employee;
```

---

✅ Better

```sql
SELECT name,
       salary
FROM Employee;
```

Less data is transferred.

---

## 3. Use WHERE Clause

❌ Bad

```sql
SELECT *
FROM Employee;
```

---

✅ Better

```sql
SELECT *
FROM Employee
WHERE department='IT';
```

Retrieves only required rows.

---

## 4. Use LIMIT

```sql
SELECT *
FROM Employee
LIMIT 10;
```

Returns only the first 10 rows.

---

## 5. Avoid Unnecessary Subqueries

❌ Bad

```sql
SELECT *
FROM Employee
WHERE id IN (
    SELECT id
    FROM Employee
);
```

---

✅ Better

```sql
SELECT *
FROM Employee;
```

---

## 6. Use EXISTS Instead of IN (Large Data)

```sql
SELECT *
FROM Employee e
WHERE EXISTS (
    SELECT 1
    FROM Department d
    WHERE d.id = e.dept_id
);
```

---

## 7. Use Proper JOIN Instead of Nested Queries

```sql
SELECT e.name,
       d.department
FROM Employee e
JOIN Department d
ON e.dept_id = d.id;
```

---

## 8. Avoid Functions in WHERE Clause

❌ Bad

```sql
SELECT *
FROM Employee
WHERE YEAR(join_date)=2024;
```

---

✅ Better

```sql
SELECT *
FROM Employee
WHERE join_date >= '2024-01-01'
AND join_date < '2025-01-01';
```

This allows indexes to be used efficiently.

---

## Interview One-Liner

Query Optimization improves SQL performance by using indexes, selecting only required columns, filtering rows efficiently, avoiding unnecessary queries, and writing efficient JOINs.

---

# Interview Summary

| Topic | Interview Answer |
|--------|------------------|
| Joins | Combine data from multiple tables using a common column. |
| GROUP BY | Groups rows having the same values and is used with aggregate functions. |
| Aggregate Functions | Perform calculations on multiple rows like COUNT, SUM, AVG, MAX, and MIN. |
| Indexes | Improve query performance by reducing full table scans. |
| Query Optimization | Write efficient queries using indexes, WHERE clauses, proper JOINs, and selecting only required data. |
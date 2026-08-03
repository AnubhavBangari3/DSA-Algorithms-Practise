# SQL Hands-on Interview Questions

---

# 156. Find the Second Highest Salary

## SQL

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);
```

**Concept:** Use a subquery to find the highest salary, then find the maximum salary less than it.

---

# 157. Find Duplicate Records

## SQL

```sql
SELECT
    email,
    COUNT(*) AS duplicate_count
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

**Concept:** `GROUP BY` + `HAVING COUNT(*) > 1`.

---

# 158. Delete Duplicate Records

## SQL

```sql
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;
```

**Concept:** Self Join. Keep the smallest ID and delete the rest.

---

# 159. Find the Top 3 Salaries

## SQL (Using DENSE_RANK)

```sql
SELECT
    employee_id,
    salary
FROM (
    SELECT
        employee_id,
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) t
WHERE rnk <= 3;
```

**Concept:** Window Function (`DENSE_RANK`).

---

# 160. Running Total

## SQL

```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
    ) AS running_total
FROM Orders;
```

**Concept:** Window Function with cumulative `SUM()`.

---

# 161. Monthly Revenue

## SQL

```sql
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(amount) AS revenue
FROM Orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m');
```

**Concept:** `GROUP BY` month + `SUM()`.

---

# 162. Employee-Manager Query

## SQL

```sql
SELECT
    e.name AS Employee,
    m.name AS Manager
FROM Employee e
LEFT JOIN Employee m
ON e.managerId = m.id;
```

**Concept:** Self Join.

---

# 163. Customers With No Orders

## SQL

```sql
SELECT
    c.name
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
```

**Concept:** `LEFT JOIN` + `IS NULL`.

---

# 164. Second Highest Salary Using Subquery

## SQL

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);
```

**Concept:** Nested Subquery.

---

# 165. Optimize a Slow Query

## Common Optimizations

- Create indexes on frequently searched columns.
- Avoid `SELECT *`.
- Filter data early using `WHERE`.
- Replace correlated subqueries with `JOIN` when possible.
- Use `EXPLAIN` to analyze execution plans.
- Index columns used in `JOIN`, `WHERE`, `ORDER BY`, and `GROUP BY`.
- Retrieve only required columns.

Example:

```sql
-- Slow
SELECT *
FROM Orders
WHERE customer_id = 101;

-- Better (with index on customer_id)
CREATE INDEX idx_customer
ON Orders(customer_id);
```

---

# 166. Design Normalized Tables

## Example

### Customer

```text
customer_id (PK)
name
email
phone
```

### Product

```text
product_id (PK)
name
price
```

### Orders

```text
order_id (PK)
customer_id (FK)
order_date
```

### Order_Items

```text
order_id (FK)
product_id (FK)
quantity
price
```

## Why?

- Removes redundancy.
- Eliminates update anomalies.
- Maintains referential integrity.
- Easier to maintain and scale.

Typically follows **3NF (Third Normal Form)**.

---

# Interview Patterns Summary

| Question | Pattern |
|----------|---------|
| Second Highest Salary | MAX + Subquery |
| Duplicate Records | GROUP BY + HAVING |
| Delete Duplicates | Self Join |
| Top 3 Salaries | DENSE_RANK() |
| Running Total | SUM() OVER() |
| Monthly Revenue | DATE_FORMAT + GROUP BY |
| Employee-Manager | Self Join |
| Customers With No Orders | LEFT JOIN + IS NULL |
| Query Optimization | Indexing + EXPLAIN |
| Normalization | 1NF → 2NF → 3NF |
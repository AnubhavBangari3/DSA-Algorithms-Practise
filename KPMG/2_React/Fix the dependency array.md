# Fix the Dependency Array

## ❌ Incorrect

```jsx
useEffect(() => {
  fetchUser(userId);
}, []);
```

**Problem:** `userId` is used inside the effect but is missing from the dependency array.

---

## ✅ Correct

```jsx
useEffect(() => {
  fetchUser(userId);
}, [userId]);
```

Runs the effect whenever `userId` changes.

---

## ❌ Incorrect

```jsx
useEffect(() => {
  console.log(count);
}, [name]);
```

**Problem:** `count` is used but not included in the dependency array.

---

## ✅ Correct

```jsx
useEffect(() => {
  console.log(count);
}, [count]);
```

---

## Multiple Dependencies

```jsx
useEffect(() => {
  fetchData(userId, filter);
}, [userId, filter]);
```

---

## Interview Tip

Include **every state or prop used inside `useEffect`** in the dependency array unless you intentionally want different behavior.
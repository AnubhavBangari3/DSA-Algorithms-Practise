# Improve this `useEffect`

## ❌ Before

```jsx
useEffect(() => {
  fetchData();
});
```

**Problem:** Runs after **every render**, causing unnecessary API calls.

---

## ✅ After

```jsx
useEffect(() => {
  fetchData();
}, []);
```

Runs only once when the component mounts.

---

## If it depends on a value

```jsx
useEffect(() => {
  fetchUser(userId);
}, [userId]);
```

Runs only when `userId` changes.

---

## Cleanup Example

```jsx
useEffect(() => {
  const timer = setInterval(() => {
    console.log("Running...");
  }, 1000);

  return () => clearInterval(timer);
}, []);
```

Always clean up timers, subscriptions, and event listeners.

---

## Common Mistakes

❌ Missing dependency array

```jsx
useEffect(() => {
  fetchData();
});
```

❌ Incorrect dependency

```jsx
useEffect(() => {
  fetchUser(userId);
}, []);
```

Should be:

```jsx
useEffect(() => {
  fetchUser(userId);
}, [userId]);
```

---

## Interview Tip

- Use `[]` → Run once on mount.
- Use `[dependency]` → Run when dependency changes.
- Return a cleanup function for timers, subscriptions, or event listeners.
- Include all values used inside the effect in the dependency array unless there's a deliberate reason not to.
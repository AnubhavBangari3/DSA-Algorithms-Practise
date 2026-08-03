# Prevent Unnecessary Renders

## 1. Use `React.memo`

```jsx
const Child = React.memo(({ name }) => {
  console.log("Child Render");
  return <h2>{name}</h2>;
});
```

Prevents re-render if props haven't changed.

---

## 2. Use `useCallback`

```jsx
const handleClick = useCallback(() => {
  console.log("Clicked");
}, []);
```

Memoizes function references passed as props.

---

## 3. Use `useMemo`

```jsx
const total = useMemo(() => {
  return calculateTotal(items);
}, [items]);
```

Memoizes expensive computations.

---

## 4. Avoid Creating New Objects/Arrays

❌

```jsx
<Child style={{ color: "red" }} />
```

✅

```jsx
const style = { color: "red" };

<Child style={style} />
```

---

## 5. Split Large Components

Keep state close to where it's used so unrelated components don't re-render.

---

## Interview Tip

The most common optimization tools are:

- `React.memo()` → Prevent component re-renders.
- `useCallback()` → Prevent new function references.
- `useMemo()` → Prevent expensive recalculations.
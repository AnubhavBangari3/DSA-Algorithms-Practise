# React: Functional Components

### Explanation
Functional components are JavaScript functions that return JSX.

### Example
```jsx
function Welcome() {
  return <h1>Hello</h1>;
}
```

---

# React: State vs Props

| State | Props |
|-------|-------|
| Managed by component | Passed from parent |
| Mutable | Read-only |
| Can change | Cannot be modified by child |

### Example
```jsx
<User name="John" />   // Prop

const [count, setCount] = useState(0); // State
```

---

# React: useState

### Explanation
`useState` is used to store and update component state.

### Example
```jsx
const [count, setCount] = useState(0);

<button onClick={() => setCount(count + 1)}>
  {count}
</button>
```

---

# React: useEffect

### Explanation
Runs side effects like API calls, timers, or event listeners.

### Example
```jsx
useEffect(() => {
  fetchUsers();
}, []);
```

---

# React: useMemo

### Explanation
Caches expensive calculations to avoid recomputing on every render.

### Example
```jsx
const total = useMemo(() => {
  return items.reduce((a, b) => a + b, 0);
}, [items]);
```

---

# React: useCallback

### Explanation
Caches a function so it isn't recreated on every render.

### Example
```jsx
const handleClick = useCallback(() => {
  console.log("Clicked");
}, []);
```

---

# React: useRef

### Explanation
Stores a value without causing re-renders or accesses DOM elements.

### Example
```jsx
const inputRef = useRef();

<input ref={inputRef} />
```

---

# React: Context API

### Explanation
Shares data across components without prop drilling.

### Example
```jsx
const UserContext = createContext();
```

---

# React: Redux Basics

### Explanation
Redux is a global state management library.

**Flow**
```
Action
   ↓
Reducer
   ↓
Store
   ↓
Component
```

---

# React: Routing

### Explanation
React Router enables navigation between pages.

### Example
```jsx
<Route path="/home" element={<Home />} />
```

---

# React: Lazy Loading

### Explanation
Loads components only when needed, improving initial load time.

### Example
```jsx
const Home = React.lazy(() => import("./Home"));
```

---

# React: Code Splitting

### Explanation
Splits JavaScript bundles into smaller chunks for faster loading.

### Example
```jsx
const Dashboard = React.lazy(() => import("./Dashboard"));
```

---

# React: Virtual DOM

### Explanation
Virtual DOM is a lightweight copy of the real DOM.

React updates the Virtual DOM first, then updates only changed parts in the real DOM.

---

# React: Reconciliation

### Explanation
Reconciliation is React's process of comparing the old and new Virtual DOM to update only changed elements.

---

# React: Controlled Components

### Explanation
Form elements whose values are controlled by React state.

### Example
```jsx
const [name, setName] = useState("");

<input
  value={name}
  onChange={(e) => setName(e.target.value)}
/>
```

---

# React: Forms

### Explanation
Forms are handled using controlled components and state.

### Example
```jsx
const [email, setEmail] = useState("");
```

---

# React: API Integration

### Explanation
Use `fetch` or `axios` inside `useEffect` to call APIs.

### Example
```jsx
useEffect(() => {
  fetch("/api/users")
    .then(res => res.json())
    .then(setUsers);
}, []);
```

---

# React: Error Boundaries

### Explanation
Error Boundaries catch rendering errors and show a fallback UI.

> **Note:** They work only with **class components**.

### Example
```jsx
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

---

# React: React.memo

### Explanation
Prevents unnecessary re-rendering of a component if its props haven't changed.

### Example
```jsx
const User = React.memo(function User(props) {
  return <h1>{props.name}</h1>;
});
```

---

# React: Performance Optimization

### Common Techniques
- `React.memo()`
- `useMemo()`
- `useCallback()`
- Lazy Loading
- Code Splitting
- Pagination
- Debouncing
- Virtualization for large lists

---

# Interview Tips

### useMemo vs useCallback

| useMemo | useCallback |
|----------|-------------|
| Caches a value | Caches a function |

### State vs Props

- **State:** Managed inside component
- **Props:** Passed from parent

### Virtual DOM

- Faster than updating the real DOM directly.
- React updates only changed elements.

### Performance

- `React.memo()` → Prevent re-renders
- `useMemo()` → Cache calculations
- `useCallback()` → Cache functions
- Lazy Loading → Faster initial load
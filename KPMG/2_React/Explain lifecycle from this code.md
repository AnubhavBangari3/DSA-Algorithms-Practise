# Explain React Lifecycle from this Code

## Example

```jsx
import React, { useEffect, useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  // Mount
  useEffect(() => {
    console.log("Component Mounted");
  }, []);

  // Update
  useEffect(() => {
    console.log("Count Updated:", count);
  }, [count]);

  // Unmount
  useEffect(() => {
    return () => {
      console.log("Component Unmounted");
    };
  }, []);

  return (
    <div>
      <h2>{count}</h2>

      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}

export default App;
```

---

## Lifecycle Phases

### 1. Mount

```jsx
useEffect(() => {
  console.log("Component Mounted");
}, []);
```

Runs **once** when the component is first rendered.

---

### 2. Update

```jsx
useEffect(() => {
  console.log("Count Updated:", count);
}, [count]);
```

Runs whenever `count` changes.

---

### 3. Unmount

```jsx
useEffect(() => {
  return () => {
    console.log("Component Unmounted");
  };
}, []);
```

Runs when the component is removed from the DOM.

---

## Interview Explanation

- **Mount:** Component is created and rendered for the first time.
- **Update:** Component re-renders when state or props change.
- **Unmount:** Cleanup function runs before the component is removed.
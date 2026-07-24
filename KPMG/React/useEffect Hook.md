# Question 9: useEffect Hook

## Difference Between `useEffect(fn)`, `useEffect(fn, [])`, and `useEffect(fn, [id])`

| Feature | `useEffect(fn)` | `useEffect(fn, [])` | `useEffect(fn, [id])` |
|---------|-----------------|---------------------|-----------------------|
| **When does it execute?** | After every render (initial + every re-render) | Only once after the initial render | After the initial render and whenever `id` changes |
| **Runs on first render?** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Runs when state changes?** | ✅ Yes (every state change) | ❌ No | ✅ Only if `id` changes |
| **Runs when props change?** | ✅ Yes | ❌ No | ✅ Only if `id` changes |
| **Dependency Array** | No dependency array | Empty dependency array (`[]`) | Dependency array containing `id` |
| **Common Use Cases** | Logging, debugging, updating DOM after every render | API call on page load, authentication check, event listeners | Fetch data based on ID, update UI when a value changes |
| **Performance** | Poor if expensive logic runs every render | Best for one-time operations | Efficient because it runs only when dependencies change |

---

# 1. `useEffect(fn)`

## Syntax

```javascript
useEffect(() => {
    console.log("Component Rendered");
});
```

## When does it execute?

- After the first render.
- After every re-render.
- Runs whenever state or props change.

## Example

```javascript
import { useState, useEffect } from "react";

function App() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log("Runs after every render");
    });

    return (
        <>
            <h1>{count}</h1>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
        </>
    );
}
```

## Output

```text
Page Load
Runs after every render

Click Button
Runs after every render

Click Again
Runs after every render
```

## Common Use Cases

- Debugging
- Logging
- Updating document title
- Tracking every render

---

# 2. `useEffect(fn, [])`

## Syntax

```javascript
useEffect(() => {
    console.log("Runs only once");
}, []);
```

## When does it execute?

- Only once after the component mounts.
- Never runs again.

## Example

```javascript
import { useEffect } from "react";

function App() {

    useEffect(() => {
        console.log("API Called");
    }, []);

    return <h1>Hello</h1>;
}
```

## Output

```text
API Called
```

Only once.

## Common Use Cases

- API Call
- Authentication Check
- Load Initial Data
- Add Event Listener
- Initialize Library

---

# 3. `useEffect(fn, [id])`

## Syntax

```javascript
useEffect(() => {
    console.log("User Changed");
}, [id]);
```

## When does it execute?

- After the first render.
- Whenever `id` changes.
- Does **NOT** run if other state variables change.

## Example

```javascript
import { useState, useEffect } from "react";

function App() {

    const [id, setId] = useState(1);

    useEffect(() => {
        console.log("Fetching User:", id);
    }, [id]);

    return (
        <button onClick={() => setId(id + 1)}>
            Next User
        </button>
    );
}
```

## Output

```text
Fetching User : 1

Click Button

Fetching User : 2

Click Again

Fetching User : 3
```

## Common Use Cases

- Fetch User by ID
- Fetch Product Details
- Search Results
- Filter Changes
- Pagination

---

# Cleanup Function

A cleanup function runs before the component unmounts or before the effect runs again.

## Syntax

```javascript
useEffect(() => {

    console.log("Effect Started");

    return () => {
        console.log("Cleanup");
    };

}, []);
```

## Example

```javascript
useEffect(() => {

    window.addEventListener("resize", handleResize);

    return () => {
        window.removeEventListener("resize", handleResize);
    };

}, []);
```

## Why use Cleanup?

- Prevent Memory Leaks
- Remove Event Listeners
- Clear Timers
- Cancel API Requests
- Close WebSocket Connections

---

# Cleanup Execution

## `useEffect(fn)`

```javascript
useEffect(() => {

    console.log("Effect");

    return () => {
        console.log("Cleanup");
    };

});
```

Runs like this:

```text
Effect

State Changes

Cleanup
Effect

State Changes

Cleanup
Effect
```

---

## `useEffect(fn, [])`

```javascript
useEffect(() => {

    console.log("Effect");

    return () => {
        console.log("Cleanup");
    };

}, []);
```

Runs like this:

```text
Component Mounted

Effect

Component Unmounted

Cleanup
```

---

## `useEffect(fn, [id])`

```javascript
useEffect(() => {

    console.log(id);

    return () => {
        console.log("Cleanup");
    };

}, [id]);
```

Runs like this:

```text
id = 1

Effect

id changes to 2

Cleanup
Effect

id changes to 3

Cleanup
Effect
```

---

# Interview Summary

| Hook | Executes | Typical Use |
|------|----------|-------------|
| `useEffect(fn)` | Every render | Logging, debugging, DOM updates |
| `useEffect(fn, [])` | Only once after mount | API calls, authentication, initialization |
| `useEffect(fn, [id])` | After mount and whenever `id` changes | Fetch data by ID, filters, search, pagination |

---

# Interview One-Liner

- **`useEffect(fn)`** → Runs after **every render**.
- **`useEffect(fn, [])`** → Runs **only once** after the component mounts.
- **`useEffect(fn, [id])`** → Runs after the initial render and **whenever `id` changes**.
- **Cleanup Function** → Executes before the component unmounts or before the effect runs again, helping prevent memory leaks and cleaning up resources like event listeners, timers, API requests, and WebSocket connections.
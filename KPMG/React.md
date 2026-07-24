# React Interview Questions

---

# 1. Explain Functional Components

## Answer

A Functional Component is a JavaScript function that returns JSX to render UI.

Earlier, Class Components were used, but nowadays Functional Components are preferred because they are simpler and support Hooks.

### Example

```jsx
function Welcome() {
    return <h1>Hello React</h1>;
}

export default Welcome;
```

### Using Props

```jsx
function Welcome(props) {
    return <h1>Hello {props.name}</h1>;
}

<Welcome name="Anubhav" />
```

Output

```
Hello Anubhav
```

### Advantages

- Less code
- Easy to understand
- Better readability
- Supports Hooks
- Better performance than class components in most cases

---

# 2. Explain React Hooks

## Answer

Hooks are built-in React functions that allow Functional Components to use state and lifecycle features.

Hooks always start with **use**.

### Common Hooks

| Hook | Purpose |
|------|----------|
| useState | Manage component state |
| useEffect | Side effects (API calls, timers, event listeners) |
| useContext | Share data without prop drilling |
| useRef | Access DOM elements or store mutable values |
| useMemo | Optimize expensive calculations |
| useCallback | Prevent unnecessary function recreation |
| useReducer | Complex state management |

### Example

```jsx
import { useState } from "react";

function Counter() {

    const [count, setCount] = useState(0);

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

### Advantages

- Reuse logic
- Simpler code
- No class components required
- Better readability

---

# 3. Explain State vs Props

## Answer

| State | Props |
|--------|-------|
| Managed inside the component | Passed from parent component |
| Mutable (can change) | Immutable (Read-only) |
| Updated using `setState()` or `useState()` | Cannot be modified by child |
| Used for dynamic data | Used for passing data |

### State Example

```jsx
function Counter() {

    const [count, setCount] = useState(0);

    return (
        <button onClick={() => setCount(count + 1)}>
            {count}
        </button>
    );
}
```

### Props Example

```jsx
function Welcome({ name }) {
    return <h1>Hello {name}</h1>;
}

<Welcome name="Anubhav" />
```

### Interview One-Liner

- **State** belongs to the component and can change.
- **Props** are passed from the parent and are read-only.

---

# 4. Explain Component Lifecycle

## Answer

The Component Lifecycle describes the different stages of a component from creation to removal.

### Three Phases

### 1. Mounting

Component is created and added to the DOM.

Common Tasks

- API Calls
- Authentication
- Initial Data Loading

Example

```jsx
useEffect(() => {
    console.log("Mounted");
}, []);
```

---

### 2. Updating

Occurs whenever State or Props change.

Example

```jsx
useEffect(() => {
    console.log("ID Changed");
}, [id]);
```

---

### 3. Unmounting

Component is removed from the DOM.

Used for cleanup.

Example

```jsx
useEffect(() => {

    return () => {
        console.log("Component Removed");
    };

}, []);
```

### Lifecycle Diagram

```
Mount
   ↓
Render
   ↓
Update (State/Props Change)
   ↓
Render Again
   ↓
Unmount
```

---

# 5. Explain API Integration

## Answer

API Integration means communicating with the backend server to fetch or send data.

React commonly uses:

- fetch()
- Axios

### Using Fetch

```jsx
import { useEffect, useState } from "react";

function Users() {

    const [users, setUsers] = useState([]);

    useEffect(() => {

        fetch("https://jsonplaceholder.typicode.com/users")
            .then(response => response.json())
            .then(data => setUsers(data));

    }, []);

    return (
        <>
            {users.map(user => (
                <p key={user.id}>{user.name}</p>
            ))}
        </>
    );
}
```

---

### Using Axios

```jsx
import axios from "axios";

useEffect(() => {

    axios.get("/api/users")
        .then(response => {
            console.log(response.data);
        });

}, []);
```

### Common HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve Data |
| POST | Create Data |
| PUT | Update Entire Record |
| PATCH | Partial Update |
| DELETE | Delete Record |

---

# 6. Explain Routing

## Answer

Routing allows users to navigate between different pages without refreshing the browser.

React commonly uses **React Router DOM**.

### Install

```bash
npm install react-router-dom
```

### Example

```jsx
import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

function Home() {
    return <h1>Home</h1>;
}

function About() {
    return <h1>About</h1>;
}

function App() {

    return (
        <BrowserRouter>

            <Routes>

                <Route path="/" element={<Home />} />

                <Route path="/about" element={<About />} />

            </Routes>

        </BrowserRouter>
    );
}
```

---

### Navigation

```jsx
import { Link } from "react-router-dom";

<Link to="/">Home</Link>

<Link to="/about">About</Link>
```

---

### Dynamic Route

```jsx
<Route path="/user/:id" element={<User />} />
```

Access Parameter

```jsx
import { useParams } from "react-router-dom";

const { id } = useParams();
```

---

### Programmatic Navigation

```jsx
import { useNavigate } from "react-router-dom";

const navigate = useNavigate();

navigate("/dashboard");
```

---

# Interview One-Liners

### Functional Components

A Functional Component is a JavaScript function that returns JSX and supports Hooks.

### React Hooks

Hooks allow Functional Components to use state, lifecycle methods, and other React features without using class components.

### State vs Props

State is managed inside the component and can change, whereas Props are passed from the parent component and are read-only.

### Component Lifecycle

A React component goes through three phases: Mounting, Updating, and Unmounting.

### API Integration

API Integration is the process of fetching or sending data between the React application and the backend using `fetch()` or Axios.

### Routing

Routing allows navigation between different pages in a Single Page Application (SPA) using **React Router DOM** without reloading the page.
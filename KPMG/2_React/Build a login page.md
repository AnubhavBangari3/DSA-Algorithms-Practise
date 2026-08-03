# Build a Login Page

## Example

```jsx
import React, { useState } from "react";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log({
      email,
      password,
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <br /><br />

      <button type="submit">
        Login
      </button>
    </form>
  );
}

export default App;
```

---

## Interview Explanation

- Use `useState` to store the email and password.
- Use controlled inputs with `value` and `onChange`.
- Prevent the default form submission using `e.preventDefault()`.
- Handle login logic inside `handleSubmit()` (e.g., API call).
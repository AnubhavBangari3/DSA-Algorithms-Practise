# Implement Debounce Search

## Example

```jsx
import React, { useState, useEffect } from "react";

function App() {
  const [search, setSearch] = useState("");

  useEffect(() => {
    const timer = setTimeout(() => {
      console.log("Searching:", search);
      // API Call
    }, 500);

    return () => clearTimeout(timer);
  }, [search]);

  return (
    <div>
      <input
        type="text"
        placeholder="Search..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </div>
  );
}

export default App;
```

---

## Interview Explanation

- Store the search text in state.
- Use `setTimeout()` to delay the API call.
- Clear the previous timeout using `clearTimeout()` so only the latest input triggers the search.
- This reduces unnecessary API requests while the user is typing.

---

## Interview Tip

**Debounce** delays execution until the user stops typing for a specified time (e.g., 500 ms), making search inputs more efficient.
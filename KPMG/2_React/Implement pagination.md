# Implement Pagination (Simple Version)

```jsx
import React, { useState } from "react";

function App() {
  const items = [1,2,3,4,5,6,7,8,9,10];

  const [page, setPage] = useState(1);
  const perPage = 3;

  const start = (page - 1) * perPage;
  const currentItems = items.slice(start, start + perPage);

  return (
    <div>
      {currentItems.map((item) => (
        <p key={item}>{item}</p>
      ))}

      <button
        onClick={() => setPage(page - 1)}
        disabled={page === 1}
      >
        Previous
      </button>

      <button
        onClick={() => setPage(page + 1)}
        disabled={start + perPage >= items.length}
      >
        Next
      </button>
    </div>
  );
}

export default App;
```

---

## Interview Explanation

- Store the current page in state.
- Calculate the starting index using:
  ```js
  (page - 1) * perPage
  ```
- Display items using `slice()`.
- Disable **Previous** on the first page.
- Disable **Next** when there are no more items.
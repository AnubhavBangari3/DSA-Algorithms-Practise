# Implement Pagination

## Example

```jsx
import React, { useState } from "react";

function App() {
  const items = Array.from({ length: 50 }, (_, i) => `Item ${i + 1}`);

  const itemsPerPage = 5;
  const [currentPage, setCurrentPage] = useState(1);

  const lastIndex = currentPage * itemsPerPage;
  const firstIndex = lastIndex - itemsPerPage;

  const currentItems = items.slice(firstIndex, lastIndex);
  const totalPages = Math.ceil(items.length / itemsPerPage);

  return (
    <div>
      <ul>
        {currentItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>

      <button
        onClick={() => setCurrentPage((prev) => prev - 1)}
        disabled={currentPage === 1}
      >
        Previous
      </button>

      <span> Page {currentPage} of {totalPages} </span>

      <button
        onClick={() => setCurrentPage((prev) => prev + 1)}
        disabled={currentPage === totalPages}
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

- Store the current page using `useState`.
- Calculate the start and end indexes.
- Use `slice()` to get items for the current page.
- Disable **Previous** on the first page and **Next** on the last page.
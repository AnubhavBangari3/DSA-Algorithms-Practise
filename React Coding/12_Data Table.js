/**
12. Data Table

Build a users data table with pagination features.
 */

import React, { useState } from "react";

function App() {
  // Sample users data
  const users = [
    { id: 1, name: "Anubhav", email: "anubhav@email.com", role: "Developer" },
    { id: 2, name: "Rahul", email: "rahul@email.com", role: "Tester" },
    { id: 3, name: "Priya", email: "priya@email.com", role: "Manager" },
    { id: 4, name: "Aman", email: "aman@email.com", role: "Developer" },
    { id: 5, name: "Sneha", email: "sneha@email.com", role: "Designer" },
    { id: 6, name: "Rohit", email: "rohit@email.com", role: "Developer" },
    { id: 7, name: "Neha", email: "neha@email.com", role: "HR" },
    { id: 8, name: "Vikas", email: "vikas@email.com", role: "Tester" },
  ];

  // Current page number
  const [currentPage, setCurrentPage] = useState(1);

  // Number of users shown per page
  const usersPerPage = 3;

  // Total number of pages
  const totalPages = Math.ceil(users.length / usersPerPage);

  // Starting index for current page
  const startIndex = (currentPage - 1) * usersPerPage;

  // Ending index for current page
  const endIndex = startIndex + usersPerPage;

  // Users visible on current page
  const currentUsers = users.slice(startIndex, endIndex);

  const styles = {
    main: {
      width: "700px",
      margin: "40px auto",
      fontFamily: "Arial",
    },
    table: {
      width: "100%",
      borderCollapse: "collapse",
      marginTop: "20px",
    },
    th: {
      border: "1px solid #ddd",
      padding: "12px",
      backgroundColor: "#5C6AC4",
      color: "white",
    },
    td: {
      border: "1px solid #ddd",
      padding: "12px",
      textAlign: "center",
    },
    pagination: {
      marginTop: "20px",
      display: "flex",
      justifyContent: "center",
      gap: "10px",
    },
    button: {
      padding: "8px 12px",
      cursor: "pointer",
    },
    activeButton: {
      padding: "8px 12px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Users Data Table</h1>

      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>ID</th>
            <th style={styles.th}>Name</th>
            <th style={styles.th}>Email</th>
            <th style={styles.th}>Role</th>
          </tr>
        </thead>

        <tbody>
          {/* Render users of current page only */}
          {currentUsers.map((user) => (
            <tr key={user.id}>
              <td style={styles.td}>{user.id}</td>
              <td style={styles.td}>{user.name}</td>
              <td style={styles.td}>{user.email}</td>
              <td style={styles.td}>{user.role}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pagination controls */}
      <div style={styles.pagination}>
        <button
          style={styles.button}
          disabled={currentPage === 1}
          onClick={() => setCurrentPage(currentPage - 1)}
        >
          Prev
        </button>

        {/* Page number buttons */}
        {Array.from({ length: totalPages }).map((_, index) => (
          <button
            key={index}
            style={
              currentPage === index + 1
                ? styles.activeButton
                : styles.button
            }
            onClick={() => setCurrentPage(index + 1)}
          >
            {index + 1}
          </button>
        ))}

        <button
          style={styles.button}
          disabled={currentPage === totalPages}
          onClick={() => setCurrentPage(currentPage + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default App;
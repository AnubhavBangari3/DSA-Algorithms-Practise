/**
7. Generate Table

Generate a table of numbers given the rows and columns.
 */

import React, { useState } from "react";

function App() {
  // Stores number of rows entered by the user
  const [rows, setRows] = useState("");

  // Stores number of columns entered by the user
  const [cols, setCols] = useState("");

  const styles = {
    main: {
      padding: "20px",
      fontFamily: "Arial",
      textAlign: "center",
    },

    input: {
      margin: "10px",
      padding: "10px",
      width: "120px",
      fontSize: "16px",
    },

    table: {
      margin: "20px auto",
      borderCollapse: "collapse",
    },

    cell: {
      border: "1px solid black",
      padding: "12px",
      width: "50px",
      textAlign: "center",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Generate Table</h1>

      {/* Input for number of rows */}
      <input
        style={styles.input}
        type="number"
        placeholder="Rows"
        value={rows}
        onChange={(e) => setRows(Number(e.target.value))}
      />

      {/* Input for number of columns */}
      <input
        style={styles.input}
        type="number"
        placeholder="Columns"
        value={cols}
        onChange={(e) => setCols(Number(e.target.value))}
      />

      {/* Table starts here */}
      <table style={styles.table}>
        <tbody>

          {/* Create rows */}
          {Array.from({ length: rows }).map((_, rowIndex) => (

            <tr key={rowIndex}>

              {/* Create columns for each row */}
              {Array.from({ length: cols }).map((_, colIndex) => (

                <td key={colIndex} style={styles.cell}>
                  {/* Display sequential numbers */}
                  {rowIndex * cols + colIndex + 1}
                </td>

              ))}

            </tr>

          ))}

        </tbody>
      </table>

    </div>
  );
}

export default App;
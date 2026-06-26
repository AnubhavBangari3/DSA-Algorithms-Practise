/**
 1. Accordion

Build an accordion component that a displays a list of vertically stacked sections with each containing a title and content snippet. 
* */
import React, { useState } from "react";

function App() {

  // Array containing accordion sections
  const data = [
    {
      title: "What is React?",
      content: "React is a JavaScript library for building user interfaces.",
    },
    {
      title: "What is useState?",
      content:
        "useState is a Hook that lets you add state to functional components.",
    },
    {
      title: "What is JSX?",
      content:
        "JSX is a syntax extension that lets us write HTML-like code inside JavaScript.",
    },
  ];

  // Stores the index of the currently opened accordion.
  // null means no accordion is open.
  const [openIndex, setOpenIndex] = useState(null);

  // Handles opening and closing accordion items
  const handleToggle = (index) => {

    // If the clicked accordion is already open,
    // close it by setting state to null.
    // Otherwise, open the clicked accordion.
    setOpenIndex(openIndex === index ? null : index);
  };

  // Inline CSS styles
  const styles = {
    main: {
      padding: "20px",
      width: "500px",
      margin: "40px auto",
      fontFamily: "Arial",
    },
    title: {
      color: "#5C6AC4",
      marginBottom: "20px",
    },
    item: {
      border: "1px solid #ccc",
      borderRadius: "5px",
      marginBottom: "10px",
    },
    button: {
      width: "100%",
      padding: "12px",
      background: "#f4f4f4",
      border: "none",
      cursor: "pointer",
      textAlign: "left",
      fontWeight: "bold",
      fontSize: "16px",
    },
    content: {
      padding: "12px",
      background: "#fff",
    },
  };

  return (
    <div style={styles.main}>
      <h1 style={styles.title}>Accordion Example</h1>

      {/* Loop through all accordion items */}
      {data.map((item, index) => (
        <div key={index} style={styles.item}>

          {/* Accordion Header */}
          <button
            style={styles.button}
            onClick={() => handleToggle(index)}
          >
            {item.title}

            {/* Show + when closed and - when opened */}
            <span style={{ float: "right" }}>
              {openIndex === index ? "-" : "+"}
            </span>
          </button>

          {/* Render content only if this accordion is open */}
          {openIndex === index && (
            <div style={styles.content}>
              {item.content}
            </div>
          )}

        </div>
      ))}
    </div>
  );
}

export default App;
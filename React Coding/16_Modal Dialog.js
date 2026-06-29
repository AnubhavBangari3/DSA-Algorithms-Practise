/**
16. Modal Dialog

Build a reusable modal dialog component that can be opened and closed.
 */

import React, { useState } from "react";

function App() {
  // Controls whether modal is visible or hidden
  const [isModalOpen, setIsModalOpen] = useState(false);

  const styles = {
    main: {
      textAlign: "center",
      marginTop: "80px",
      fontFamily: "Arial",
    },

    openButton: {
      padding: "12px 20px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      borderRadius: "6px",
      cursor: "pointer",
      fontSize: "16px",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Modal Dialog</h1>

      {/* Button to open modal */}
      <button
        style={styles.openButton}
        onClick={() => setIsModalOpen(true)}
      >
        Open Modal
      </button>

      {/* Render modal only when isModalOpen is true */}
      {isModalOpen && (
        <Modal
          title="Confirm Action"
          onClose={() => setIsModalOpen(false)}
        >
          <p>This is a reusable modal dialog component.</p>
          <p>You can pass any content inside it using children.</p>
        </Modal>
      )}
    </div>
  );
}

// Reusable Modal Component
function Modal({ title, children, onClose }) {
  const styles = {
    overlay: {
      position: "fixed",
      top: 0,
      left: 0,
      width: "100%",
      height: "100%",
      backgroundColor: "rgba(0, 0, 0, 0.5)", // dark background
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
    },

    modal: {
      width: "400px",
      backgroundColor: "white",
      borderRadius: "8px",
      padding: "20px",
      boxShadow: "0 4px 10px rgba(0,0,0,0.3)",
      textAlign: "left",
    },

    header: {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      marginBottom: "15px",
    },

    closeButton: {
      border: "none",
      background: "transparent",
      fontSize: "22px",
      cursor: "pointer",
    },

    footer: {
      marginTop: "20px",
      textAlign: "right",
    },

    button: {
      padding: "8px 14px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      borderRadius: "5px",
      cursor: "pointer",
    },
  };

  return (
    <div style={styles.overlay}>
      <div style={styles.modal}>
        {/* Modal Header */}
        <div style={styles.header}>
          <h2>{title}</h2>

          {/* Close icon */}
          <button style={styles.closeButton} onClick={onClose}>
            ×
          </button>
        </div>

        {/* Modal Body */}
        <div>{children}</div>

        {/* Modal Footer */}
        <div style={styles.footer}>
          <button style={styles.button} onClick={onClose}>
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
/**
 2. Contact Form

Build a contact form which submits user feedback and contact details to a back end API.
 */

import React, { useState } from "react";

function App() {
  // Form state to store user input values
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  // State to show success/error/loading messages
  const [status, setStatus] = useState("");

  // Handles input change for all fields
  const handleChange = (e) => {
    const { name, value } = e.target;

    // Update only the changed field
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Handles form submit
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent page refresh

    setStatus("Submitting...");

    try {
      // API call to backend
      const response = await fetch("https://example.com/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },

        // Convert JS object into JSON string
        body: JSON.stringify(formData),
      });

      // If API fails, throw error
      if (!response.ok) {
        throw new Error("Failed to submit form");
      }

      setStatus("Feedback submitted successfully!");

      // Clear form after successful submission
      setFormData({
        name: "",
        email: "",
        message: "",
      });
    } catch (error) {
      setStatus("Something went wrong. Please try again.");
    }
  };

  const styles = {
    main: {
      padding: "20px",
      width: "450px",
      margin: "40px auto",
      fontFamily: "Arial",
    },
    title: {
      color: "#5C6AC4",
    },
    form: {
      display: "flex",
      flexDirection: "column",
      gap: "12px",
    },
    input: {
      padding: "10px",
      fontSize: "16px",
      border: "1px solid #ccc",
      borderRadius: "5px",
    },
    textarea: {
      padding: "10px",
      fontSize: "16px",
      border: "1px solid #ccc",
      borderRadius: "5px",
      minHeight: "100px",
    },
    button: {
      padding: "10px",
      background: "#5C6AC4",
      color: "white",
      border: "none",
      borderRadius: "5px",
      cursor: "pointer",
      fontSize: "16px",
    },
    status: {
      marginTop: "12px",
      fontWeight: "bold",
    },
  };

  return (
    <div style={styles.main}>
      <h1 style={styles.title}>Contact Form</h1>

      <form style={styles.form} onSubmit={handleSubmit}>
        {/* Name input */}
        <input
          style={styles.input}
          type="text"
          name="name"
          placeholder="Enter your name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        {/* Email input */}
        <input
          style={styles.input}
          type="email"
          name="email"
          placeholder="Enter your email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        {/* Feedback message */}
        <textarea
          style={styles.textarea}
          name="message"
          placeholder="Enter your feedback"
          value={formData.message}
          onChange={handleChange}
          required
        />

        <button style={styles.button} type="submit">
          Submit
        </button>
      </form>

      {/* Show loading/success/error message */}
      {status && <p style={styles.status}>{status}</p>}
    </div>
  );
}

export default App;
/**
 6. Flight Booker

Build a component that books a flight for specified dates.
 */
import React, { useState } from "react";

function App() {
  // Stores selected flight type
  // "one-way" means only departure date is required
  // "return" means both departure and return dates are required
  const [flightType, setFlightType] = useState("one-way");

  // Stores departure date
  const [departureDate, setDepartureDate] = useState("");

  // Stores return date
  const [returnDate, setReturnDate] = useState("");

  // Stores final booking message
  const [message, setMessage] = useState("");

  // Validate dates and book flight
  const handleSubmit = (e) => {
    e.preventDefault();

    // For return flight, return date should not be before departure date
    if (flightType === "return" && returnDate < departureDate) {
      setMessage("Return date cannot be before departure date.");
      return;
    }

    // Success message for one-way trip
    if (flightType === "one-way") {
      setMessage(`You booked a one-way flight on ${departureDate}.`);
      return;
    }

    // Success message for return trip
    setMessage(
      `You booked a return flight from ${departureDate} to ${returnDate}.`
    );
  };

  const styles = {
    main: {
      width: "400px",
      margin: "40px auto",
      padding: "20px",
      fontFamily: "Arial",
      border: "1px solid #ddd",
      borderRadius: "8px",
    },
    title: {
      color: "#5C6AC4",
      textAlign: "center",
    },
    form: {
      display: "flex",
      flexDirection: "column",
      gap: "12px",
    },
    input: {
      padding: "10px",
      fontSize: "16px",
    },
    button: {
      padding: "10px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      cursor: "pointer",
      fontSize: "16px",
    },
    message: {
      marginTop: "20px",
      fontWeight: "bold",
      textAlign: "center",
    },
  };

  return (
    <div style={styles.main}>
      <h1 style={styles.title}>Flight Booker</h1>

      <form style={styles.form} onSubmit={handleSubmit}>
        {/* Select flight type */}
        <select
          style={styles.input}
          value={flightType}
          onChange={(e) => setFlightType(e.target.value)}
        >
          <option value="one-way">One-way Flight</option>
          <option value="return">Return Flight</option>
        </select>

        {/* Departure date is always required */}
        <input
          style={styles.input}
          type="date"
          value={departureDate}
          onChange={(e) => setDepartureDate(e.target.value)}
          required
        />

        {/* Return date is required only for return flight */}
        <input
          style={styles.input}
          type="date"
          value={returnDate}
          onChange={(e) => setReturnDate(e.target.value)}
          disabled={flightType === "one-way"}
          required={flightType === "return"}
        />

        <button style={styles.button} type="submit">
          Book Flight
        </button>
      </form>

      {/* Show booking or validation message */}
      {message && <p style={styles.message}>{message}</p>}
    </div>
  );
}

export default App;
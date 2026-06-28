/**
9. Temperature Converter

Build a temperature converter widget that converts temperature values between Celsius and Fahrenheit.
 */

import React, { useState } from "react";

function App() {
  // Stores temperature entered by the user
  const [temperature, setTemperature] = useState("");

  // Stores the conversion type
  // "CtoF" => Celsius to Fahrenheit
  // "FtoC" => Fahrenheit to Celsius
  const [conversionType, setConversionType] = useState("CtoF");

  // Stores converted temperature
  const [result, setResult] = useState("");

  // Perform temperature conversion
  const convertTemperature = () => {
    // Convert input string into number
    const temp = Number(temperature);

    // Check if input is valid
    if (isNaN(temp)) {
      setResult("Please enter a valid temperature.");
      return;
    }

    let convertedTemp;

    // Celsius → Fahrenheit
    if (conversionType === "CtoF") {
      convertedTemp = (temp * 9) / 5 + 32;
      setResult(`${convertedTemp.toFixed(2)} °F`);
    }
    // Fahrenheit → Celsius
    else {
      convertedTemp = ((temp - 32) * 5) / 9;
      setResult(`${convertedTemp.toFixed(2)} °C`);
    }
  };

  const styles = {
    main: {
      width: "400px",
      margin: "40px auto",
      padding: "20px",
      fontFamily: "Arial",
      border: "1px solid #ddd",
      borderRadius: "8px",
      textAlign: "center",
    },

    title: {
      color: "#5C6AC4",
    },

    input: {
      width: "100%",
      padding: "10px",
      marginBottom: "15px",
      fontSize: "16px",
    },

    select: {
      width: "100%",
      padding: "10px",
      marginBottom: "15px",
      fontSize: "16px",
    },

    button: {
      width: "100%",
      padding: "10px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      cursor: "pointer",
      fontSize: "16px",
    },

    result: {
      marginTop: "20px",
      fontSize: "20px",
      fontWeight: "bold",
    },
  };

  return (
    <div style={styles.main}>
      <h1 style={styles.title}>Temperature Converter</h1>

      {/* Temperature Input */}
      <input
        style={styles.input}
        type="number"
        placeholder="Enter Temperature"
        value={temperature}
        onChange={(e) => setTemperature(e.target.value)}
      />

      {/* Select Conversion Type */}
      <select
        style={styles.select}
        value={conversionType}
        onChange={(e) => setConversionType(e.target.value)}
      >
        <option value="CtoF">Celsius → Fahrenheit</option>
        <option value="FtoC">Fahrenheit → Celsius</option>
      </select>

      {/* Convert Button */}
      <button style={styles.button} onClick={convertTemperature}>
        Convert
      </button>

      {/* Display Converted Temperature */}
      {result && <div style={styles.result}>{result}</div>}
    </div>
  );
}

export default App;
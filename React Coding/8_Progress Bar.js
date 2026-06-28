/**
 8. Progress Bar

Build a progress bar component that shows the percentage completion of an operation.
 */

import React, { useState } from "react";

function App() {
  // Stores current progress percentage
  const [progress, setProgress] = useState(30);

  const styles = {
    main: {
      width: "500px",
      margin: "40px auto",
      fontFamily: "Arial",
      textAlign: "center",
    },

    progressContainer: {
      width: "100%",
      height: "30px",
      backgroundColor: "#e0e0e0",
      borderRadius: "20px",
      overflow: "hidden",
      marginTop: "20px",
    },

    progressFill: {
      width: `${progress}%`, // Dynamic width based on progress
      height: "100%",
      backgroundColor: "#5C6AC4",
      color: "white",
      textAlign: "center",
      lineHeight: "30px",
      transition: "width 0.3s ease",
    },

    button: {
      margin: "10px",
      padding: "10px 15px",
      cursor: "pointer",
    },
  };

  // Increase progress by 10, but not above 100
  const increaseProgress = () => {
    setProgress((prev) => Math.min(prev + 10, 100));
  };

  // Decrease progress by 10, but not below 0
  const decreaseProgress = () => {
    setProgress((prev) => Math.max(prev - 10, 0));
  };

  return (
    <div style={styles.main}>
      <h1>Progress Bar</h1>

      {/* Progress bar outer container */}
      <div style={styles.progressContainer}>
        {/* Progress bar inner fill */}
        <div style={styles.progressFill}>
          {progress}%
        </div>
      </div>

      <button style={styles.button} onClick={decreaseProgress}>
        Decrease
      </button>

      <button style={styles.button} onClick={increaseProgress}>
        Increase
      </button>
    </div>
  );
}

export default App;
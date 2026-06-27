/**
4. Progress Bars

Build a list of progress bars that fill up gradually when they are added to the page.
 */
import React, { useEffect, useState } from "react";

function App() {
  // Number of progress bars
  const [bars, setBars] = useState([]);

  // Add new progress bar
  const addProgressBar = () => {
    setBars([...bars, { id: Date.now() }]);
  };

  const styles = {
    main: {
      padding: "20px",
      fontFamily: "Arial",
    },
    button: {
      padding: "10px 16px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      borderRadius: "5px",
      cursor: "pointer",
      marginBottom: "20px",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Progress Bars</h1>

      <button style={styles.button} onClick={addProgressBar}>
        Add Progress Bar
      </button>

      {/* Render all progress bars */}
      {bars.map((bar) => (
        <ProgressBar key={bar.id} />
      ))}
    </div>
  );
}

// Separate component for each progress bar
function ProgressBar() {
  // Current progress percentage
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Increase progress every 50ms
    const timer = setInterval(() => {
      setProgress((prev) => {
        // Stop at 100%
        if (prev >= 100) {
          clearInterval(timer);
          return 100;
        }

        return prev + 1;
      });
    }, 50);

    // Cleanup interval when component unmounts
    return () => clearInterval(timer);
  }, []);

  const styles = {
    container: {
      width: "100%",
      height: "25px",
      backgroundColor: "#e0e0e0",
      borderRadius: "20px",
      marginBottom: "12px",
      overflow: "hidden",
    },
    fill: {
      width: `${progress}%`,
      height: "100%",
      backgroundColor: "#5C6AC4",
      transition: "width 0.05s linear",
      color: "white",
      textAlign: "center",
      lineHeight: "25px",
      fontSize: "12px",
    },
  };

  return (
    <div style={styles.container}>
      <div style={styles.fill}>{progress}%</div>
    </div>
  );
}

export default App;
import React, { useState, useEffect } from "react";

function App() {
  const [seconds, setSeconds] = useState(10);

  useEffect(() => {
    if (seconds <= 0) return;

    const timer = setInterval(() => {
      setSeconds((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [seconds]);

  return (
    <div>
      <h1>Countdown Timer</h1>

      <h2>{seconds}</h2>
    </div>
  );
}

export default App;
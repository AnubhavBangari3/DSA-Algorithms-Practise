/**
13. Dice Roller

Build a dice roller app that simulates the results of rolling 6-sided dice.
 */
import React, { useState } from "react";

function App() {
  // Stores the current dice value
  // Initially showing 1
  const [diceValue, setDiceValue] = useState(1);

  // Generate a random number between 1 and 6
  const rollDice = () => {
    const randomNumber = Math.floor(Math.random() * 6) + 1;

    // Update the dice value
    setDiceValue(randomNumber);
  };

  const styles = {
    main: {
      width: "400px",
      margin: "40px auto",
      textAlign: "center",
      fontFamily: "Arial",
    },

    dice: {
      width: "120px",
      height: "120px",
      margin: "20px auto",
      border: "3px solid #5C6AC4",
      borderRadius: "10px",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      fontSize: "60px",
      fontWeight: "bold",
      backgroundColor: "#f8f8f8",
    },

    button: {
      padding: "12px 20px",
      backgroundColor: "#5C6AC4",
      color: "white",
      border: "none",
      cursor: "pointer",
      borderRadius: "5px",
      fontSize: "16px",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Dice Roller</h1>

      {/* Dice Display */}
      <div style={styles.dice}>
        {diceValue}
      </div>

      {/* Roll Dice Button */}
      <button style={styles.button} onClick={rollDice}>
        Roll Dice
      </button>
    </div>
  );
}

export default App;
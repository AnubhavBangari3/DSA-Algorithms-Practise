/**
17. Star Rating

Build a star rating component that shows a row of star icons for users to select the number of filled stars corresponding to the rating.
 */

import React, { useState } from "react";

function App() {
  // Stores the selected rating
  const [rating, setRating] = useState(0);

  // Stores the star currently being hovered
  const [hoverRating, setHoverRating] = useState(0);

  const styles = {
    main: {
      textAlign: "center",
      marginTop: "60px",
      fontFamily: "Arial",
    },

    star: {
      fontSize: "40px",
      cursor: "pointer",
      margin: "5px",
      transition: "0.2s",
    },

    text: {
      marginTop: "20px",
      fontSize: "20px",
      fontWeight: "bold",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Star Rating</h1>

      {/* Render 5 stars */}
      {[1, 2, 3, 4, 5].map((star) => (
        <span
          key={star}
          style={{
            ...styles.star,

            // Fill stars based on hover value first,
            // otherwise use selected rating
            color:
              star <= (hoverRating || rating)
                ? "#f5b301"
                : "#ccc",
          }}
          onClick={() => setRating(star)}
          onMouseEnter={() => setHoverRating(star)}
          onMouseLeave={() => setHoverRating(0)}
        >
          ★
        </span>
      ))}

      {/* Show selected rating */}
      <div style={styles.text}>
        Rating: {rating} / 5
      </div>
    </div>
  );
}

export default App;
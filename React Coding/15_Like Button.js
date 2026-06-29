/**
15. Like Button

Build a Like button that changes appearance based on the states.
 */

import React, { useState } from "react";

function App() {
  // Stores whether the button is liked or not
  const [liked, setLiked] = useState(false);

  // Stores total likes
  const [likes, setLikes] = useState(100);

  // Toggle Like / Unlike
  const handleLike = () => {
    if (liked) {
      // If already liked, remove the like
      setLikes(likes - 1);
    } else {
      // If not liked, add one like
      setLikes(likes + 1);
    }

    // Toggle the liked state
    setLiked(!liked);
  };

  const styles = {
    main: {
      textAlign: "center",
      marginTop: "50px",
      fontFamily: "Arial",
    },

    button: {
      padding: "12px 20px",
      fontSize: "18px",
      border: "none",
      borderRadius: "8px",
      cursor: "pointer",
      color: "white",
      backgroundColor: liked ? "#e0245e" : "#5C6AC4",
      transition: "0.3s",
    },

    count: {
      marginTop: "20px",
      fontSize: "22px",
      fontWeight: "bold",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Like Button</h1>

      {/* Like Button */}
      <button style={styles.button} onClick={handleLike}>
        {liked ? "❤️ Liked" : "🤍 Like"}
      </button>

      {/* Total Likes */}
      <div style={styles.count}>
        Total Likes: {likes}
      </div>
    </div>
  );
}

export default App;
/**
10. Tweet

Build a component that resembles a Tweet from Twitter.
 */

import React, { useState } from "react";

function App() {
  // Stores whether tweet is liked or not
  const [liked, setLiked] = useState(false);

  // Stores current like count
  const [likes, setLikes] = useState(128);

  // Toggle like/unlike
  const handleLike = () => {
    if (liked) {
      setLikes(likes - 1);
    } else {
      setLikes(likes + 1);
    }

    setLiked(!liked);
  };

  const styles = {
    card: {
      width: "500px",
      margin: "40px auto",
      padding: "16px",
      border: "1px solid #ddd",
      borderRadius: "12px",
      fontFamily: "Arial",
    },
    header: {
      display: "flex",
      gap: "12px",
    },
    avatar: {
      width: "48px",
      height: "48px",
      borderRadius: "50%",
      backgroundColor: "#5C6AC4",
      color: "white",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      fontWeight: "bold",
    },
    name: {
      fontWeight: "bold",
    },
    username: {
      color: "#657786",
      fontSize: "14px",
    },
    tweetText: {
      marginTop: "12px",
      fontSize: "16px",
      lineHeight: "1.5",
    },
    meta: {
      color: "#657786",
      fontSize: "14px",
      marginTop: "10px",
    },
    actions: {
      display: "flex",
      justifyContent: "space-between",
      marginTop: "16px",
      color: "#657786",
    },
    actionButton: {
      border: "none",
      background: "transparent",
      cursor: "pointer",
      fontSize: "15px",
    },
  };

  return (
    <div style={styles.card}>
      {/* Tweet Header */}
      <div style={styles.header}>
        {/* Avatar */}
        <div style={styles.avatar}>A</div>

        {/* User Info */}
        <div>
          <div style={styles.name}>Anubhav Bangari</div>
          <div style={styles.username}>@anubhavdev · 2h</div>
        </div>
      </div>

      {/* Tweet Content */}
      <p style={styles.tweetText}>
        Learning React by building small UI components is one of the best ways
        to improve frontend skills.
      </p>

      {/* Tweet Time */}
      <div style={styles.meta}>10:30 AM · Jun 29, 2026</div>

      {/* Tweet Actions */}
      <div style={styles.actions}>
        <button style={styles.actionButton}>💬 12</button>
        <button style={styles.actionButton}>🔁 24</button>

        <button style={styles.actionButton} onClick={handleLike}>
          {liked ? "❤️" : "🤍"} {likes}
        </button>

        <button style={styles.actionButton}>📤 Share</button>
      </div>
    </div>
  );
}

export default App;
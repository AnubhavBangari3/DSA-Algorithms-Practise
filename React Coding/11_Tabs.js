/**
 11. Tabs

Build a tabs component that displays a list of tab elements and one associated panel of content at a time.
 */
import React, { useState } from "react";

function App() {
  // List of tabs with their corresponding content
  const tabs = [
    {
      title: "Home",
      content: "Welcome to the Home page.",
    },
    {
      title: "Profile",
      content: "This is your Profile page.",
    },
    {
      title: "Settings",
      content: "Manage your account settings here.",
    },
  ];

  // Stores the currently selected tab index
  // Initially, the first tab (Home) is selected
  const [activeTab, setActiveTab] = useState(0);

  const styles = {
    main: {
      width: "500px",
      margin: "40px auto",
      fontFamily: "Arial",
    },

    tabContainer: {
      display: "flex",
      borderBottom: "2px solid #ddd",
    },

   tab: {
  padding: "12px 20px",
  cursor: "pointer",
  border: "none",
  backgroundColor: "#f5f5f5", // changed
  fontSize: "16px",
},

activeTab: {
  backgroundColor: "#5C6AC4",
  color: "white",
  fontWeight: "bold",
},

    panel: {
      border: "1px solid #ddd",
      padding: "20px",
      marginTop: "10px",
      borderRadius: "5px",
      minHeight: "100px",
    },
  };

  return (
    <div style={styles.main}>
      <h1>Tabs Component</h1>

      {/* Render all tab buttons */}
      <div style={styles.tabContainer}>
        {tabs.map((tab, index) => (
          <button
            key={index}
            style={{
              ...styles.tab,
              ...(activeTab === index ? styles.activeTab : {}),
            }}
            onClick={() => setActiveTab(index)}
          >
            {tab.title}
          </button>
        ))}
      </div>

      {/* Display content of the selected tab */}
      <div style={styles.panel}>
        <h3>{tabs[activeTab].title}</h3>

        <p>{tabs[activeTab].content}</p>
      </div>
    </div>
  );
}

export default App;
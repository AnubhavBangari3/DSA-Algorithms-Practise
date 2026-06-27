/**
 3. Holy Grail

Build the famous holy grail layout consisting of a header, 3 columns, and a footer.
 */
import React from "react";

function App() {

  // Inline CSS styles
  const styles = {

    // Main container (Full screen)
    container: {
      display: "flex",
      flexDirection: "column", // Arrange Header -> Main -> Footer vertically
      height: "100vh", // Full viewport height
      fontFamily: "Arial",
    },

    // Header
    header: {
      backgroundColor: "#5C6AC4",
      color: "white",
      textAlign: "center",
      padding: "20px",
      fontSize: "24px",
      fontWeight: "bold",
    },

    // Middle section containing 3 columns
    main: {
      display: "flex", // Arrange children horizontally
      flex: 1, // Occupy remaining height
    },

    // Left Sidebar
    leftSidebar: {
      width: "200px", // Fixed width
      backgroundColor: "#f2f2f2",
      padding: "20px",
      borderRight: "1px solid #ccc",
    },

    // Main Content
    content: {
      flex: 1, // Occupies remaining available width
      padding: "20px",
      backgroundColor: "#ffffff",
      textAlign: "center",
    },

    // Right Sidebar
    rightSidebar: {
      width: "200px", // Fixed width
      backgroundColor: "#f2f2f2",
      padding: "20px",
      borderLeft: "1px solid #ccc",
    },

    // Footer
    footer: {
      backgroundColor: "#333",
      color: "white",
      textAlign: "center",
      padding: "20px",
      fontWeight: "bold",
    },
  };

  return (
    <div style={styles.container}>

      {/* ================= HEADER ================= */}
      <header style={styles.header}>
        Header
      </header>

      {/* ================= MAIN SECTION ================= */}
      <div style={styles.main}>

        {/* Left Sidebar */}
        <aside style={styles.leftSidebar}>
          <h3>Left Sidebar</h3>
          <p>Navigation Links</p>
          <p>Dashboard</p>
          <p>Profile</p>
          <p>Settings</p>
        </aside>

        {/* Main Content */}
        <main style={styles.content}>
          <h2>Main Content</h2>

          <p>
            This is the main content area.
          </p>

          <p>
            Since it uses <b>flex: 1</b>, it automatically
            occupies the remaining width after the left and
            right sidebars.
          </p>

          <p>
            This is exactly how the Holy Grail Layout works.
          </p>
        </main>

        {/* Right Sidebar */}
        <aside style={styles.rightSidebar}>
          <h3>Right Sidebar</h3>
          <p>Advertisements</p>
          <p>Latest News</p>
          <p>Widgets</p>
        </aside>

      </div>

      {/* ================= FOOTER ================= */}
      <footer style={styles.footer}>
        Footer
      </footer>

    </div>
  );
}

export default App;
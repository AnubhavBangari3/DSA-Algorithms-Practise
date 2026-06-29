/**
14. File Explorer

Build a file explorer component to navigate files and directories in a tree-like hierarchical viewer.
 */
import React, { useState } from "react";

function App() {
  // Sample file/folder structure
  const fileData = {
    name: "root",
    type: "folder",
    children: [
      {
        name: "src",
        type: "folder",
        children: [
          { name: "App.jsx", type: "file" },
          { name: "index.js", type: "file" },
          {
            name: "components",
            type: "folder",
            children: [
              { name: "Header.jsx", type: "file" },
              { name: "Footer.jsx", type: "file" },
            ],
          },
        ],
      },
      {
        name: "public",
        type: "folder",
        children: [
          { name: "index.html", type: "file" },
          { name: "favicon.ico", type: "file" },
        ],
      },
      { name: "package.json", type: "file" },
    ],
  };

  return (
    <div style={styles.main}>
      <h1>File Explorer</h1>

      {/* Render root folder */}
      <FileNode node={fileData} />
    </div>
  );
}

// Recursive component to render both files and folders
function FileNode({ node }) {
  // Controls whether a folder is expanded or collapsed
  const [isOpen, setIsOpen] = useState(false);

  // Check if current node is a folder
  const isFolder = node.type === "folder";

  return (
    <div style={styles.node}>
      <div
        style={styles.row}
        onClick={() => {
          // Only folders should expand/collapse
          if (isFolder) {
            setIsOpen(!isOpen);
          }
        }}
      >
        {/* Folder icon changes based on open/close state */}
        {isFolder ? (isOpen ? "📂" : "📁") : "📄"} {node.name}
      </div>

      {/* Render children only when folder is open */}
      {isFolder && isOpen && (
        <div style={styles.children}>
          {node.children.map((child, index) => (
            <FileNode key={index} node={child} />
          ))}
        </div>
      )}
    </div>
  );
}

const styles = {
  main: {
    width: "450px",
    margin: "40px auto",
    padding: "20px",
    fontFamily: "Arial",
    border: "1px solid #ddd",
    borderRadius: "8px",
  },

  node: {
    marginTop: "6px",
  },

  row: {
    cursor: "pointer",
    padding: "6px",
    borderRadius: "4px",
  },

  children: {
    marginLeft: "20px",
    borderLeft: "1px solid #ddd",
    paddingLeft: "10px",
  },
};

export default App;
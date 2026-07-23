import React from 'react';
import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)
  
  const styles = {
    main: {
      padding: '20px',
    },
    title: {
      color: '#5C6AC4'
    },
    butD:{
      display:'flex',justifyContent:'space-between'
    }
  };

  return (
    <div style={styles.main}>
      <h1 style={styles.title}>{count}</h1>
      <div style={styles.butD}>
        <button onClick={() => setCount((count) => count + 1)}>
          +
        </button>
        <button onClick={() => setCount((count) => count - 1)}>
          - 
        </button>
      </div>
    </div>
  )
}

export default App

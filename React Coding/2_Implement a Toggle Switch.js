import React from 'react';
import { useState } from 'react'

function App() {
  const [toggle, setToggle] = useState(false)
  
  const styles = {
   
  };

  return (
    <div >
      
      <div>
        <button onClick={() => setToggle(!toggle)}>
          {toggle ? 'Off' : `On`}
        </button>
        
      </div>
    </div>
  )
}

export default App

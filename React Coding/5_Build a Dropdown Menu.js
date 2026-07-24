import React, { useState } from "react";

const SearchBar = ({items}) =>{

const [isOpen,setIsOpen]=useState(false);


return (
  <div>
   <button onClick={() => setIsOpen(!isOpen)} >Toggle</button>
   {isOpen && (
    <ul>
      {
        items.map((item,index) => (
          <li key={index}>{item}</li>
        ))
      }
    </ul>
   )}
  
  </div>
)

}

function App() {
  const items = ['Profile', 'Settings', 'Logout'];

  return (
    <div>
      <SearchBar items={items}  />
    </div>
  );
}

export default App;
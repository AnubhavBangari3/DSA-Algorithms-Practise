import React, { useState } from "react";

const SearchBar = ({items}) =>{
const [query,setQuery]=useState('');
const filteredItems = items.filter(item => item.toLowerCase().includes(query.toLowerCase()))

return (
  <div>
    <input type="text" value={query} onChange={(e)=> setQuery(e.target.value)}
    placeholder="Searching ..." />

    <ul>
    
    {filteredItems.map((item,id)=>(
      <li key={id}>{item}</li>
    ))}
    </ul>
  
  </div>
)

}

function App() {
  const items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'];

  return (
    <div>
      <SearchBar items={items} />
    </div>
  );
}

export default App;
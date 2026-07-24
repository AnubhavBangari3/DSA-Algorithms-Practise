import React, { useState } from "react";

const Tabs = ({tabs}) =>{

const [active,setActive]=useState(0);

return (
  <div>
    <div className="tab-buttons">
      {tabs.map((tab,index) => (
        <button key={index} 
        className={index === active ?'active':''}  
        onClick={() => setActive(index)} >{tab.label}</button>


      ))}
    </div>
    <div className="tab-content">
     {tabs[active].content}
    </div>
   
  </div>
)

}

function App() {
  const tabs = [
    { label: 'Tab 1', content: <div>Content of Tab 1</div> },
    { label: 'Tab 2', content: <div>Content of Tab 2</div> },
    { label: 'Tab 3', content: <div>Content of Tab 3</div> },
  ];

  return (
    <div>
    <Tabs tabs={tabs} />
      
    </div>
  );
}

export default App;
import React, { useState } from 'react';

const DynamicForm = () => {
  const [fields, setFields] = useState([{ value: '' }]);

  const handleChange = (index, event) => {
    const newFields = fields.slice();
    newFields[index].value = event.target.value;
    setFields(newFields);
  };

  const handleAdd = () => {
    setFields([...fields, { value: '' }]);
  };

  const handleRemove = (index) => {
    const newFields = fields.slice();
    newFields.splice(index, 1);
    setFields(newFields);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', fields);
  };

  return (
    <form onSubmit={handleSubmit}>
      {fields.map((field, index) => (
        <div key={index}>
          <input
            type="text"
            value={field.value}
            onChange={(e) => handleChange(index, e)}
          />
          <button type="button" onClick={() => handleRemove(index)}>Remove</button>
        </div>
      ))}
      <button type="button" onClick={handleAdd}>Add Field</button>
      <button type="submit">Submit</button>
    </form>
  );
};

const App = () => {
  return (
    <div>
      <h1>Dynamic Form</h1>
      <DynamicForm />
    </div>
  );
};

export default App;
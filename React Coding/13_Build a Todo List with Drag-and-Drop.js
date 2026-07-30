import React, { useState } from "react";

function App() {
  const [text, setText] = useState("");

  const [todos, setTodos] = useState([
    { id: 1, text: "Learn React" },
    { id: 2, text: "Practice JavaScript" },
    { id: 3, text: "Prepare for interview" }
  ]);

  const [draggedIndex, setDraggedIndex] = useState(null);

  const addTodo = () => {
    if (!text.trim()) return;

    const newTodo = {
      id: Date.now(),
      text: text
    };

    setTodos([...todos, newTodo]);
    setText("");
  };

  const removeTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  const handleDragStart = (index) => {
    setDraggedIndex(index);
  };

  const handleDragOver = (event) => {
    // Required to allow dropping
    event.preventDefault();
  };

  const handleDrop = (dropIndex) => {
    if (draggedIndex === null) return;

    const updatedTodos = [...todos];

    // Remove the dragged todo
    const draggedTodo = updatedTodos.splice(draggedIndex, 1)[0];

    // Insert it at the dropped position
    updatedTodos.splice(dropIndex, 0, draggedTodo);

    setTodos(updatedTodos);
    setDraggedIndex(null);
  };

  return (
    <div>
      <h1>Drag-and-Drop Todo List</h1>

      <input
        type="text"
        value={text}
        placeholder="Enter todo"
        onChange={(event) => setText(event.target.value)}
      />

      <button onClick={addTodo}>Add</button>

      <ul>
        {todos.map((todo, index) => (
          <li
            key={todo.id}
            draggable
            onDragStart={() => handleDragStart(index)}
            onDragOver={handleDragOver}
            onDrop={() => handleDrop(index)}
            style={{
              cursor: "grab",
              margin: "10px",
              padding: "10px",
              border: "1px solid black"
            }}
          >
            {todo.text}

            <button onClick={() => removeTodo(todo.id)}>
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
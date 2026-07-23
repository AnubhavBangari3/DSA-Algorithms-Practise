import React, { useState } from "react";

function App() {
  const [todos, setTodos] = useState([]);
  const [text, setText] = useState("");

  const addTodo = () => {
    if (text.trim()) {
      setTodos([
        ...todos,
        {
          text: text.trim(),
          completed: false,
        },
      ]);

      setText("");
    }
  };

  const toggleTodo = (index) => {
    const updatedTodos = [...todos];

    updatedTodos[index] = {
      ...updatedTodos[index],
      completed: !updatedTodos[index].completed,
    };

    setTodos(updatedTodos);
  };

  const removeTodo = (index) => {
    const updatedTodos = [...todos];
    updatedTodos.splice(index, 1);
    setTodos(updatedTodos);
  };

  return (
    <div>
      <input
        value={text}
        onChange={(event) => setText(event.target.value)}
        placeholder="Enter a task"
      />

      <button onClick={addTodo}>Add</button>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            <span
              style={{
                textDecoration: todo.completed ? "line-through" : "none",
              }}
            >
              {todo.text}
            </span>

            <button onClick={() => toggleTodo(index)}>
              {todo.completed ? "Undo" : "Complete"}
            </button>

            <button onClick={() => removeTodo(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
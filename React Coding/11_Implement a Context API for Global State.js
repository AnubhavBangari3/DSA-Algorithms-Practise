import React, { createContext, useContext, useState } from "react";

// 1. Create Context
const UserContext = createContext();

// 2. Create Provider
const UserProvider = ({ children }) => {
  const [user, setUser] = useState({
    name: "Anubhav",
    role: "Developer"
  });

  const updateUser = () => {
    setUser({
      name: "Rahul",
      role: "Senior Developer"
    });
  };

  return (
    <UserContext.Provider value={{ user, updateUser }}>
      {children}
    </UserContext.Provider>
  );
};

// 3. Consume Context
const Profile = () => {
  const { user, updateUser } = useContext(UserContext);

  return (
    <div>
      <h2>User Profile</h2>
      <p>Name: {user.name}</p>
      <p>Role: {user.role}</p>

      <button onClick={updateUser}>Update User</button>
    </div>
  );
};

function App() {
  return (
    <UserProvider>
      <Profile />
    </UserProvider>
  );
}

export default App;
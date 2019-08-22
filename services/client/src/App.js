import React from 'react';
import logo from './logo.svg';
import './App.css';
import SubscribeForm from './SubscribeForm.js';
import UserList from './UserList.js';



function App() {
  return (
    <div className="App">
      <SubscribeForm />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Store Name</h1>
      </header>
      <UserList />
    </div>
  );
}

export default App;

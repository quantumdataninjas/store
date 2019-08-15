import React from 'react';
import logo from './logo.svg';
import './App.css';
import Subscribe from './Subscribe.js';



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Store Name</h1>
      </header>
      <Subscribe />
    </div>
  );
}

export default App;

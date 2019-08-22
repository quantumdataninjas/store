import React from 'react';
import logo from './logo.svg';
import './App.css';
import SimpleUserList from './SimpleUserList';
import SubscribeForm from './SubscribeForm';



function App() {
  return (
    <div className="App">
      <SubscribeForm />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Store Name</h1>
      </header>
      <SimpleUserList />
    </div>
  );
}

export default App;

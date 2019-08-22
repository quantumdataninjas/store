import React from 'react';
import logo from 'assets/img/logo.svg';
import 'assets/scss/App.scss';
import SimpleUserList from 'components/SimpleUserList';
import SubscribeForm from 'components/SubscribeForm';



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

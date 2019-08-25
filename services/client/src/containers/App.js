import React, { Component } from 'react'
import logo from 'assets/img/logo.svg'
import 'assets/scss/App.scss'
import SimpleUserList from './Users/SimpleUserList'
import UserList from './Users/UserList'
import SubscribeForm from './Auth/SubscribeForm'



class App extends Component {
  render() {
    return (
      <div className="App">
        <SubscribeForm />
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>Store Name</h1>
        </header>
        <SimpleUserList />
        <UserList />
      </div>
    )
  }
}

export default App;

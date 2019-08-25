import React, { Component } from 'react'
import logo from 'assets/img/logo.svg'
import 'assets/scss/App.scss'
import SimpleUserListContainer from './Users/SimpleUserListContainer'
import UserListContainer from './Users/UserListContainer'
import SubscribeForm from './Auth/SubscribeForm'
import ProductsContainer from './ProductsContainer'
import CartContainer from './CartContainer'



class App extends Component {
  render() {
    return (
      <div className="App">
        <SubscribeForm />
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>Store Name</h1>
        </header>
        <SimpleUserListContainer />
        <UserListContainer />
        <hr />
        <ProductsContainer />
        <hr />
        <CartContainer />
      </div>
    )
  }
}

export default App;

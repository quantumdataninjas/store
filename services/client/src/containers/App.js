import React, { Component } from 'react';
import logo from 'assets/img/logo.svg';
import 'assets/scss/App.scss';
import SimpleUsersContainer from './Users/SimpleUsersContainer';
import UsersContainer from './Users/UsersContainer';
import SubscribeForm from './Auth/SubscribeForm';
import ProductsContainer from './ProductsContainer';
import CartContainer from './CartContainer';


class App extends Component {

  render() {
    return (
      <div className="App">
        <SubscribeForm />
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>Store Name</h1>
        </header>
        <SimpleUsersContainer />
        <UsersContainer />
        <hr />
        <ProductsContainer />
        <hr />
        <CartContainer />
      </div>
    );
  };
};

export default App;

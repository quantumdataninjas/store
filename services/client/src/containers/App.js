import React, { Component } from 'react'
import { connect } from 'react-redux'
import logo from 'assets/img/logo.svg'
import 'assets/scss/App.scss'
import SimpleUsersContainer from './Users/SimpleUsersContainer'
import UsersContainer from './Users/UsersContainer'
import SubscribeForm from './Auth/SubscribeForm'
import ProductsContainer from './ProductsContainer'
import CartContainer from './CartContainer'
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles'


export class App extends Component {

  constructor(props){
    super(props)
    this.state = {
      palette: {
        type: "dark"
      }
    }
  }

  toggleDarkTheme() {
    let newPaletteType = this.state.palette.type === "light" ? "dark" : "light"
    this.setState({
      palette: newPaletteType
    })
  }

  render() {
    const muiTheme = createMuiTheme(this.state)
    return (
      <MuiThemeProvider theme={muiTheme}>
        <div className="App">
          <SubscribeForm />
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <h1>Store Name</h1>
          </header>
          <hr /><br />
          <SimpleUsersContainer />
          <hr /><br />
          <UsersContainer />
          <hr />
          <ProductsContainer />
          <hr />
          <CartContainer />
        </div>
      </MuiThemeProvider>
    )
  }
}

const mapStateToProps = (state) => ({
})

export default connect(
  mapStateToProps
)(App)

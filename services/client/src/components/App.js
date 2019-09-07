import React, { Component } from 'react'
import { connect } from 'react-redux'
import logo from 'assets/img/logo.svg'
import 'assets/scss/App.scss'
import SimpleUsers from '../containers/Users/SimpleUsers'
import UsersContainer from '../containers/Users/UsersContainer'
import SubscribeForm from 'components/Auth/SubscribeForm'
import SignupForm from 'components/Auth/SignupForm'
import ProductsContainer from '../containers/ProductsContainer'
import CartContainer from '../containers/CartContainer'
import { Paper, Typography } from '@material-ui/core'
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles'


class App extends Component {

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
            {/* <h1>Store Name</h1> */}
            <Typography component="h1">
              Store Name
            </Typography>
            <SignupForm />
          </header>
          <SimpleUsers />
          <UsersContainer />
          <ProductsContainer />
          <CartContainer />
        </div>
      </MuiThemeProvider>
    )
  }
}

export default App

// const mapStateToProps = (state) => ({
// })

// export default connect(
//   mapStateToProps
// )(App)

import React, { Component } from 'react'
import { connect } from 'react-redux'
import logo from 'assets/img/logo.svg'
import 'assets/scss/App.scss'
import SimpleUsersContainer from './Users/SimpleUsersContainer'
import UsersContainer from './Users/UsersContainer'
import SubscribeForm from 'components/Auth/SubscribeForm'
<<<<<<< HEAD:services/client/src/components/App.js
import SignupForm from 'components/Auth/SignupForm'
import ProductsContainer from '../containers/ProductsContainer'
import CartContainer from '../containers/CartContainer'
||||||| merged common ancestors:services/client/src/components/App.js
import ProductsContainer from '../containers/ProductsContainer'
import CartContainer from '../containers/CartContainer'
=======
import ProductsContainer from './ProductsContainer'
import CartContainer from './CartContainer'
>>>>>>> 66ad30331d8b93be03074765d0c642358ca2a11b:services/client/src/containers/App.js
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
          <SimpleUsersContainer />
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

import React from 'react'
import ReactDOM from 'react-dom'
// import { createBrowserHistory } from 'history'
import { Provider } from 'react-redux'
import configureStore from 'stores'
import 'assets/scss/index.scss'
import App from 'components/App'
// import App from 'containers/App'
import * as serviceWorker from 'serviceWorker'


/**
https://github.com/creativetimofficial/react-redux-tutorial/blob/master/Part%204/paper-dashboard-react/src/index.js

use with react router (check above link)
const hist = createBrowserHistory()
**/

const store = configureStore()

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister()

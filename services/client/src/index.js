import React from 'react';
import ReactDOM from 'react-dom';
import { createBrowserHistory } from 'history';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import { createLogger } from 'redux-logger';
import thunk from 'redux-thunk';
// import reducer from './reducers';

import 'assets/scss/index.scss';
import App from 'containers/App';
import * as serviceWorker from 'serviceWorker';


const hist = createBrowserHistory();
const middleware = [ thunk ];
if(process.env.NODE_ENV !== 'production') {
  middleware.push(createLogger());
}


ReactDOM.render(
  <Provider>
    <App />
  </Provider>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

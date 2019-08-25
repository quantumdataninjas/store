import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import promise from 'redux-promise';
import { createLogger } from 'redux-logger';
import rootReducer from 'reducers';
import {
  getSimpleUserList,
  getUserList,
  getAllProducts
} from 'actions';


const middleware = [ thunk, promise ];
if(process.env.NODE_ENV !== 'production') {
  middleware.push(createLogger());
}
const middlewareEnhancer = applyMiddleware(...middleware);
const composedEnhancers = compose(middlewareEnhancer);

const configureStore = (state={}) => {
  const store = createStore(
    rootReducer,
    composedEnhancers,
  );
  if(process.env.NODE_ENV !== 'production' && module.hot) {
    module.hot.accept('reducers', () => store.replaceReducer(rootReducer));
  }
  store.dispatch(getSimpleUserList());
  store.dispatch(getUserList());
  store.dispatch(getAllProducts());
  return store;
};

export default configureStore;

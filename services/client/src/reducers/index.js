import { combineReducers } from 'redux';
import simpleUsersReducer from './simpleUsers';
import usersReducer from './users';
import cartReducer, * as fromCart from './cart';
import productsReducer, * as fromProducts from './products';


export default combineReducers({
  simple_users: simpleUsersReducer,
  users: usersReducer,
  cart: cartReducer,
  products: productsReducer
});

// const getSimpleUserList = state =>

const getAddedIds = state => fromCart.getAddedIds(state.cart);
const getQuantity = (state, id) => fromCart.getQuantity(state.cart, id);
const getProduct = (state, id) => fromProducts.getProduct(state.products, id);

export const getTotal = state =>
  getAddedIds(state).reduce((total, id) =>
    total + getProduct(state, id).price * getQuantity(state, id), 0
  ).toFixed(2);

export const getCartProducts = state =>
  getAddedIds(state).map(id => ({
    ...getProduct(state, id),
    quantity: getQuantity(state, id)
  }));

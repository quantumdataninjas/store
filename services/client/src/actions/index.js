import axios from 'axios';
import shop from 'api/shop';
import * as types from 'constants/ActionTypes';


const getSimpleUsers = simple_users => ({
  type: types.GET_SIMPLE_USERS,
  simple_users
});

export const getSimpleUserList = () => dispatch => {
  axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users/simple`)
  .then((res) => {
    res.data.simple_users.forEach(user => {
      user.last_signin = new Date(user.last_signin);
      user.last_signout = new Date(user.last_signout);
      user.created_at = new Date(user.created_at);
    });
    dispatch(getSimpleUsers(res.data.simple_users));
  })
  .catch((err) => {
    console.log(err);
  });
};

const getUsers = users => ({
  type: types.GET_USERS,
  users
});

export const getUserList = () => dispatch => {
  axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
  .then((res) => {
    res.data.users.forEach(user => {
      user.birthday = new Date(user.birthday);
      user.last_signin = new Date(user.last_signin);
      user.last_signout = new Date(user.last_signout);
      user.created_at = new Date(user.created_at);
    });
    dispatch(getUsers(res.data.users))
  })
  .catch((err) => {
    console.log(err);
  });
};

const receiveProducts = products => ({
  type: types.RECEIVE_PRODUCTS,
  products
});

export const getAllProducts = () => dispatch => {
  shop.getProducts(products => {
    dispatch(receiveProducts(products));
  });
};

const addToCartUnsafe = productId => ({
  type: types.ADD_TO_CART,
  productId
});

export const addToCart = productId => (dispatch, getState) => {
  if (getState().products.byId[productId].inventory > 0) {
    dispatch(addToCartUnsafe(productId));
  }
};

export const checkout = products => (dispatch, getState) => {
  const { cart } = getState();

  dispatch({
    type: types.CHECKOUT_REQUEST
  });
  shop.buyProducts(products, () => {
    dispatch({
      type: types.CHECKOUT_SUCCESS,
      cart
    });
    // Replace the line above with line below to rollback on failure:
    // dispatch({ type: types.CHECKOUT_FAILURE, cart })
  });
};

import axios from 'axios'
import shop from 'api/shop'
import * as types from 'constants/ActionTypes'


export const toggleDarkTheme = theme => dispatch => {
  dispatch({
    type: types.TOGGLE_DARK_THEME,
    theme
  })
}


const receiveSimpleUsers = simple_users => ({
  type: types.GET_SIMPLE_USERS,
  simple_users
})

export const getSimpleUsers = () => dispatch => {
  axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users/simple`)
  .then((res) => {
    res.data.simple_users.forEach(user => {
      user.last_signin = new Date(user.last_signin)
      user.last_signout = new Date(user.last_signout)
      user.created_at = new Date(user.created_at)
    })
    dispatch(receiveSimpleUsers(res.data.simple_users))
  })
  .catch((err) => {
    console.log(err)
  })
}

export const createSimpleUser = simple_user => {
  return {
    type: types.SIMPLE_USER_CREATED,
    simple_user
  }
  // dispatch(getSimpleUsers())
}

// const subscribe = 

const receiveUsers = users => ({
  type: types.GET_USERS,
  users
})

export const getUsers = () => dispatch => {
  axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
  .then((res) => {
    res.data.users.forEach(user => {
      user.birthday = new Date(user.birthday)
      user.last_signin = new Date(user.last_signin)
      user.last_signout = new Date(user.last_signout)
      user.created_at = new Date(user.created_at)
    })
    dispatch(receiveUsers(res.data.users))
  })
  .catch((err) => {
    console.log(err)
  })
}

const receiveProducts = products => ({
  type: types.RECEIVE_PRODUCTS,
  products
})

export const getAllProducts = () => dispatch => {
  shop.getProducts(products => {
    dispatch(receiveProducts(products))
  })
}

const addToCartUnsafe = productId => ({
  type: types.ADD_TO_CART,
  productId
})

export const addToCart = productId => (dispatch, getState) => {
  if (getState().products.byId[productId].inventory > 0) {
    dispatch(addToCartUnsafe(productId))
  }
}

export const checkout = products => (dispatch, getState) => {
  const { cart } = getState()

  dispatch({
    type: types.CHECKOUT_REQUEST
  })
  shop.buyProducts(products, () => {
    dispatch({
      type: types.CHECKOUT_SUCCESS,
      cart
    })
    // Replace the line above with line below to rollback on failure:
    // dispatch({ type: types.CHECKOUT_FAILURE, cart })
  })
}

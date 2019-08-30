import { GET_SIMPLE_USERS, SIMPLE_USER_CREATED } from 'constants/ActionTypes'


const initialState = []

const simple_users = (state=initialState, action) => {
  switch(action.type) {
    case GET_SIMPLE_USERS:
      return [...state, ...action.simple_users]
    case SIMPLE_USER_CREATED:
      console.log('SIMPLE_USER_CREATED')
      return [...state, ...action.simple_users]
    default:
      return state
  }
}

export default simple_users

import { SIMPLE_USER_CREATED } from 'constants/ActionTypes'

const initialState = {
  simple_users: []
}

const simpleUserList = (state=initialState, action) => {
  switch(action.type) {
    case SIMPLE_USER_CREATED:
      return [...state.simple_users, action.data]
    default:
      return state
  }
}

export default simpleUserList

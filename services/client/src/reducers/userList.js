import { USER_CREATED } from 'constants/ActionTypes'

const initialState = {
  users: []
}

const userList = (state=initialState, action) => {
  switch(action.type) {
    case USER_CREATED:
      return [...state.users, action.data]
    default:
      return state
  }
}

export default userList

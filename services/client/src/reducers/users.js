import { GET_USERS, USER_CREATED } from 'constants/ActionTypes';


const users = (state=[], action) => {
  switch(action.type) {
    case GET_USERS:
      return [...state, ...action.users];
    case USER_CREATED:
      return [...state, ...action.users];
    default:
      return state;
  };
};

export default users;

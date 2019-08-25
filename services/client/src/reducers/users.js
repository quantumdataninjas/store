import { GET_USERS, USER_CREATED } from 'constants/ActionTypes';


const usersReducer = (state=[], action) => {
  console.log("action: " + JSON.stringify(action));
  switch(action.type) {
    case GET_USERS:
      return [...state, ...action.users];
    case USER_CREATED:
      return [...state, ...action.users];
    default:
      return state;
  };
};

export default usersReducer;

import { GET_SIMPLE_USERS, SIMPLE_USER_CREATED } from 'constants/ActionTypes';


const simple_users = (state=[], action) => {
  console.log("action: " + JSON.stringify(action));
  switch(action.type) {
    case GET_SIMPLE_USERS:
      return [...state, ...action.simple_users];
    case SIMPLE_USER_CREATED:
      return [...state, ...action.simple_users];
    default:
      return state;
  };
};

export default simple_users;

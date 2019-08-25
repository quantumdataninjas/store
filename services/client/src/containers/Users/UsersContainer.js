import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
// import reducer from 'reducers';
// import SimpleUserData from 'components/Users/SimpleUserData';
// import SimpleUserList from 'components/Users/SimpleUserList';

class UsersContainer extends Component {

  static propTypes = {
    users: PropTypes.arrayOf(PropTypes.shape({
      id: PropTypes.number.isRequired,
      email: PropTypes.string.isRequired,
      subscribed: PropTypes.bool.isRequired,
      signed_up: PropTypes.bool.isRequired,
      online: PropTypes.bool.isRequired,
      last_signin: PropTypes.instanceOf(Date).isRequired,
      last_signout: PropTypes.instanceOf(Date).isRequired,
      created_at: PropTypes.instanceOf(Date).isRequired
    })).isRequired
  };

  userList() {
    return (
      this.props.users.map(user =>
        <h4
          key={user.id}
          className="box title is-4"
        >{ user.email }
        </h4>
      )
    );
  };

  render() {
    console.log("state: " + JSON.stringify(this.state));
    console.log("props: " + JSON.stringify(this.props));
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">User List</h1>
              <hr/><br/>
              {/* new */}
              { this.userList() }
            </div>
          </div>
        </div>
      </section>
    );
    // return (
    //   <SimpleUserList
    //     simple_users={this.props.simple_users.list} />
    // );
  };
};

const mapStateToProps = (state) => ({
  users: state.users
});

export default connect(
  mapStateToProps,
)(UsersContainer);

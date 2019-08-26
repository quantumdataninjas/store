import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { getSimpleUserList } from 'actions';
// import reducer from 'reducers';
// import SimpleUserData from 'components/Users/SimpleUserData';
import SimpleUserTable from 'components/Users/SimpleUserTable';

class SimpleUsersContainer extends Component {

  static propTypes = {
    simple_users: PropTypes.arrayOf(PropTypes.shape({
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

  simpleUserList() {
    return (
      this.props.simple_users.map(user =>
        <h4
          key={user.id}
          className="box title is-4"
        >{ user.email }
        </h4>
      )
    );
  };

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">Simple User List</h1>
              <hr/><br/>
              {/* new */}
              { this.simpleUserList() }
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
  simple_users: state.simple_users
});

const mapDispatchToProps = dispatch => ({
  getSimpleUserList: dispatch(getSimpleUserList)
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(SimpleUsersContainer);

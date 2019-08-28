import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import {
  getSimpleUsers,
  // simpleUserCreated
} from 'actions'
// import reducer from 'reducers'
import SimpleUserTable from 'components/Users/SimpleUserTable'

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
  }

  render() {
    const { simple_users } = this.props
    return (
      <SimpleUserTable simple_users={simple_users} />
    )
  }
}

const mapStateToProps = (state) => ({
  simple_users: state.simple_users
})

const mapDispatchToProps = dispatch => ({
  getSimpleUsers: dispatch(getSimpleUsers),
  // simpleUserCreated: dispatch(simpleUserCreated)
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(SimpleUsersContainer)

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { getUserList } from 'actions'
// import reducer from 'reducers'
import UserTable from 'components/Users/UserTable'

class UsersContainer extends Component {

  static propTypes = {
    users: PropTypes.arrayOf(PropTypes.shape({
      id: PropTypes.number.isRequired,
      email: PropTypes.string.isRequired,
      subscribed: PropTypes.bool.isRequired,
      terms_and_conditions: PropTypes.bool.isRequired,
      verified: PropTypes.bool.isRequired,
      firstname: PropTypes.string.isRequired,
      middlename: PropTypes.string,
      lastname: PropTypes.string.isRequired,
      address1: PropTypes.string.isRequired,
      address2: PropTypes.string,
      city: PropTypes.string.isRequired,
      state: PropTypes.string.isRequired,
      zipcode: PropTypes.string.isRequired,
      country: PropTypes.string.isRequired,
      phone: PropTypes.string,
      birthday: PropTypes.instanceOf(Date).isRequired,
      online: PropTypes.bool.isRequired,
      last_signin: PropTypes.instanceOf(Date).isRequired,
      last_signout: PropTypes.instanceOf(Date).isRequired,
      created_at: PropTypes.instanceOf(Date).isRequired
    })).isRequired
  }

  render() {
    const { users } = this.props
    return (
      <UserTable
        users={users} />
    )
  }
}

const mapStateToProps = (state) => ({
  users: state.users
})

const mapDispatchToProps = dispatch => ({
  getUserList: dispatch(getUserList)
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(UsersContainer)

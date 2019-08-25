import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { getSimpleUserList } from 'actions'
import reducer from 'reducers'
import SimpleUserList from 'components/SimpleUserList'

class SimpleUserListContainer extends Component {
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

  /**
  -- setup default props if necessary

  static defaultProps = {
  }
  **/

  /**
  constructor() {
    super()

    // this.state = {
    //   simple_users: []
    // }

    // this.handleChange = this.handleChange.bind(this)
    // this.handleSubmit = this.handleSubmit.bind(this)
  }
  **/

  // componentDidMount() {
  //   this.getSimpleUsers()
  // }

  // getSimpleUsers() {
  //   axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users/simple`)
  //   .then((res) => {
  //     // console.log(res)
  //     this.setState({
  //       simple_users: res.data.data.simple_users
  //     })
  //   })
  //   .catch((err) => { console.log(err) })
  // }

  // handleChange(event) {
  //   this.setState({value: event.target.value})
  // }
  //
  // handleSubmit(event) {
  //   axios({
  //     method: 'post',
  //     url: `${process.env.REACT_APP_USERS_SERVICE_URL}/users/subscribe`,
  //     data: {
  //       email: this.state.value
  //     },
  //     responseType: 'application/json'
  //   })
  //   .then((res) => { console.log(res) })
  //   .catch((err) => { console.log(err) })
  //   event.preventDefault()
  // }

  render() {
    return (
      <SimpleUserList
        simple_users={this.props.simple_users} />
    )
  }
}

const mapStateToProps = (state) => ({
  simple_users: getSimpleUserList(state)
})

export default connect(
  mapStateToProps,
  { getSimpleUserList }
)(SimpleUserListContainer)

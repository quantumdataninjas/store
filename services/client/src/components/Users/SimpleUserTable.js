import React, { Component } from 'react';
import PropTypes from 'prop-types';

class SimpleUserList extends Component {

  static propTypes = {
    simple_users: PropTypes.array
  };

  /**
  constructor(props) {
    super(props)

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

  simpleUserList() {
    return (
      this.props.simple_users.map(simple_user =>
        <h4
          key={simple_user.id}
          className="box title is-4"
        >{ simple_user.email }
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
  };
}

export default SimpleUserList;

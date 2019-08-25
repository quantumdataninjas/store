import React, { Component } from 'react';
import PropTypes from 'prop-types';


class UserData extends Component {

  static propTypes = {
    users: PropTypes.array
  };
  /**
  constructor() {
    super()

    // this.state = {
    //   users: []
    // }

    // this.handleChange = this.handleChange.bind(this)
    // this.handleSubmit = this.handleSubmit.bind(this)
  }
  **/

  // componentDidMount() {
  //   this.getUsers()
  // }

  // getUsers() {
  //   axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
  //   .then((res) => {
  //     // console.log(res)
  //     this.setState({
  //       users: res.data.data.users
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
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">User List</h1>
              <hr/><br/>
              {/* new */}
              {
                this.state.users.map((user) => {
                  return (
                    <h4
                      key={user.id}
                      className="box title is-4"
                    >{ user.email }
                    </h4>
                  )
                })
              }
            </div>
          </div>
        </div>
      </section>
    );
  };
};

export default UserData;

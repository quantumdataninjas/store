import React, { Component } from 'react';
import axios from 'axios';

class UserList extends Component {
  constructor() {
    super();
    // this.state = {
    //   value: ''
    // };
    this.getUserList();
    // this.handleChange = this.handleChange.bind(this);
    // this.handleSubmit = this.handleSubmit.bind(this);
  }

  getUserList() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { console.log(res); })
    .catch((err) => { console.log(err); });
  }

  // handleChange(event) {
  //   this.setState({value: event.target.value});
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
  //   .then((res) => { console.log(res); })
  //   .catch((err) => { console.log(err); });
  //   event.preventDefault();
  // }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">All Users</h1>
              <hr/><br/>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default UserList;

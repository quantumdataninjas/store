import React, { Component } from 'react';
import axios from 'axios';

class SubscribeForm extends Component {
  constructor() {
    super();
    this.state = {
      value: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    axios({
      method: 'post',
      url: `${process.env.REACT_APP_USERS_SERVICE_URL}/users/subscribe`,
      data: {
        email: this.state.value
      },
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then((res) => { console.log(res); })
    .catch((err) => { console.log(err); });
    event.preventDefault();
  }

  render() {
    return (
      <div className="container">
        <form onSubmit={this.handleSubmit}>
          <label>
            Email:
            <input type="text" name="email" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="submit" />
        </form>
      </div>
    )
  }
}

export default SubscribeForm;

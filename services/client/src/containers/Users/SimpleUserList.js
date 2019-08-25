import React, { Component } from 'react'
// import axios from 'axios'

class SimpleUserList extends Component {
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
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-one-third">
              <br/>
              <h1 className="title is-1">Simple User List</h1>
              <hr/><br/>
              {/* new */}
              {
                this.state.simple_users.map((user) => {
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
    )
  }
}

export default SimpleUserList

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import {
  Grid,
  Table,
  TableHeaderRow
} from '@devexpress/dx-react-grid-material-ui'
import { Paper } from '@material-ui/core'


class UserTable extends Component {

  static propTypes = {
    users: PropTypes.array.isRequired
  }

  render() {
    let { users } = this.props
    users.forEach(user => {
      Object.keys(user).forEach(key => {
        if(typeof(user[key]) === "boolean") {
          user[key] = user[key].toString()
        } else if(user[key] instanceof Date) {
          user[key] = user[key].toLocaleDateString()
        }
      })
    })
    return (
      <Paper>
        <Grid
          rows={users}
          columns={[
            { name: 'id', title: 'ID' },
            { name: 'email', title: 'Email' },
            { name: 'subscribed', title: 'Subscribed' },
            { name: 'terms_and_conditions', title: 'Terms And Conditions' },
            { name: 'verified', title: 'Verified' },
            { name: 'firstname', title: 'First Name' },
            { name: 'middlename', title: 'Middle Name' },
            { name: 'lastname', title: 'Last Name' },
            { name: 'address1', title: 'Address1' },
            { name: 'address2', title: 'Address2' },
            { name: 'city', title: 'City' },
            { name: 'state', title: 'State' },
            { name: 'zipcode', title: 'Zipcode' },
            { name: 'country', title: 'Country' },
            { name: 'phone', title: 'Phone' },
            { name: 'birthday', title: 'Birthday' },
            { name: 'online', title: 'Online' },
            { name: 'last_signin', title: 'Last Signin' },
            { name: 'last_signout', title: 'Last Signout' },
            { name: 'created_at', title: 'Created At' }
          ]}>
          <h1 className="title is-1" style={{color: 'white'}}>User Table</h1>
          <Table styles="border-right: 1px solid white" />
          <TableHeaderRow />
        </Grid>
      </Paper>
    )
  }
}

export default UserTable

import React, { Component } from 'react'
import PropTypes from 'prop-types'
import {
  Grid,
  Table,
  TableHeaderRow
} from '@devexpress/dx-react-grid-material-ui'
import { Paper } from '@material-ui/core'


class SimpleUserTable extends Component {

  static propTypes = {
    simple_users: PropTypes.array.isRequired
  }

  render() {
    let { simple_users } = this.props
    simple_users.forEach(user => {
      for(let key in user){
        if(typeof(user[key]) === "boolean") {
          user[key] = user[key].toString()
        } else if(user[key] instanceof Date) {
          user[key] = user[key].toLocaleDateString()
        }
      }
    })

    return (
      <Paper>
        <Grid
          rows={simple_users}
          columns={[
            { name: 'id', title: 'ID' },
            { name: 'email', title: 'Email' },
            { name: 'subscribed', title: 'Subscribed' },
            { name: 'signed_up', title: 'Signed Up' },
            { name: 'online', title: 'Online' },
            { name: 'last_signin', title: 'Last Signin' },
            { name: 'last_signout', title: 'Last Signout' },
            { name: 'created_at', title: 'Created At' }
          ]}>
          <h1 className="title is-1" style={{color: 'white'}}>Simple User Table</h1>
          <Table styles="border-right: 1px solid white" />
          <TableHeaderRow />
        </Grid>
      </Paper>
    )
  }
}

export default SimpleUserTable

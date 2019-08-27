import React, { Component } from 'react'
import PropTypes from 'prop-types'
import {
  Grid,
  Table,
  TableHeaderRow
} from '@devexpress/dx-react-grid-material-ui'
import { withStyles } from '@material-ui/styles'
import { Paper } from '@material-ui/core'


const styles = theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
    padding: theme.spacing(3),
    justifyContent: 'center',
  },
  title: {
    display: 'flex',
    flexWrap: 'wrap',
    padding: theme.spacing(2),
    justifyContent: 'center',
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 200,
  },
  dense: {
    marginTop: 19,
  },
  button: {
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
    borderRadius: 3,
    border: 0,
    color: 'white',
    height: 50,
    padding: '0 30px',
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
  },
})

class SimpleUserTable extends Component {

  static propTypes = {
    classes: PropTypes.object.isRequired,
    simple_users: PropTypes.array.isRequired,
  }

  render() {
    let { classes, simple_users } = this.props
    simple_users.forEach(user => {
      Object.keys(user).forEach(key => {
        if(typeof(user[key]) === "boolean") {
          user[key] = user[key].toString()
        } else if(user[key] instanceof Date) {
          user[key] = user[key].toLocaleDateString()
        }
      })
    })

    return (
      <Paper
        className={classes.container}
      >
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
          <Table style="border-right: 1px solid white" />
          <TableHeaderRow />
          <Paper
            className={classes.title}
          >
            <h1 className="title is-1" style={{color: 'white'}}>
              Simple User Table
            </h1>
          </Paper>
        </Grid>
      </Paper>
    )
  }
}

export default withStyles(styles)(SimpleUserTable)

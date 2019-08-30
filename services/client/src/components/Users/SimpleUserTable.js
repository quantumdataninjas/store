import React, { Component } from 'react'
import PropTypes from 'prop-types'
import {
  Grid,
  Table,
  TableHeaderRow
} from '@devexpress/dx-react-grid-material-ui'
import { Paper, Typography, withStyles } from '@material-ui/core'


const styles = theme => ({
  container: {
    // backgroundColor: "#353535",
    display: 'flex',
    flexWrap: 'wrap',
    padding: theme.spacing(3),
    justifyContent: 'center',
  },
  titlePaper: {
    backgroundColor: "#4b4b4b",
    display: 'flex',
    flexWrap: 'wrap',
    padding: theme.spacing(2),
    justifyContent: 'center',
    // fontSize: 40,
  },
  title: {
    fontSize: 40,
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
    // simple_users: PropTypes.arrayOf(PropTypes.shape({
    //   id: PropTypes.number.isRequired,
    //   email: PropTypes.string.isRequired,
    //   subscribed: PropTypes.bool.isRequired,
    //   signed_up: PropTypes.bool.isRequired,
    //   online: PropTypes.bool.isRequired,
    //   last_signin: PropTypes.instanceOf(Date).isRequired,
    //   last_signout: PropTypes.instanceOf(Date).isRequired,
    //   created_at: PropTypes.instanceOf(Date).isRequired
    // })).isRequired,
  }

  render() {
    console.log('Simple User Table render')
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
          {/*
            * TODO:
            * make borders around each cell
            * 
            <Table style="border-right: 1px solid white" />
          */}
          <Table />
          <TableHeaderRow />
          <Paper
            className={classes.titlePaper}
          >
            {/* <h1 className="title is-1" style={{color: 'white'}}>
              Simple Users
            </h1> */}
            <Typography variant="h1" component="h2" className={classes.title}>
              Simple Users
            </Typography>
          </Paper>
        </Grid>
      </Paper>
    )
  }
}

export default withStyles(styles)(SimpleUserTable)

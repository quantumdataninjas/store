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

class UserTable extends Component {

  static propTypes = {
    // users: PropTypes.array.isRequired,
    users: PropTypes.arrayOf(PropTypes.shape({
      id: PropTypes.number.isRequired,
      simple_user_id: PropTypes.number.isRequired,
      username: PropTypes.string.isRequired,
      email: PropTypes.string.isRequired,
      subscribed: PropTypes.bool.isRequired,
      terms_and_conditions: PropTypes.bool.isRequired,
      verified: PropTypes.bool.isRequired,
      firstname: PropTypes.string.isRequired,
      middlename: PropTypes.string,
      lastname: PropTypes.string.isRequired,
      // address1: PropTypes.string.isRequired,
      // address2: PropTypes.string,
      // city: PropTypes.string.isRequired,
      // state: PropTypes.string.isRequired,
      // zipcode: PropTypes.string.isRequired,
      // country: PropTypes.string.isRequired,
      phone: PropTypes.string,
      birthday: PropTypes.instanceOf(Date).isRequired,
      online: PropTypes.bool.isRequired,
      last_signin: PropTypes.instanceOf(Date).isRequired,
      last_signout: PropTypes.instanceOf(Date).isRequired,
      created_at: PropTypes.instanceOf(Date).isRequired
    })).isRequired
  }

  render() {
    let { classes, users } = this.props
    users.forEach(user => {
      Object.keys(user).forEach(key => {
        if(typeof(user[key]) === "boolean") {
          user[key] = user[key].toString()
        } else if(user[key] instanceof Date) {
          user[key] = user[key].toLocaleDateString()
        } else if(typeof(user[key]) === "undefined") {
          user[key] = "undefined"
        }
      })
    })
    return (
      <Paper className={classes.container}>
        <Grid
          rows={users}
          columns={[
            { name: 'id', title: 'ID' },
            { name: 'simple_user_id', title: 'Simple User ID' },
            { name: 'username', title: 'Username' },
            { name: 'email', title: 'Email' },
            { name: 'subscribed', title: 'Subscribed' },
            { name: 'terms_and_conditions', title: 'Terms And Conditions' },
            { name: 'verified', title: 'Verified' },
            { name: 'firstname', title: 'First Name' },
            { name: 'middlename', title: 'Middle Name' },
            { name: 'lastname', title: 'Last Name' },
            // { name: 'address1', title: 'Address1' },
            // { name: 'address2', title: 'Address2' },
            // { name: 'city', title: 'City' },
            // { name: 'state', title: 'State' },
            // { name: 'zipcode', title: 'Zipcode' },
            // { name: 'country', title: 'Country' },
            { name: 'phone', title: 'Phone' },
            { name: 'birthday', title: 'Birthday' },
            { name: 'online', title: 'Online' },
            { name: 'last_signin', title: 'Last Signin' },
            { name: 'last_signout', title: 'Last Signout' },
            { name: 'created_at', title: 'Created At' },
            { name: 'deleted', title: 'Deleted' },
            { name: 'deleted_at', title: 'Deleted At' },
          ]}>
          <Paper
            className={classes.titlePaper}
          >
            {/* <h1 className="title is-1" style={{color: 'white'}}>
              Users
            </h1> */}
            <Typography variant="h1" component="h2" className={classes.title}>
              Users
            </Typography>
          </Paper>
          {/* <Table style={{borderRight: "white"}} /> */}
          <Table />
          <TableHeaderRow />
        </Grid>
      </Paper>
    )
  }
}

export default withStyles(styles)(UserTable)

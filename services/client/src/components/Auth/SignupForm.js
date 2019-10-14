import React, { Component } from 'react'
import PropTypes from 'prop-types'
import axios from 'axios'
import clsx from 'clsx'
import { Paper, TextField, Button, withStyles } from '@material-ui/core'
import { FormHelperText, Select , NativeSelect , InputLabel, FormControl } from '@material-ui/core'
//import FormHelperText from '@material-ui/core/FormHelperText';

// import 'date-fns';
// import Grid from '@material-ui/core/Grid';
// import DateFnsUtils from '@date-io/date-fns';
// import {
//   MuiPickersUtilsProvider,
//   KeyboardTimePicker,
//   KeyboardDatePicker,
// } from '@material-ui/pickers';

const styles = theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
    //padding: 20,
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    margin: theme.spacing(2)
  },
  form: {
    margin: theme.spacing(2),
    //marginTop: theme.spacing(10)
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
    marginTop: 20,
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
    margin: theme.spacing(1)
  },
})

export class SignupForm extends Component {

  static propTypes = {
    classes: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      firstname: '',
      //middlename: '',
      lastname: '',
      email: '',
      password: '',
      birthday: '',
      username: '',
      //phone: ''
      address:
      {
        address1: '',
        city: '',
        zipcode: '',
        state: '',
        country: ''
      }
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleAddressChange = this.handleAddressChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  handleSubmit(event) {
    //console.log(this.state.value)
    this.signup(this.state)
    event.preventDefault()
    console.log(this.state)
  }

  handleAddressChange(event) {
    const address = this.state.address
    address[event.target.name] = event.target.value
    this.setState({
      address: address
    })
    // const newState = this.state
    // newState.address[event.target.name] = event.target.value
    // this.setState(newState/)
    // this.setState({
    //   "address": {
    //     [event.target.name]: event.target.value
    //   }
    // })
  }

  signup(data) {
    axios({
      method: 'post',
      url: `${process.env.REACT_APP_USERS_SERVICE_URL}/users/auth/signup`,
      data: data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  render() {
    const { handleSubmit, handleChange, handleAddressChange } = this
    const { classes } = this.props
    return (
      <Paper className={classes.container}>
        <form className={classes.form} onSubmit={handleSubmit} autoComplete="on">
          <TextField
            required
            id="username-field"
            type="text"
            name="username"
            label="Username"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="email-field"
            type="email"
            name="email"
            label="Email"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="firstname-field"
            type="text"
            name="firstname"
            label="First Name"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <TextField
            required
            id="lastname-field"
            type="text"
            name="lastname"
            label="Last Name"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="birthday-field"
            type="date"
            name="birthday"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="password-field"
            type="password"
            name="password"
            label="Password"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="address1-field"
            type="text"
            name="address1"
            label="Address1"
            className={classes.textField}
            onChange={handleAddressChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="city-field"
            type="text"
            name="city"
            label="City"
            className={classes.textField}
            onChange={handleAddressChange}
            margin="normal"
          />
          <TextField
            required
            id="state-field"
            type="text"
            name="state"
            label="State"
            className={classes.textField}
            onChange={handleAddressChange}
            margin="normal"
          />
          <TextField
            required
            id="zipcode-field"
            type="text"
            name="zipcode"
            label="Zipcode"
            className={classes.textField}
            onChange={handleAddressChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="country-field"
            type="text"
            name="country"
            label="Country"
            className={classes.textField}
            onChange={handleAddressChange}
            margin="normal"
          />
          <br />
          <Button
            type="submit"
            className={classes.button}
          >
            Sign Up
          </Button>
          <Button
            type="submit"
            className={classes.button}
          >
            Login
          </Button>
        </form>

      </Paper>

    )
  }
}

export default withStyles(styles)(SignupForm)

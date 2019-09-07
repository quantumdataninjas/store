import React, { Component } from 'react'
import PropTypes from 'prop-types'
import axios from 'axios'
import clsx from 'clsx'
import { Paper, TextField, Button, withStyles } from '@material-ui/core'
import { Select , NativeSelect , InputLabel, FormControl } from '@material-ui/core'

const styles = theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
    // padding: 20,
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
  },
  form: {
    margin: theme.spacing(2),
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
      lastname: '',
      email: '',
      password: '',
      repassword: '',
      role: ''
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(event) {
    this.setState({email: event.target.value})
    //this.setState({
    //  [event.target.name]: event.target.value
    //})
  }

  handleSubmit(event) {
    console.log(this.state.value)
    axios({
      method: 'post',
      url: `${process.env.REACT_APP_USERS_SERVICE_URL}/users/signup`,
      data: this.state,
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
    event.preventDefault()
  }

  render() {
    const { handleSubmit, handleChange } = this
    const { classes } = this.props
    return (
      <Paper className={classes.container}>
        <form className={classes.form} onSubmit={handleSubmit} autoComplete="on">
          <TextField
            required
            id="firstname-field"
            type="firstname"
            name="firstname"
            label="FirstName"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <br />
          <TextField
            required
            id="lastname-field"
            type="lastname"
            name="lastname"
            label="LastName"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          <div>
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
          </div>
          <div>
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
          </div>
          <div>
          <TextField
            required
            id="repassword-field"
            type="repassword"
            name="repassword"
            label="Repassword"
            className={classes.textField}
            onChange={handleChange}
            margin="normal"
          />
          </div>
          <div>
          <NativeSelect
            required
            id="role-field"
            type="role"
            name="role"
            label="Role"
            className={classes.selectEmpty}
            onChange={handleChange}
            inputProps={{ 'aria-label': 'age' }}
          >
            <option value="">Role*</option>
            <option value={10}>Gamer</option>
            <option value={20}>Brand</option>
            <option value={30}>Agency</option>
            <option value={40}>Other (Specify)</option>
          </NativeSelect>
          </div>

          <Button
            type="submit"
            className={classes.button}
          >
            Sign Up
          </Button>

        </form>

      </Paper>

      // <div classsName={classes.root}>
      // <FormControl className={classes.formControl}>
      //   <InputLabel htmlFor="age-native-simple">Age</InputLabel>
      //   <Select
      //     native
      //     value={state.role}
      //     onChange={handleChange('role')}
      //     inputProps={{
      //       name: 'role',
      //       id: 'role-native-simple',
      //     }}
      //   >
      //     <option value="" />
      //     <option value={10}>Gamer</option>
      //     <option value={20}>Brand</option>
      //     <option value={30}>Agency</option>
      //     <option value={30}>Other (Specify)</option>
      //   </Select>
      // </FormControl>
      // </div>
    )
  }
}

export default withStyles(styles)(SignupForm)

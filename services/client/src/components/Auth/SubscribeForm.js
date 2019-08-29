import React, { Component } from 'react'
import PropTypes from 'prop-types'
import axios from 'axios'
import clsx from 'clsx'
import { Paper, TextField, Button, withStyles } from '@material-ui/core'


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

export class SubscribeForm extends Component {

  static propTypes = {
    classes: PropTypes.object.isRequired,
  }

  constructor() {
    super()
    this.state = {
      email: ''
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  handleSubmit(event) {
    console.log(this.state)
    axios({
      method: 'post',
      url: `${process.env.REACT_APP_USERS_SERVICE_URL}/users/subscribe`,
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
    const { email } = this.state
    const { classes } = this.props
    return (
      <Paper className={classes.container}>
        <form className={classes.form} onSubmit={handleSubmit} autoComplete="on">
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
          <Button
            type="submit"
            className={classes.button}
          >
            Subscribe
          </Button>
        </form>
      </Paper>
    )
  }
}

export default withStyles(styles)(SubscribeForm)

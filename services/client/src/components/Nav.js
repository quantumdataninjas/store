import React, { Component } from 'react'
import PropTypes from 'prop-types'
//import { makeStyles } from '@material-ui/core/styles';
import { Colors, Paper, withStyles, AppBar, Toolbar, Typography, Button, IconButton } from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';

//const useStyles = makeStyles(theme => ({
const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
});

//export default function ButtonAppBar() {
export class Nav extends Component {
  //const classes = styles();

  render() {
    //const { handleSubmit, handleChange } = this
    const { classes } = this.props
    return (
      <Paper>
        <AppBar style={{ background: 'inherit' }} position="static">
          <Toolbar>
            <IconButton edge="start" className={classes.menuButton} aria-label="menu">
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" className={classes.title}>
              News
            </Typography>
            <Button>Login</Button>
          </Toolbar>
        </AppBar>
      </Paper>
    );
  }
}

export default withStyles(styles)(Nav)

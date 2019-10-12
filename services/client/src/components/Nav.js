import React, { Component } from 'react'
import PropTypes from 'prop-types'
//import { makeStyles } from '@material-ui/core/styles';
import { Paper, withStyles, AppBar, Toolbar, Typography, Button, IconButton } from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';
import { CssBaseline, useScrollTrigger, Box, Container, Slide } from '@material-ui/core';

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

function HideOnScroll(props) {
  const { children, window } = props;
  // Note that you normally won't need to set the window ref as useScrollTrigger
  // will default to window.
  // This is only being set here because the demo is in an iframe.
  const trigger = useScrollTrigger({ target: window ? window() : undefined });

  return (
    <Slide appear={false} direction="down" in={!trigger}>
      {children}
    </Slide>
  );
}

HideOnScroll.propTypes = {
  children: PropTypes.element.isRequired,
  /**
   * Injected by the documentation to work in an iframe.
   * You won't need it on your project.
   */
  window: PropTypes.func,
};

//export default function HideAppBar(props) {
export class Nav extends Component {
  
  render(){
    const { classes } = this.props
    return (
      <Paper>
        <React.Fragment>
          <CssBaseline />
          <HideOnScroll {...this.props}>
              <AppBar style={{ background: 'inherit' }}>
                <Toolbar>
              <IconButton edge="start" className={classes.menuButton} aria-label="menu">
                <MenuIcon />
              </IconButton>
              <Typography variant="h6" className={classes.title}>
                Home
              </Typography>
              <Button>Login</Button>
              </Toolbar>
                {/* <Toolbar>
                  <Typography variant="h6">Scroll to Hide App Bar</Typography>
                </Toolbar> */}
              </AppBar>
            </HideOnScroll>
            <Toolbar />
            {/* <Container>
              <Box my={2}>
                {[...new Array(12)]
                  .map(
                    () => `Cras mattis consectetur purus sit amet fermentum.
      Cras justo odio, dapibus ac facilisis in, egestas eget quam.
      Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
      Praesent commodo cursus magna, vel scelerisque nisl consectetur et.`,
                  )
                  .join('\n')}
              </Box>
            </Container> */}
        </React.Fragment>
      </Paper>
    );
  }
}


//export default function ButtonAppBar() {
// export class Nav extends Component {
//   //const classes = styles();

//   render() {
//     //const { handleSubmit, handleChange } = this
//     const { classes } = this.props
//     return (
//       <Paper>
//         <AppBar style={{ background: 'inherit' }} position="static">
//           <Toolbar>
//             <IconButton edge="start" className={classes.menuButton} aria-label="menu">
//               <MenuIcon />
//             </IconButton>
//             <Typography variant="h6" className={classes.title}>
//               Home
//             </Typography>
//             <Button>Login</Button>
//           </Toolbar>
//         </AppBar>
//       </Paper>
//     );
//   }
// }

export default withStyles(styles)(Nav)

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Grid,
  Table,
  TableHeaderRow
} from '@devexpress/dx-react-grid-material-ui';
import { Paper } from '@material-ui/core';


class SimpleUserGrid extends Component {

  static propTypes = {
    simple_users: PropTypes.array.isRequired
  };

  render() {
    const { simple_users } = this.props;
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
        ]}>
        <Table />
        <TableHeaderRow />
        <section className="section">
          <div className="container">
            <div className="columns">
            <div className="column is-one-third">
            <br/>
            <h1 className="title is-1">Simple User Table</h1>
            <hr/><br/>
            {/* new */}
            {
              simple_users.map(simple_user =>
                <h4
                key={simple_user.id}
                className="box title is-4"
                >{ simple_user.email }
                </h4>
              )
            }
            </div>
            </div>
          </div>
        </section>
      </Grid>
      </Paper>
    );
  };
}

export default SimpleUserGrid;

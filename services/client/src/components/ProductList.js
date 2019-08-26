import React, { Component } from 'react'
import PropTypes from 'prop-types'


class ProductList extends Component {

  static propTypes = {
    children: PropTypes.node,
    title: PropTypes.string.isRequired
  }

  render() {
    return (
      <div>
        <h3>{this.props.title}</h3>
        <div>{this.props.children}</div>
      </div>
    )
  }
}

export default ProductList

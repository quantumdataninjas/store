import React, { Component } from 'react'
import PropTypes from 'prop-types'


class ProductList extends Component {

  static propTypes = {
    children: PropTypes.node,
    title: PropTypes.string.isRequired
  }

  render() {
    const { title, children } = this.props
    return (
      <div>
        <h3>{title}</h3>
        <div>{children}</div>
      </div>
    )
  }
}

export default ProductList

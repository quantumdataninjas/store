import React, { Component } from 'react'
import PropTypes from 'prop-types'

class Product extends Component {
  static propTypes = {
    price: PropTypes.number,
    quantity: PropTypes.number,
    title: PropTypes.string
  }

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
        {this.props.title} - &#36;{this.props.price}{this.props.quantity ? ` x ${this.props.quantity}` : null}
      </div>
    )
  }
}

export default Product

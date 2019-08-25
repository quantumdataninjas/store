import React, { Component } from 'react'
import PropTypes from 'prop-types'
import Product from './Product'

class Cart extends Component {
  static propTypes = {
    products: PropTypes.array,
    total: PropTypes.string,
    onCheckoutClicked: PropTypes.func
  }

  constructor(props) {
    super(props);
  }

  hasProducts() {
    return this.props.products.length > 0
  }

  productList() {
    return this.hasProducts() ? (
      this.props.products.map(product =>
        <Product
          title={product.title}
          price={product.price}
          quantity={product.quantity}
          key={product.id}
        />
      )
    ) : (
      <em>Please add some products to cart.</em>
    )
  }

  render() {
    return (
      <div>
        <h3>Your Cart</h3>
        <div>{this.productList()}</div>
        <p>Total: &#36;{this.props.total}</p>
        <button onClick={this.props.onCheckoutClicked}
          disabled={this.hasProducts() ? '' : 'disabled'}>
          Checkout
        </button>
      </div>
    )
  }
}

export default Cart

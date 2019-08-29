import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { checkout } from 'actions'
import { getTotal, getCartProducts } from 'reducers'
import Cart from 'components/Cart'


class CartContainer extends Component {
  static propTypes = {
    products: PropTypes.arrayOf(PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      quantity: PropTypes.number.isRequired
    })).isRequired,
    total: PropTypes.string,
    checkout: PropTypes.func.isRequired
  }

  render() {
    const { products, total } = this.props
    return (
      <Cart
        products={products}
        total={total}
        onCheckoutClicked={() => checkout(products)} />
    )
  }
}

const mapStateToProps = (state) => ({
  products: getCartProducts(state),
  total: getTotal(state)
})

const mapDispatchToProps = dispatch => ({
  checkout: dispatch(checkout)
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CartContainer)

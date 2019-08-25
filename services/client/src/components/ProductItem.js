import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Product from './Product';


class ProductItem extends Component {

  static propTypes = {
    product: PropTypes.shape({
      title: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      inventory: PropTypes.number.isRequired
    }).isRequired,
    onAddToCartClicked: PropTypes.func.isRequired
  };

  render() {
    return (
      <div style={{ marginBottom: 20 }}>
        <Product
          title={this.props.product.title}
          price={this.props.product.price}
          quantity={this.props.product.inventory} />
        <button
          onClick={this.props.onAddToCartClicked}
          disabled={this.props.product.inventory > 0 ? '' : 'disabled'}>
          {this.props.product.inventory > 0 ? 'Add to cart' : 'Sold Out'}
        </button>
      </div>
    );
  };
}

export default ProductItem;

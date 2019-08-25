import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { addToCart } from 'actions';
import { getVisibleProducts } from 'reducers/products';
import ProductItem from 'components/ProductItem';
import ProductList from 'components/ProductList';


class ProductsContainer extends Component {

  static propTypes = {
    products: PropTypes.arrayOf(PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      inventory: PropTypes.number.isRequired
    })).isRequired,
    addToCart: PropTypes.func.isRequired
  };

  render() {
    return (
      <ProductList title="Products">
        {this.props.products.map(product =>
          <ProductItem
            key={product.id}
            product={product}
            onAddToCartClicked={() => addToCart(product.id)} />
        )}
      </ProductList>
    );
  };
}

const mapStateToProps = state => ({
  products: getVisibleProducts(state.products)
});

const mapDispatchToProps = dispatch => ({
  addToCart: dispatch(addToCart)
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
  // { addToCart }
)(ProductsContainer);

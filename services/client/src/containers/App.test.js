import React from 'react'
// import ReactDOM from 'react-dom'
// import { Provider } from 'react-redux'
import thunk from 'redux-thunk'
import promise from 'redux-promise'
import { createLogger } from 'redux-logger'
import { App } from './App'
// import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'
import configureStore from 'redux-mock-store'


const logger = createLogger()
const middlewares = [thunk, promise, logger]
const mockStore = configureStore(middlewares)

describe('App Component tests', () => {
  const initialState = {
    simple_users: [],
    users: [],
    cart: {},
    products: {}
  }
  const store = mockStore(initialState)

  it('should shallow render App component', () => {
    const wrapper = shallow(<App store={store} />)
    const app = wrapper.find('.App')
    expect(app.length).toBe(1)
  })

  /**
   * TODO
   * wait for stackoverflow response
   * 
  it('should render App component', () => {
    const tree = renderer.create(<App store={store} />)
    expect(tree.toJSON()).toMatchSnapshot()
  })
  
  it('renders without crashing', () => {
    const div = document.createElement('div')
    ReactDOM.render(<App store={store} />, div)
    ReactDOM.unmountComponentAtNode(div)
  })
   */

})


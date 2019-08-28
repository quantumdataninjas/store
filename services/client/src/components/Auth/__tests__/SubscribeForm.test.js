import React from 'react'
import { mount, shallow } from 'enzyme'
import renderer from 'react-test-renderer'
import SubscribeForm from '../SubscribeForm'
import { TextField, Button } from '@material-ui/core'



describe('SubscribeForm Component', () => {

    it('renders', () => {
        const wrapper = mount(<SubscribeForm />)
        const form = wrapper.find('form')
        expect(form.find('input')).toHaveLength(1)
        expect(form.find(TextField)).toHaveLength(1)
        expect(form.find(TextField).get(0).props.name).toBe('email')
        expect(form.find(Button).get(0).props.type).toBe('submit')
    })

    it('renders a snapshot', () => {
        const tree = renderer.create(<SubscribeForm />)
        expect(tree).toMatchSnapshot()
    })
})
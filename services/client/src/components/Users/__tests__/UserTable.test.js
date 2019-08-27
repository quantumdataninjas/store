import React from 'react'
import { mount, shallow } from 'enzyme'
import renderer from 'react-test-renderer'
import UserTable from '../UserTable'


const users = [
    {
        "id": "1",
        "email": "user@test.org",
        "subscribed": "true",
        "terms_and_conditions": "true",
        "verified": "false",
        "firstname": "first",
        "middlename": "",
        "lastname": "last",
        "address1": "1523 John St.",
        "address2": "",
        "city": "Fort Lee",
        "state": "NJ",
        "zipcode": "07024",
        "country": "United States",
        "phone": "",
        "birthday": "1/1/1990",
        "online": "true",
        "last_signin": "8/26/2019",
        "last_signout": "8/26/2019",
        "created_at": "8/26/2019"
    },
    {
        "id": "2",
        "email": "user2@test.org",
        "subscribed": "true",
        "terms_and_conditions": "true",
        "verified": "false",
        "firstname": "first",
        "middlename": "",
        "lastname": "last",
        "address1": "1523 John St.",
        "address2": "",
        "city": "Fort Lee",
        "state": "NJ",
        "zipcode": "07024",
        "country": "United States",
        "phone": "",
        "birthday": "1/1/1990",
        "online": "true",
        "last_signin": "8/26/2019",
        "last_signout": "8/26/2019",
        "created_at": "8/26/2019"
    },
]

const cols = [
    { header: "ID", name: "id" },
    { header: "Email", name: "email" },
    { header: "Subscribed", name: "subscribed" },
    { header: "Terms And Conditions", name: "terms_and_conditions" },
    { header: "Verified", name: "verified" },
    { header: "First Name", name: "firstname" },
    { header: "Middle Name", name: "middlename" },
    { header: "Last Name", name: "lastname" },
    { header: "Address1", name: "address1" },
    { header: "Address2", name: "address2" },
    { header: "City", name: "city" },
    { header: "State", name: "state" },
    { header: "Zipcode", name: "zipcode" },
    { header: "Country", name: "country" },
    { header: "Phone", name: "phone" },
    { header: "Birthday", name: "birthday" },
    { header: "Online", name: "online" },
    { header: "Last Signin", name: "last_signin" },
    { header: "Last Signout", name: "last_signout" },
    { header: "Created At", name: "created_at" },
]

describe('UserTable Component', () => {

    it('renders empty message as table cell if there is no data', () => {
        const wrapper = mount(<UserTable users={[]}/>)
        const table = wrapper.find('table');
        expect(table).toHaveLength(1);
        const thead = table.find('thead');
        expect(thead).toHaveLength(1);
        const headers = thead.find('th');
        expect(headers).toHaveLength(cols.length);
        headers.forEach((th, idx) => {
            expect(th.text()).toEqual(cols[idx].header);
        });
        const tbody = table.find('tbody');
        expect(tbody).toHaveLength(1);
        const row = tbody.find('tr');
        expect(row).toHaveLength(1);
        const cell = row.find('td');
        expect(cell).toHaveLength(1);
        expect(cell.prop('colSpan')).toEqual(cols.length);
        expect(cell.text()).toEqual('No data');
    })

    it('renders properly', () => {
        const wrapper = mount(<UserTable users={users}/>)
        const table = wrapper.find('table')
        expect(table).toHaveLength(1)
        const thead = table.find('thead')
        expect(thead).toHaveLength(1)
        const headers = thead.find('th')
        expect(headers).toHaveLength(cols.length)
        headers.forEach((th, i) => {
            expect(th.text()).toEqual(cols[i].header)
        })
        const tbody = table.find('tbody')
        expect(tbody).toHaveLength(1)
        const rows = tbody.find('tr')
        expect(rows).toHaveLength(users.length)
        rows.forEach((tr, i) => {
            const cells = tr.find('td')
            expect(cells).toHaveLength(cols.length)
            cells.forEach((cell, j) => {
                expect(cell.text()).toEqual(users[i][cols[j].name])
            })
        })
    })

    it('renders a snapshot', () => {
        const tree = renderer.create(<UserTable users={users} />)
        expect(tree).toMatchSnapshot()
    })
})
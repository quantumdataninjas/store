import React from 'react'
import { mount, shallow } from 'enzyme'
import renderer from 'react-test-renderer'
import { Grid } from '@devexpress/dx-react-grid-material-ui'
import SimpleUserTable from '../SimpleUserTable'


const simple_users = [
    {
        "id": "1",
        "email": "user@test.org",
        "subscribed": "true",
        "signed_up": "false",
        "online": "true",
        "last_signin": "8/26/2019",
        "last_signout": "8/26/2019",
        "created_at": "8/26/2019"
    },
    {
        "id": "2",
        "email": "user2@test.org",
        "subscribed": "true",
        "signed_up": "false",
        "online": "true",
        "last_signin": "8/26/2019",
        "last_signout": "8/26/2019",
        "created_at": "8/26/2019"
    },
    {
        "id": "3",
        "email": "test@test.org",
        "subscribed": "true",
        "signed_up": "false",
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
    { header: "Signed Up", name: "signed_up" },
    { header: "Online", name: "online" },
    { header: "Last Signin", name: "last_signin" },
    { header: "Last Signout", name: "last_signout" },
    { header: "Created At", name: "created_at" },
]

describe('SimpleUserTable Component', () => {

    it('renders empty message as table cell if there is no data', () => {
        const wrapper = mount(<SimpleUserTable simple_users={[]}/>)
        const grid = wrapper.find(Grid);
        expect(grid).toHaveLength(1);
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

    it('renders', () => {
        //   const wrapper = shallow(<SimpleUserTable simple_users={simple_users}/>)
        const wrapper = mount(<SimpleUserTable simple_users={simple_users}/>)
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
        expect(rows).toHaveLength(simple_users.length)
        rows.forEach((tr, i) => {
            const cells = tr.find('td')
            expect(cells).toHaveLength(cols.length)
            cells.forEach((cell, j) => {
                expect(cell.text()).toEqual(simple_users[i][cols[j].name])
            })
        })
    })

    it('renders a snapshot', () => {
        const tree = renderer.create(<SimpleUserTable simple_users={simple_users} />)
        expect(tree).toMatchSnapshot()
    })
})
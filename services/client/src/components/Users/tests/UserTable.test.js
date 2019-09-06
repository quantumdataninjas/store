import { cloneDeep } from 'lodash'
import React from 'react'
import { mount, shallow } from 'enzyme'
import renderer from 'react-test-renderer'
import UserTable from '../UserTable'


const users = [
  {
    "id": 1,
    "simple_users_id": 1,
    "username": "user",
    "email": "user@test.org",
    "subscribed": true,
    "terms_and_conditions": true,
    "verified": false,
    "firstname": "first",
    "middlename": "",
    "lastname": "last",
    // "address1": "1523 John St.",
    // "address2": "",
    // "city": "Fort Lee",
    // "state": "NJ",
    // "zipcode": "07024",
    // "country": "United States",
    "phone": "",
    "birthday": new Date("1/1/1990"),
    "online": true,
    "last_signin": new Date("8/26/2019"),
    "last_signout": new Date("8/26/2019"),
    "created_at": new Date("8/26/2019"),
    "deleted": false,
    "deleted_at": undefined
  },
  {
    "id": 2,
    "simple_users_id": 2,
    "username": "user2",
    "email": "user2@test.org",
    "subscribed": true,
    "terms_and_conditions": true,
    "verified": false,
    "firstname": "first",
    "middlename": "",
    "lastname": "last",
    // "address1": "1523 John St.",
    // "address2": "",
    // "city": "Fort Lee",
    // "state": "NJ",
    // "zipcode": "07024",
    // "country": "United States",
    "phone": "",
    "birthday": new Date("1/1/1990"),
    "online": true,
    "last_signin": new Date("8/26/2019"),
    "last_signout": new Date("8/26/2019"),
    "created_at": new Date("8/26/2019"),
    "deleted": false,
    "deleted_at": undefined
  },
]

const cols = [
  { header: "ID", name: "id" },
  { header: "Simple Users ID", name: "simple_users_id" },
  { header: "Username", name: "username" },
  { header: "Email", name: "email" },
  { header: "Subscribed", name: "subscribed" },
  { header: "Terms And Conditions", name: "terms_and_conditions" },
  { header: "Verified", name: "verified" },
  { header: "First Name", name: "firstname" },
  { header: "Middle Name", name: "middlename" },
  { header: "Last Name", name: "lastname" },
  // { header: "Address1", name: "address1" },
  // { header: "Address2", name: "address2" },
  // { header: "City", name: "city" },
  // { header: "State", name: "state" },
  // { header: "Zipcode", name: "zipcode" },
  // { header: "Country", name: "country" },
  { header: "Phone", name: "phone" },
  { header: "Birthday", name: "birthday" },
  { header: "Online", name: "online" },
  { header: "Last Signin", name: "last_signin" },
  { header: "Last Signout", name: "last_signout" },
  { header: "Created At", name: "created_at" },
  { header: "Deleted", name: "deleted" },
  { header: "Deleted At", name: "deleted_at" },
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
    const users_clone = cloneDeep(users)
    const wrapper = mount(<UserTable users={users_clone}/>)
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
        const value = users[i][cols[j].name]
        if(value instanceof Date) {
          expect(cell.text()).toEqual(value.toLocaleDateString())
        } else if(typeof(value) === "undefined") {
          expect(cell.text()).toEqual("undefined")
        } else {
          expect(cell.text()).toEqual(value.toString())
        }
      })
    })
  })

  it('renders a snapshot', () => {
    const users_clone = cloneDeep(users)
    const tree = renderer.create(<UserTable users={users_clone} />)
    expect(tree).toMatchSnapshot()
  })
})
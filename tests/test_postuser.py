import pytest
from utils.apis import APIs
import uuid

@pytest.fixture(scope='module')
def apis():
    return APIs()

# test case 02 - create (post) a user

def test_post_user_validation(apis):
    user_data ={
        "name": "test user1",
        "username":"test QA1",
        "email":"test@gmail.com"
    }

    response = apis.post('users', user_data)

    # display the response
    print(response.json())

    # validate the response code if passed
    assert response.status_code == 201

    # output returned response code and flag as passed
    str_code = str(response.status_code)
    print("****Code " + str_code +" is passed!****")

    # ensure that the data key (username) is added in the database
    assert response.json()['name'] =='test user1'
    print("****User ID/Name " + str(response.json()['id']) + " and " + response.json()['username'] +" is added!****")

    

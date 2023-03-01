import pytest
import requests
from data.db_session import create_session, global_init
from data.users import User

base_url = 'http://127.0.0.1:5000'


@pytest.fixture
def db_init():
    global_init('db/blogs.db')


def test_get_one_user(db_init):
    response = requests.get(base_url + '/api/v2/users/1')
    sess = create_session()
    user = sess.query(User).get(1)
    assert response.json() == {'user': user.to_dict(rules=('-jobs',))}


def test_get_wrong_user(db_init):
    user_id = 999
    response = requests.get(base_url + f'/api/v2/users/{user_id}')
    assert response.json() == {'message': f'User {user_id} not found'}


def test_get_all_user(db_init):
    response = requests.get(base_url + '/api/v2/users/999')
    session = create_session()
    users = session.query(User).all()
    return response.json() == {'users': [item.to_dict(only=('id', 'name', 'surname', 'email', 'jobs.id', 'jobs.job'))
                                         for item in users]}

import pytest
import requests
from data.jobs import Jobs
from data.db_session import create_session, global_init
import json

base_url = 'http://127.0.0.1:5000'


@pytest.fixture
def db_init():
    global_init('db/blogs.db')


def test_post_jobs(db_init):
    data = {'team_leader': 1, 'job': 'описание', 'work_size': 3}
    response = requests.post(base_url + '/api/jobs', json=data)
    assert response.json() == {'success': 'OK'}


def test_post_empty(db_init):
    response = requests.get(base_url + '/api/jobs/', json={})
    assert response.json() == {'error': 'Empty request'}


def test_post_bad_job(db_init):
    data = {'team_leader': 1, 'job': 'описание'}
    response = requests.get(base_url + '/api/jobs/', json=data)
    assert response.json() == {'error': 'Bad request'}

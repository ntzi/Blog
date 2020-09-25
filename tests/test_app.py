import os
import tempfile
import pytest
import sys
sys.path.insert(0, '../blog')

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    return app.test_client()


def login(client, password):
    return client.post('/login', data=dict(
        password=password
    ), follow_redirects=True)


def logout(client):
    client.get('/logout', follow_redirects=True)
    return client.post('/logout', follow_redirects=True)


def test_login_logout(client):
    """Make sure login and logout works."""

    rv = login(client, 'secret')
    assert b'You are now logged in.' in rv.data

    rv = logout(client)
    assert b'You are now logged out.' in rv.data

    rv = login(client, 'secret' + 'x')
    assert b'Incorrect password.' in rv.data

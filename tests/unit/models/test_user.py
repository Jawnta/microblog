"""
Contains tests for app.models.User class
"""
# pylint: disable=redefined-outer-name,unused-argument
# from unittest import mock
import pytest
from app.models import User

@pytest.fixture
def user1():
    """
    User object
    """
    return User(
        username='john',
        email='john@example.com',
        about_me="Hello",
    )


def test_new_user(user1):
    """
    Test that user object contain correct values
    """
    assert user1.email == 'john@example.com'
    assert user1.username == "john"
    assert user1.about_me == 'Hello'
    assert str(user1) == "<User john, john@example.com>"

def test_password_hashing(test_app, user1):
    """
    Test setting password for user
    """
    user1.set_password('cat')
    assert user1.check_password('dog') is False
    assert user1.check_password('cat') is True

def test_avatar(test_app, user1):
    """
    Test creation of Gravatar URL
    """
    import hashlib

    email_hash = hashlib.sha256(user1.email.lower().encode('utf-8')).hexdigest()
    expected_url = f'https://www.gravatar.com/avatar/{email_hash}?d=retro&s=128'

    assert user1.avatar(128) == expected_url


import pytest
from exercise_three import verify_email


def test_verify_email_when_email_empty():
    with pytest.raises(ValueError, match='Invalid email'):
        verify_email('')


def test_verify_email_when_username_invalid():
    with pytest.raises(ValueError, match='Invalid username'):
        verify_email('1-username@email.com')


def test_verify_email_when_username_invalid_two():
    with pytest.raises(ValueError, match='Invalid username'):
        verify_email('username*@email.com')


def test_verify_email_when_website_invalid():
    with pytest.raises(ValueError, match='Invalid website'):
        verify_email('username@*email.com')


def test_verify_email_when_extension_invalid():
    with pytest.raises(ValueError, match='Invalid extension'):
        verify_email('username@email.comm')


def test_verify_email_returns_valid_email():
    assert verify_email('username@website.com') == 'Valid email'

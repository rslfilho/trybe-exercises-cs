import pytest
from exercise_four import valid_emails


def test_valid_emails_returns_empty_array_when_receives_an_empty_array():
    assert valid_emails([]) == []


@pytest.fixture
def emails():
    return ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"]


def test_valid_emails_returns_two_emails_when_one_is_invalid(emails):
    assert len(valid_emails(emails)) == 2


def test_valid_emails_not_contains_the_invalid_email(emails):
    assert 'errad#@dominio.com' not in valid_emails(emails)


def test_valid_emails_contains_the_valid_emails(emails):
    assert 'nome@dominio.com' in valid_emails(emails)
    assert 'outro@dominio.com' in valid_emails(emails)

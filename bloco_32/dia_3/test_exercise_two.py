import pytest
from exercise_two import word_to_phone_number


def test_word_to_phone_number_when_no_parameters():
    with pytest.raises(ValueError, match='Invalid parameter'):
        word_to_phone_number('')


def test_word_to_phone_number_when_parameter_too_long():
    with pytest.raises(ValueError, match='Invalid parameter'):
        word_to_phone_number('SDFLKJ-DKJFK-DKLJFK-1-LKDFJLK-JFDS')


def test_word_to_phone_number_when_has_invalid_letters():
    with pytest.raises(ValueError, match='Invalid letter'):
        word_to_phone_number('1-HOME-SWEET_HOME')


def test_word_to_phone_number_when_rceives_correctly():
    assert word_to_phone_number('1-HOME-SWEET-HOME') == '1-4663-79338-4663'


def test_word_to_phone_number_when_rceives_correctly_again():
    assert word_to_phone_number('MY-MISERABLE-JOB') == '69-647372253-562'

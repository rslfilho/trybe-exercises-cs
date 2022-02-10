from exercise_one import fizz_buzz


def test_fizz_buzz_when_receive_2():
    assert fizz_buzz(2) == [1, 2]


def test_fizz_buzz_when_receive_3():
    assert fizz_buzz(3) == [1, 2, 'Fizz']


def test_fizz_buzz_when_receive_5():
    assert fizz_buzz(5) == [1, 2, 'Fizz', 4, 'Buzz']


def test_fizz_buzz_when_receive_7():
    assert fizz_buzz(7) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]

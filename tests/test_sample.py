def test_basic_math():
    assert 1 + 1 == 2


def test_string_check():
    name = "jenkins"
    assert name.upper() == "JENKINS"


def test_list_contains_value():
    numbers = [1, 2, 3, 4]
    assert 3 in numbers

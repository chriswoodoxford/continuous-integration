import ci_course


def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"


def test_minimum():
    """
    Test the function `minimum` in functionality.py
    """
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3

def test_minimum_with_strings():
    """
    Test the function `minimum` in functionality.py with strings, which should not return anything if solely strings are passed in
    """
    assert(ci_course.minimum("apple", "banana") is None)

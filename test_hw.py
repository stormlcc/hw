# content of test_sample.py
"""Execute test"""
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

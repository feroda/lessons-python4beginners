import pytest

from hello_who_3 import compose_hello


def test_hello():
    msg = compose_hello("students", force=True)
    assert msg == "Hello students!"


def test_hello_to_not_string():
    with pytest.raises(TypeError):
        compose_hello(1)


def test_hello_to_not_string_forced():
    msg = compose_hello(1, force=True)
    assert msg == "Hello 1!"

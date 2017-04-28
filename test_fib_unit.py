import pytest
from fib import fib


def test_fib_0_returns_0():
    assert fib(0) == 0

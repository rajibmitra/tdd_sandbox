import pytest
from fib import fib


def test_fib_0_returns_0():
    assert fib(0) == 0


def test_fib_1_returns_1():
    assert fib(1) == 1


def test_fib_2_returns_1():
    assert fib(2) == 1


def test_fib_6_returns_8():
    assert fib(6) == 8

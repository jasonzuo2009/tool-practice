import pytest


@pytest.fixture
def fees():
    return [39, 89, 169]


def add(a, b):
    return a + b

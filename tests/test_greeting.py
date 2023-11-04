import pytest

from poetry_dummy_greeting.greeting import DummyClass

VALID_GREETING = "Hello Dummy!!"
INVALID_GREETING = "Hello Gummy!!"

# see https://docs.pytest.org/en/6.2.x/fixture.html#
@pytest.fixture
def greeting():
    return DummyClass()

def test_valid_greeting(greeting):
    assert greeting.validateGreeting(VALID_GREETING) == True

def test_invalid_greeting(greeting):
    assert greeting.validateGreeting(INVALID_GREETING) == False
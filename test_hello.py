import pytest

from hello import Hello

def test_task_hello():
    assert Hello().task_hello() == "hello!"
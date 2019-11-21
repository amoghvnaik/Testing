import pytest
from python_exercises import multiply_list


def test_multiply_five():
    assert multiply_list.product([5,5])==25

def test_multiply_zero():
    assert multiply_list.product([0,0])==0

import pytest
from python_exercises import anti_vowel


def test_multiply_hi():
    assert anti_vowel.anti_vowel("hello")=="hll"

def test_multiply_goodbye():
    assert anti_vowel.anti_vowel("goodbye")=="gdby"

"""Tests for the Calculator module."""

from calculator import add, sub

def test_add():
    '''Test that the addition of two numbers works correctly.'''
    assert add(2, 2) == 4

def test_sub():
    '''Test that the subtraction of two numbers works correctly.'''
    assert sub(2, 2) == 0

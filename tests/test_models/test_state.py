#!/usr/bin/python3
"""Unittest for class TestState"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """
    def test_attributes(self):
        """Test that State has the expected attributes."""
        state = State()

        self.assertTrue(hasattr(state, 'name'))

        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for class TestCity"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """
    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_state_id_attribute(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_state_id_assignment(self):
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_name_attribute(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_name_assignment(self):
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_to_dict(self):
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        expected_dict = {
            'id': city.id,
            'created_at': city.created_at.isoformat(),
            'updated_at': city.updated_at.isoformat(),
            '__class__': 'City',
            'state_id': 'CA',
            'name': 'San Francisco'
        }
        self.assertEqual(city.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()

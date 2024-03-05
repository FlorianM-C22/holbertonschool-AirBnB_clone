#!/usr/bin/python3
"""Unittest for class BaseModel"""
import unittest
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """Set up method that runs before each test case"""
        self.my_model = BaseModel()

    def tearDown(self):
        """Teardown method that runs after each test case"""
        del self.my_model

    def test_init_with_arguments(self):
        """Test the __init__ method with valid arguments."""
        my_model = BaseModel(id='123', created_at='2022-01-01T00:00:00',
                             updated_at='2022-01-01T00:00:00')
        self.assertEqual(my_model.id, '123')
        self.assertEqual(my_model.created_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))
        self.assertEqual(my_model.updated_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))

    def test_str_empty_model(self):
        """Test the __str__ method with an empty model."""
        empty_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(empty_model.id,
                                                    empty_model.__dict__)
        self.assertEqual(str(empty_model), expected_str)

    def test_save_without_changes(self):
        """Test the save method without changes."""
        old_updated_at = self.my_model.updated_at
        time.sleep(0.001)  # Ensure the time has changed
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict_with_additional_attributes(self):
        """Test the to_dict method with additional attributes."""
        self.my_model.name = 'John'
        self.my_model.age = 25
        expected_dict = {
            'id': self.my_model.id,
            'created_at': self.my_model.created_at.isoformat(),
            'updated_at': self.my_model.updated_at.isoformat(),
            '__class__': 'BaseModel',
            'name': 'John',
            'age': 25
        }
        self.assertEqual(self.my_model.to_dict(), expected_dict)

    def test_init_with_invalid_id(self):
        """Test the __init__ method with an invalid id."""
        with self.assertRaises(TypeError):
            BaseModel(id=123)

    def test_str_with_missing_id(self):
        """Test the __str__ method with a missing id."""
        del self.my_model.id
        with self.assertRaises(AttributeError):
            str(self.my_model)

    def test_save_with_invalid_updated_at(self):
        """Test the save method with an invalid updated_at."""
        with self.assertRaises(ValueError):
            self.my_model.updated_at = '2022-01-01'
            self.my_model.save()

    def test_to_dict_with_reserved_attribute(self):
        """Test the to_dict method with a reserved attribute."""
        with self.assertRaises(TypeError):
            self.my_model.__class__ = 'InvalidClass'
            self.my_model.to_dict()

    def test_init_without_arguments(self):
        """Test the __init__ method without arguments."""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_to_dict_without_arguments(self):
        """Test the to_dict method without arguments."""
        expected_dict = {
            'id': self.my_model.id,
            'created_at': self.my_model.created_at.isoformat(),
            'updated_at': self.my_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.my_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()

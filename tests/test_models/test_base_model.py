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
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        time.sleep(0.001)  # Ensure the time has changed
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_with_additional_attributes(self):
        """Test the to_dict method with additional attributes."""
        my_model = BaseModel()
        my_model.name = 'John'
        my_model.age = 25
        expected_dict = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            '__class__': 'BaseModel',
            'name': 'John',
            'age': 25
        }
        self.assertEqual(my_model.to_dict(), expected_dict)

    def test_init_with_invalid_id(self):
        """Test the __init__ method with an invalid id."""
        with self.assertRaises(TypeError):
            BaseModel(id=123)

    def test_str_with_missing_id(self):
        """Test the __str__ method with a missing id."""
        my_model = BaseModel()
        del my_model.id
        with self.assertRaises(AttributeError):
            str(my_model)

    def test_save_with_invalid_updated_at(self):
        """Test the save method with an invalid updated_at."""
        my_model = BaseModel()
        my_model.updated_at = '2022-01-01'
        with self.assertRaises(ValueError):
            my_model.save()

    def test_to_dict_with_reserved_attribute(self):
        """Test the to_dict method with a reserved attribute."""
        my_model = BaseModel()
        my_model.__class__ = 'InvalidClass'
        with self.assertRaises(TypeError):
            my_model.to_dict()

    def test_new_attribute(self):
        """Test adding a new attribute to the model."""
        my_model = BaseModel()
        my_model.new_attribute = 'new value'
        self.assertEqual(my_model.new_attribute, 'new value')

    def test_updated_at_after_save(self):
        """Test the updated_at attribute after calling save."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_created_at(self):
        """Test the created_at attribute."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_id_generation(self):
        """Test the generation of unique IDs."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for base_model.py"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                    self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save(self):
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        expected_dict = {
            'id': self.my_model.id,
            'created_at': self.my_model.created_at.isoformat(),
            'updated_at': self.my_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.my_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()

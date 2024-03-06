#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUp(self):
        """Set up test environment"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.base_model.save()

    @classmethod
    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the 'all' method of the storage object."""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIn(f"{self.base_model.__class__.__name__}.\
                    {self.base_model.id}", all_objs)

    def test_new(self):
        """Test the 'new' method of the storage object."""
        storage = FileStorage()
        new_model = BaseModel()
        storage.new(new_model)
        all_objs = storage.all()
        self.assertIn(f"{new_model.__class__.__name__}.{new_model.id}",
                      all_objs)

    def test_save(self):
        """Test case for 'save' method"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test case for 'reload' method"""
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        self.assertIn(f"{self.base_model.__class__.__name__}.\
                    {self.base_model.id}", all_objs)


if __name__ == '__main__':
    unittest.main()

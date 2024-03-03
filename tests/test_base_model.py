import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_with_arguments(self):
        my_model = BaseModel(id='123', created_at='2022-01-01T00:00:00',
                             updated_at='2022-01-01T00:00:00')
        self.assertEqual(my_model.id, '123')
        self.assertEqual(my_model.created_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))
        self.assertEqual(my_model.updated_at,
                         datetime.fromisoformat('2022-01-01T00:00:00'))

    def test_str_empty_model(self):
        empty_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(empty_model.id,
                                                    empty_model.__dict__)
        self.assertEqual(str(empty_model), expected_str)

    def test_save_without_changes(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_with_additional_attributes(self):
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
        with self.assertRaises(TypeError):
            BaseModel(id=123)

    def test_str_with_missing_id(self):
        my_model = BaseModel()
        my_model.__dict__.pop('id', None)
        expected_str = "[BaseModel] ({}) {}".format('missing',
                                                    my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_with_invalid_updated_at(self):
        my_model = BaseModel()
        my_model.updated_at = '2022-01-01'
        with self.assertRaises(ValueError):
            my_model.save()

    def test_to_dict_with_reserved_attribute(self):
        my_model = BaseModel()
        my_model.__class__ = 'InvalidClass'
        expected_dict = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(my_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()

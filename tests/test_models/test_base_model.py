#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.base_model import Base
import unittest
from datetime import datetime
from uuid import UUID
import json
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
        'basemodel test not supported')

class test_basemodel(unittest.TestCase):
    """base mode class test"""

    def __init__(self, *args, **kwargs):
        """init basemodel """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """set up method of the test class """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
    def test_init(self):
        """Tests the initialization"""
        instance = self.value()
        self.assertIsInstance(instance, BaseModel)
    
        if instance.__class__ is not BaseModel:
            self.assertIsInstance(instance, Base)
        else:
            self.assertNotIsInstance(instance, Base)

    def test_default(self):
        """ default testing of basemodel """
        instace = self.value()
        self.assertEqual(type(instace), self.value)

    def test_kwargs(self):
        """kwargs testing of basemodel"""
        instace = self.value()
        copy = instace.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is instace)

    def test_kwargs_int(self):
        """ kwargs_int testing of basemodel """
        instace = self.value()
        copy = instace.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        instace = self.value()
        instace.save()
        key = self.name + "." + instace.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], instace.to_dict())

    def test_str(self):
        """Testing str methond """
        instace = self.value()
        self.assertEqual(str(instace), '[{}] ({}) {}'.format(self.name, instace.id,
            instace.__dict__))

    def test_todict(self):
        """Testing the to_dict method"""
        instance = self.value()
        self.assertEqual(instance.to_dict(), instance.to_dict())
        self.assertIsInstance(instance.to_dict(), dict)
        self.assertIn('id', instance.to_dict())
        self.assertIn('created_at', instance.to_dict())
        self.assertIn('updated_at', instance.to_dict())
        mdl = self.value()
        mdl.firstname = 'Celestine'
        mdl.lastname = 'Akpanoko'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', self.value(firstname='Celestine').to_dict())
        self.assertIn('lastname', self.value(lastname='Akpanoko').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(instance.to_dict()['created_at'], str)
        self.assertIsInstance(instance.to_dict()['updated_at'], str)
    
        # Tests to_dict output
        datetime_now = datetime.today()
        mdl = self.value()
        mdl.id = '012345'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': mdl.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            expected_dict = {
                 '__class__': 'BaseModel',
                 'id': 'u-b34',
                 'created_at': instance.created_at.isoformat(),
                 'updated_at': instance.updated_at.isoformat()
            }
            if hasattr(instance, 'age'):
                expected_dict['age'] = 13

            self.assertDictEqual(instance.to_dict(), expected_dict)

        with self.assertRaises(TypeError):
            instance.to_dict(None)
        
        with self.assertRaises(TypeError):
            instance.to_dict(self.value())
        
        with self.assertRaises(TypeError):
            instance.to_dict(45)
        
        self.assertNotIn('_sa_instance_state', mdl.__dict__)

    def test_kwargs_none(self):
        """testing kwargs again with non """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertNotEqual(new.created_at.isoformat(), new.updated_at)

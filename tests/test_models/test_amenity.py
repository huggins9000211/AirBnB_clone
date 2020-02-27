#!/usr/bin/python3
""" Unit tests for Amenity """
import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt
from models import storage


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.AmenityTest = Amenity()

    def test_subclass_Amenity(self):
        """Tests if Amenity is a subclass of BaseModel"""
        self.assertTrue(
            issubclass(
                self.AmenityTest.__class__,
                BaseModel),
            True)
        self.assertIsInstance(self.AmenityTest, Amenity)

    def test_attribute_types_Amenity(self):
        """Tests the attributes of Amenity"""
        self.assertEqual((self.AmenityTest.name), '')

    def test_save_Amenity(self):
        """Tests if saving works"""
        self.AmenityTest.save()
        self.assertNotEqual(
            self.AmenityTest.created_at,
            self.AmenityTest.updated_at)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

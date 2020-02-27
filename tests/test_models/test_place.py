#!/usr/bin/python3
"""Unit tests for Place"""
import os
import unittest
from models.base_model import BaseModel
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt
from models import storage


class TestPlace(TestBaseModel):
    """Tests for Place class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.PlaceTest = Place()

    def test_subclass_Place(self):
        """Tests if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.PlaceTest.__class__, BaseModel), True)
        self.assertIsInstance(self.PlaceTest, Place)

    def test_attribute_types_Place(self):
        """Tests the attributes of Place"""
        self.assertEqual((self.PlaceTest.city_id), '')
        self.assertEqual((self.PlaceTest.user_id), '')
        self.assertEqual((self.PlaceTest.name), '')
        self.assertEqual((self.PlaceTest.description), '')
        self.assertEqual((self.PlaceTest.number_rooms), 0)
        self.assertEqual((self.PlaceTest.number_bathrooms), 0)
        self.assertEqual((self.PlaceTest.max_guest), 0)
        self.assertEqual((self.PlaceTest.price_by_night), 0)
        self.assertEqual((self.PlaceTest.latitude), 0.0)
        self.assertEqual((self.PlaceTest.longitude), 0.0)
        self.assertEqual((self.PlaceTest.amenity_ids), [])

    def test_save_Place(self):
        """Tests if saving works"""
        self.PlaceTest.save()
        self.assertNotEqual(
            self.PlaceTest.created_at,
            self.PlaceTest.updated_at)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

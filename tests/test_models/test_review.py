#!/usr/bin/python3
"""Unit tests for Review"""
import os
import unittest
from models.base_model import BaseModel
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt
from models import storage


class TestReview(TestBaseModel):
    """Tests for Review class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.ReviewTest = Review()

    def test_subclass_Review(self):
        """Tests if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.ReviewTest.__class__, BaseModel), True)
        self.assertIsInstance(self.ReviewTest, Review)

    def test_attribute_types_Review(self):
        """Tests the attributes of Review"""
        self.assertEqual((self.ReviewTest.text), '')
        self.assertEqual((self.ReviewTest.user_id), '')
        self.assertEqual((self.ReviewTest.place_id), '')

    def test_save_Review(self):
        """Tests if saving works"""
        self.ReviewTest.save()
        self.assertNotEqual(
            self.ReviewTest.created_at,
            self.ReviewTest.updated_at)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

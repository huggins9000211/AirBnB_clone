#!/usr/bin/python3
"""Unit tests for user"""
import os
import unittest
from models.base_model import BaseModel
from models.state import State
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt
import json
from models import storage


class TestState(TestBaseModel):
    """Tests for State class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.StateTest = State()

    def test_subclass_State(self):
        """Tests if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.StateTest.__class__, BaseModel), True)
        self.assertIsInstance(self.StateTest, State)

    def test_attribute_types_State(self):
        """Tests the attributes of State"""
        self.assertEqual((self.StateTest.name), '')
        self.assertEqual(hasattr(self.StateTest, "name"), True)

    def test_save_State(self):
        """Tests if saving works"""
        self.StateTest.save()
        self.assertNotEqual(
            self.StateTest.created_at,
            self.StateTest.updated_at)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

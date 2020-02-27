#!/usr/bin/python3
""" FileStoage unit tests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import pep8


class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage """

    def test_pep8_FileStorage(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_save_FileStorage(self):
        """Tests if saving works"""
        store = FileStorage()
        store.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_all_FileStorage(self):
        """Tests if all is functional in File Storage"""
        store = FileStorage()
        dict_instances = store.all()
        self.assertIsNotNone(dict_instances)
        self.assertEqual(type(dict_instances), dict)
        self.assertIs(dict_instances, store._FileStorage__objects)

    def test_new_FileStorage(self):
        """Tests when new is created in File Storage"""
        store = FileStorage()
        item = store.all()
        user = User()
        user.id = 22475
        user.name = "Betty"
        store.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(item[key])

    def test_reload_FileStorage(self):
        """Tests reload in File Storage"""
        store = FileStorage()
        store.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except BaseException:
            pass
        store.save()
        with open(path, 'r') as f:
            lines_2 = f.readlines()
        self.assertEqual(lines, lines_2)
        try:
            os.remove(path)
        except BaseException:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(store.reload(), None)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()

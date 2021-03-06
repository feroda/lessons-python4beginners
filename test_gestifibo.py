# -*- coding: utf-8 -*-
import unittest
import codecs
import tempfile

import gestifibo
import export_manager as emanager

class TestGestiFibo(unittest.TestCase):
       
    def setUp(self):
        self.p = [
            {"name": "Gianni", "city": "Napoli", "salary": 3000, "genfibo": 5},
            # {"name": "Simone", "city": "Pesaro", "salary": 3300, "genfibo": 7},
            # {"name": "Gabriele", "city": "Faenza", "salary": 2900, "genfibo": 12},
            {"name": u"Fabiòòòò", "city": "Ascoli", "salary": 300, "genfibo": 8},
            # {"name": "Andrea", "city": "Ancona", "salary": 200, "genfibo": 32},
            # {"name": "Davide", "city": "Rimini", "salary": 2300, "genfibo": 1},
        ]

    # def tearDown(self):
    #    print("fine test")

    def test_export_repr_all(self):
        
        f, fname = tempfile.mkstemp()
        gestifibo.export_repr_all(self.p, fname=fname)
        with codecs.open(fname, "rb") as f:
            exported_content = f.read()
        with codecs.open("fixtures/test_export_all.txt", "rb") as f:
            content = f.read()
        self.assertEqual(exported_content, content)

    def test_export_repr_line_by_line(self):
        # content = u""

        f, fname = tempfile.mkstemp()
        gestifibo.export_repr_line_by_line(self.p, fname=fname)
        with codecs.open(fname, "rb") as f:
            exported_content = f.read()
        with codecs.open("fixtures/test_export_lbl.txt", "rb") as f:
            content = f.read()
        self.assertEqual(exported_content, content)

    def test_export_custom_line_by_line(self):
        # content = u""

        f, fname = tempfile.mkstemp()
        gestifibo.export_custom_line_by_line(self.p, fname=fname)
        with codecs.open(fname, "rb") as f:
            exported_content = [x.strip() for x in f.readlines()]
        with codecs.open("fixtures/test_export_custom.txt", "rb") as f:
            content = [x.strip() for x in f.readlines()]

        self.assertEqual(exported_content, content)


if __name__ == '__main__':
    unittest.main()

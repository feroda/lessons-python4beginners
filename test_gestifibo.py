# -*- coding: utf-8 -*-
import unittest
import codecs

import gestifibo

class TestGestiFibo(unittest.TestCase):
    
    def setUp(self):
        self.p = [
            {"name": "Gianni", "city": "Napoli", "salary": 3000, "genfibo": 5},
            {"name": "Simone", "city": "Pesaro", "salary": 3300, "genfibo": 7},
            {"name": "Gabriele", "city": "Faenza", "salary": 2900, "genfibo": 12},
            {"name": u"Fabiòòòò", "city": "Ascoli", "salary": 300, "genfibo": 8},
            {"name": "Andrea", "city": "Ancona", "salary": 200, "genfibo": 32},
            {"name": "Davide", "city": "Rimini", "salary": 2300, "genfibo": 1},
        ]

    # def tearDown(self):
    #    print("fine test")

    def test_export_repr_all(self):
        # content = u""
        gestifibo.export_repr_all(self.p)
        with codecs.open("fixtures/test_export_all.txt", "rb") as f:
            content = f.read()
        self.assertEqual(gestifibo.export_repr_all(self.p), content)

    def test_export_repr_line_by_line(self):
        # content = u""
        with codecs.open("fixtures/test_export_lbl.txt", "rb") as f:
            content = f.read()
        self.assertEqual(gestifibo.export_repr_line_by_line(self.p), content)

if __name__ == '__main__':
    unittest.main()
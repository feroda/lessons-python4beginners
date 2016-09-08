# -*- coding: utf-8 -*-

class Exporter(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello {}".format(self.name))
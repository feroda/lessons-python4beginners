# -*- coding: utf-8 -*-

class Exporter(object):

    def __init__(self, name):
        self.name = name

    def do_export(self, f, data):
        
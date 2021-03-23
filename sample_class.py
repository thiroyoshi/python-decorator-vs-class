#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SampleClass(object):

    def __init__(self):
        pass

    def controller(self, query_strings=None, body=None, path_params=None):
        print("controller is not implemented.")

    def handler(self, num_loop=10000):
        query_strings = 'Query'
        body = 'Body'
        path_params = 'Path'

        for i in range(0, num_loop + 1):
            self.controller(query_strings, body, path_params)

        return True

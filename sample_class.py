#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


class SampleClass(object):

    def __init__(self):
        pass

    def controller(self, query_strings=None, body=None, path_params=None):
        print("controller is not implemented.")

    def handler(self, num_loop=10000):
        query_strings = 'Query'
        body = 'Body'
        path_params = 'Path'

        start = time.perf_counter()

        for i in range(0, num_loop + 1):
            self.controller(query_strings, body, path_params)

        elapsed_time = time.perf_counter() - start

        print('elapsed_time: %f [msec]' % elapsed_time)

        return True

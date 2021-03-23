#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sample_decorator(controller):
    def handler(num_loop=10000):
        query_strings = 'Query'
        body = 'Body'
        path_params = 'Path'

        for i in range(0, num_loop + 1):
            controller(query_strings, body, path_params)

        return True
    return handler

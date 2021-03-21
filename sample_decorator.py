#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def decoratedHander(controller):
    def handler(event, num_loop):
        query_strings = 'Query'
        body = 'Body'
        path_params = 'Path'

        start = time.perf_counter()
        for i in range(0, num_loop + 1):
            controller(query_strings, body, path_params)

        elapsed_time = time.perf_counter() - start

        print('elapsed_time: %f [msec]' % elapsed_time)

        return True
    return handler

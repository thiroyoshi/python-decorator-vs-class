#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sample_decorator import sample_decorator


@sample_decorator
def controller(query_strings=None, body=None, path_params=None):
    print('This is NEW controller !!!')


if __name__ == '__main__':
    start = time.perf_counter()

    result = controller()
    print(result)

    elapsed_time = time.perf_counter() - start

    print('elapsed_time: %f [sec]' % elapsed_time)

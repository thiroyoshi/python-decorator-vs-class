#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sample_decorator import decoratedHander


@decoratedHander
def controller(query_strings=None, body=None, path_params=None):
    print('This is NEW controller !!!')


if __name__ == '__main__':
    result = controller(None, 10000)
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sample_class import SampleClass


class ImplementedClass(SampleClass):

    def controller(self, query_strings=None, body=None, path_params=None):
        print('This is NEW controller !!!')


if __name__ == '__main__':
    sc = ImplementedClass()
    result = sc.handler()
    print(result)

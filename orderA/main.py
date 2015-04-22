#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'davidportella'


def order_a(txt):
    return ''.join(sorted(txt))

if __name__ == "__main__":
    text = raw_input("Ingrese cadena de caracteres: ")

    result = order_a(text)

    print result
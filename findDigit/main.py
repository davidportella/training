#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'davidportella'

import re


def find_digit(txt):
    digit = re.search('[0-9]', txt)
    if digit is None:
        return False
    else:
        return digit.group(0)

if __name__ == "__main__":
    text = raw_input("Ingrese cadena de texto: ")

    result = find_digit(text)

    print result
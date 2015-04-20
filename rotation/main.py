#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'davidportella'


def rotation(worda, wordb):

    wordb += wordb

    if worda in wordb:
        message = "Palabra B es rotación de palabra A"
    else:
        message = "Palabra B no es rotación de palabra A"

    return message


if __name__ == "__main__":

    original = raw_input("Ingrese palabra A, original: ")
    rotado = raw_input("Ingrese palabra B, posible rotación: ")

    result = rotation(original, rotado)

    print result
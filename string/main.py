#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'davidportella'

import string
import random


# Funcion para generar un string random
def random_string(param):
    # inicializamos variables
    cadena = ""
    r = 42
    choices = string.ascii_lowercase + string.digits + string.punctuation

    # validamos si param es o podria ser valido
    if not isinstance(param, int):
        if param.isdigit():
            r = int(param)

    # Armamos la cadena
    for i in range(r):
        cadena += cadena.join(random.choice(choices))

    return cadena


if __name__ == "__main__":
    amount = raw_input("Ingrese cantidad de caracteres: ")

    result = random_string(amount)

    print result
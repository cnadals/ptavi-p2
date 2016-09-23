#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Calculadora():
    def suma(self, op1, op2):
        return op1 + op2

    def resta(self, op1, op2):
        return op1 - op2

if __name__ == "__main__":
    calculadora = Calculadora()
    resultado = calculadora.suma(3,5)
    print(resultado)
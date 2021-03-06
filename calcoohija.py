#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoo
import sys


class CalculadoraHija(calcoo.Calculadora):

    def multiplicacion(self, op1, op2):
        return op1 * op2

    def division(self, op1, op2):
        if op2 == 0:
            return "Division by zero is not allowed"
        else:
            return op1 / op2

if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    CalculaDeNuevo = CalculadoraHija()

    print(sys.argv)

    if sys.argv[2] == "suma":
        resultado = CalculaDeNuevo.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = CalculaDeNuevo.resta(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        resultado = CalculaDeNuevo.multiplicacion(operando1, operando2)
    elif sys.argv[2] == "divide":
        resultado = CalculaDeNuevo.division(operando1, operando2)
    else:
        sys.exit('Operación no válida.')

    print(resultado)

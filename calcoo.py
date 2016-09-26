#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
	def suma(self, op1, op2):
		return op1 + op2

	def resta(self, op1, op2):
		return op1 - op2

if __name__ == "__main":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	CalculadoraNueva = Calculadora()

	if sys.argv[2] == "suma":
		resultado = CalculadoraNueva.suma(operando1, operando2)
	elif sys.argv[2] == "resta":
		resultado = CalculadoraNueva.resta(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser sumar o restar.')
	print(resultado)

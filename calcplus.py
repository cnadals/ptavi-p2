#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

fich = open('fichero.csv', 'r')
lineas = fich.readlines()

if __name__ == '__main__':

    c = calcoohija.CalculadoraHija()

    for linea in lineas:
        operador = linea.split(',')[0]
        Datos = linea.split(',')[1:]
        resultado = int(Datos[0])

        if operador == "suma":
            for num in Datos[1:]:
                resultado = c.suma(resultado, int(num))
            print ("Suma = ", resultado)

        elif operador == "resta":
            for num in Datos[1:]:
                resultado = c.resta(resultado, int(num))
            print ("Resta = ", resultado)

        elif operador == "multiplica":
            for num in Datos[1:]:
                resultado = c.multiplicacion(resultado, int(num))
            print ("Multiplicacion = ", resultado)

        elif operador == "divide":
            for num in Datos[1:]:
                resultado = c.division(resultado, int(num))
            print ("Division = ", resultado)

        else:
            sys.exit('Error. Permite: suma, resta, multiplica, divide')

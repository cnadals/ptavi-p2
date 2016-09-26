####!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

#Empiezo
if __name__ == "__main__":

    #Abro el fichero
    with open('ficherooperaciones.csv') as fichero:
        Datos = csv.reader(fichero)

        c = calcoohija.CalculadoraHija()

        for linea in fichero:
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
                    if Datos == "0":
                        sys.exit("Error: Division by 0 is not allowed")
                    else:
                        resultado = c.division(resultado, int(num))
                print ("Division = ", resultado)
            else:
                sys.exit('Error. Permite: suma, resta, multiplica, divide.')

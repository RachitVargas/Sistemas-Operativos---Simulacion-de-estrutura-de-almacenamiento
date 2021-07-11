#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:45:02 2021

@author: antony.vargasulead.ac.cr
"""

def main():
    
    opcion = 0
    while opcion != 2:
        
        print("Bienvenido al simulador [Estructura de almacenamiento en la nube]")
        print('Elija una opcion:')
        
        print("1. Correr simulacion.")
        print("2. Salir de la simulacion.")
        
        try:
            opcion = int(input())
            if opcion == 1:
                megas_inicial = int(input("Ingrese la cantidad de megas inicial: "))
                n_dias = int(input("Ingrese la cantidad de dias: "))
                dias = n_dias
                almacenamiento_total = 0
                for i in range(n_dias):
                    print("dia " + str(i+1) + ", cantidad de almacenamiento disponible: " +\
                          str(megas_inicial) + " megas; cantidad de dias faltantes: " + str(n_dias-1))
                    
                    megas_dia = int(input("Ingrese la cantidad de megas que almacenara el dia " +\
                                          str(i+1) + ": "))
                    
                    if megas_dia <= megas_inicial:
                        almacenamiento_total += megas_dia
                        megas_inicial = megas_inicial - megas_dia
                        n_dias -= 1
                    else:
                        print("La cantidad de megas solicitadas excede el almacenamiento disponible")
                        
                print("En " + str(dias) + " dias se almaceno " + str(almacenamiento_total) +\
                      " megas y sobro " + str(megas_inicial) + " megas disponibles")
                
            elif opcion == 2:
                print("Muchas gracias por usar el simulador.")
        
            else:
                print("Opcion invalida, vuelva a intentarlo.")
    
        except:
            print("Por favor asegurese haber ingresado un valor correcto.")
            

if __name__ == '__main__':
    main()
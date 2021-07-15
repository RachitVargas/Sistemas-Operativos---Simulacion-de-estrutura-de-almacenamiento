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
                promedio_megas = 7000
                dias = 0
                for i in range(n_dias):
                    print("dia " + str(i+1) + ", cantidad de almacenamiento disponible: " +\
                          str(megas_inicial) + " megas")
                    dias += 1
                    if megas_inicial > 28000:
                        megas_inicial = megas_inicial + promedio_megas + (promedio_megas*0.4)
                        
                    else:
                        megas_inicial = megas_inicial + promedio_megas + (promedio_megas*0.31)
                
                print("En " + str(dias) + " dias se almaceno " + str(megas_inicial) +\
                      " megas.")
                
            elif opcion == 2:
                print("Muchas gracias por usar el simulador.")
        
            else:
                print("Opcion invalida, vuelva a intentarlo.")
    
        except:
            print("Por favor asegurese haber ingresado un valor correcto.")
            

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:47:37 2023

@author: wixav
"""
#-------------------Inicio Programa 1---------------

nombre1 = input("Ingresa tu nombre: ")
print("Ahora estas en la matrix", nombre1) 

#------------------Fin Programa 1-------------------

#-------------------Inicio Programa 2---------------

num_dec = float(input("Ingresa un numero decimal: "))
num_int = int(input("Ingresa un numero entero: "))
suma = num_dec + num_int
print("El resultado de la suma es: ", suma)

#------------------Fin Programa 2-------------------

#-------------------Inicio Programa 3---------------

num_1 = float(input("Ingresa un numero: "))
num_2 = float(input("Ingresa otro numero: "))
suma2 = num_1 + num_2
print("La suma de los dos numeros es ", suma2)
num_3 = float(input("Ingresa otro numero: "))
producto = suma2 * num_3
print("El producto de la suma y del numero es ", producto)

#------------------Fin Programa 3-------------------

#-------------------Inicio Programa 4---------------

km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
lit = float(input("Ingresa la cantidad de litros consumidos: "))
cons = km/lit
print("El consumo por kilometro es de: ", cons)

#------------------Fin Programa 4-------------------

#-------------------Inicio Programa 5---------------

fr = float(input("Ingrese una temperatura en grados Farenheit: "))
temc = (5/9) * (fr-32)
print("La temperatura en Celsius es de: ", temc)


#------------------Fin Programa 5-------------------

#-------------------Inicio Programa 6---------------

num_4 = float(input("Ingresa un numero: "))
num_5 = float(input("Ingresa otro numero: "))
num_6 = float(input("Ingresa otro numero: "))
prom = (num_4 + num_5 + num_6)/3
print("El promedio de los tres numeros es de: ", prom)

#------------------Fin Programa 6-------------------

#-------------------Inicio Programa 7---------------

num_7 = float(input("Ingresa un numero: "))
des = num_7 - (num_7 *0.15)
print("Descontado el 15% queda: ", des)

#------------------Fin Programa 7-------------------

#-------------------Inicio Programa 8---------------

pal_1 = input("Ingresa la primera palabra: ")
pal_2 = input("Ingresa la segunda palabra: ")
fra = pal_1 + " " +  pal_2
print("La frase es: ", fra)

#------------------Fin Programa 8-------------------

#-------------------Inicio Programa 9---------------

tex = input("Ingresa un texto: ")
print("La primera letra del texto  es:", tex[0])

indice = int(input(f"Ingresa un número positivo menor a {len(tex)}: "))
print("El carácter del texto ubicado en la posición dada por indice es:", tex[indice])

#------------------Fin Programa 9-------------------

#-------------------Inicio Programa 10---------------

shows = int(input("Ingresa la cantidad de shows musicales que has visto el ultimo año: "))
print("¿Has visto más de 3 shows musicales en el último año?:", shows > 3)

#------------------Fin Programa 10-------------------

#-------------------Inicio Programa 11---------------

fecha = (input("Ingrese una fecha en formato DDMMAAAA: "))
dia = fecha[0:2]
mes = fecha[2:4]
anio = fecha[4:8]
fechafor = dia + " / " + mes + " / " + anio
print("La fecha ingresada es:", fechafor)
    
#------------------Fin Programa 11-------------------

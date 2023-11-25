# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:35:09 2023

@author: Xavier Cevallos
"""

cedula = input("Ingrese su numero de cedula: ")
# la cedula debe tener 10 digitos     
if(len(cedula)) == 10:
    
    # codigo de provincia (primeros 2 digitos)
    provincia = int(cedula [0:2])
    
    # str para mostrar el numero si empieza con 0
    provinciaf = str(cedula [0:2])
       
    if 1<= provincia <= 24 or provincia == 30:
        # comprobacion del tercer digito
        terdig = int(cedula [2])
        if 0 <= terdig <= 6:

        #numeros impares y suma
            numim_1 = int(cedula[0]) * 2
            if (numim_1 > 9):
                numim_1 = numim_1 - 9        
        
            numim_2 = int(cedula[2]) * 2
            if (numim_2 > 9):
                numim_2 = numim_2 - 9       
        
            numim_3 = int(cedula[4]) * 2
            if (numim_3 > 9):
                numim_3 = numim_3 - 9
                
            numim_4 = int(cedula[6]) * 2
            if (numim_4 > 9):
                numim_4 = numim_4 - 9
            
            numim_5 = int(cedula[8]) * 2
            if (numim_5 > 9):
                numim_5 = numim_5 - 9
                  
            numimpares = (numim_1 + numim_2 +numim_3 + numim_4 + numim_5)
            
        #suma de numeros pares
            numpares = int(cedula[1]) +int(cedula[3])+  int(cedula[5]) + int(cedula[7])      
            
        #suma total
            sumatotal = numimpares + numpares
        
        #digito verificador     

            strtotal = str(sumatotal)
            numveri = int(strtotal[1])
            if numveri < 1:
               numveri = (numveri + 10)
            digver = (10 - numveri) 
          
            if digver != int(cedula [9]):
                print("Cedula invalida, ingresa tus datos de nuevo")
            else:
                if numveri == 0 and provincia != 30:
                    print("Cedula autentica")
                    print("Codigo de verificacion: 0")
                    print("Codigo de provincia correcto", provinciaf)
                
                if numveri != 0 and provincia != 30: 
                    print("Cedula autentica")
                    print("Codigo de verificacion: ", digver)
                    print("Codigo de provincia correcto: ",provinciaf)
                
                #cedula extranjera
               
                if provincia == 30 and numveri == 0:
                    print("Cedula autentica")
                    print("Codigo de verificacion: 0")
                    print("Codigo extranjero correcto", provincia)
                    
                if provincia == 30 and numveri != 0:
                    print("Cedula autentica")
                    print("Codigo de verificacion: ", digver)
                    print("Codigo extranjero correcto: ",provincia)
            
        else:(print("Numero de cedula no valido, ingresa tus datos de nuevo"))
    else:(print("El codigo de provincia no es valido, ingresa tus datos de nuevo"))    
else:(print("La cedula debe tener 10 digitos, ingresa tus datos de nuevo"))    
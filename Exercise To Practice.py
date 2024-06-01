#Pequeño ejercicio
#Imprime todos las posiciones de la lista donde esta el numero 32

"""mi_lista=[32,345,3432,32,23,32]
posiciones=[]

for i in range (len(mi_lista)):
    if not mi_lista[i] != 32:
        posiciones.append(i)
print(posiciones)"""


#Ejercicio
"""Escribe un programa en Python que permita calcular el IMC de una persona y clasificar su estado de peso de acuerdo 
con la siguiente tabla:

IMC < 18.5: Bajo peso
18.5 <= IMC < 25: Peso normal
25 <= IMC < 30: Sobrepeso
IMC >= 30: Obesidad
Requisitos:
IMC = peso / altura ^ 2
El programa debe solicitar al usuario que ingrese su peso en kilogramos y su altura en metros.
Debe calcular el IMC utilizando la fórmula proporcionada.
Debe mostrar el resultado del IMC y la clasificación de acuerdo con la tabla proporcionada.
Debe manejar entradas inválidas (por ejemplo, valores negativos o no numéricos) y solicitar al usuario que vuelva a ingresar los datos
si es necesario.
El programa debe ser capaz de calcular el IMC para múltiples personas si así lo desea el usuario."""


import os
def imc (n,m):
    try:
        n=float(input("Ingrese su peso en kiligramos: "))
        m=float(input("Ingrese su altura en metros: "))
    
        IMC=(n/m**2)
    except ValueError:
        print("Valor ingresado no valido")
        os.system("cls")
        imc(0,0)
    finally:   
        if IMC < 18.5:
            print("Clasificación: Bajo de peso")
        elif IMC >18.5 and IMC < 25:
            print("Clasificación: Peso Normal")
        elif IMC >=25 and IMC < 30:
            print("Clasificación: Sobrepeso")
        elif IMC >=30:
            print("Clasificación: Obesidad")
    print("""Deseas Repetir el proceso
          1. Ingresa 1 para si:
          2. Ingresa 2 para no""")
    opc=int(input("Ingresa tu opción: "))
    if opc == 1:
        os.system("cls")
        imc(0,0)
    elif opc == 2:
        exit()
    else:
        os.system("cls")
        imc(0,0)
    
imc(0,0)
    
     



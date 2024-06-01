
'''
Operadores
'''

#Operadores aritmeticos
print("###Operadores de aritmeticos###","\n")
print(f"Suma 10 + 3 = {10 + 3}")
print(f"Resta 10 - 3 = {10 - 3}")
print(f"Multiplicación 10 * 3 = {10 * 3}")
print(f"División 10 / 3 = {10 / 3}")
print(f"Modulo 10 % 3 = {10 % 3}")
print(f"Modulo 10 % 2 = {10 % 2}")
print(f"Exponente 10 ** 3 = {10 ** 3}")
print(f"Divisió entera 10 // 3 = {10//3}")
print(f"Exponente -10 ** 4 = {-10 ** 4}")
print(f"Exponente (-10) ** 3 = {(-10) ** 3}")
print(f"Exponente (-10) ** 4 = {(-10) ** 4}")

#Operadores de comparación

print("\n","###Operadores de comparación","\n")
print(f"Igualdad: 10 == 3 -> {10==3}")
print(f"Desigualdad: 10 != 3 -> {10!=3}")
print(f"Mayor que: 10 > 3 -> {10>3}")
print(f"Menor que: 10 < 3 -> {10<3}")
print(f"Mayor o igual que: 10 >= 3 -> {10>=3}")
print(f"Menor o igual que: 10 <= 3 -> {10<=3}","\n","#Ejemplo","\n")
a="string"
b="strasdfgfd"
print(f"a ='string' y b = 'strasdfgfd'{a==b}")
print(f"a ='string' y b = 'strasdfgfd'{a!=b}")


#Operadores lógicos
# Lógicos
'''
  Operador              Descripción
  and         Devuelve True si ambos son True
  or          Devuelve True si alguno de los operandos es True
  not         Devuelve True si alguno de los operandos es False
'''

print("\n","###Operadores Lógicos","\n",f"AND &&: 17 + 7 == 24 and 5 - 1 == 4 es {17 + 7 == 24 and 5 - 1 == 4}")
print(f"OR ||: 17 + 7 == 24 or 5 - 1 == 4 es {17 + 7 == 24 or 5 - 1 == 8}")
print(f"NOT !: not 17 + 7 == 21 es {not 17 + 7 == 21}")

print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}","\n")

#Operadores de Operación

print("Operadores de Operación","\n")
messi = 10 #Asignación
ronaldo = 7

messi+=1 #Suma y asignación (messi=messi+1)
print (messi)
ronaldo-=1 #Resta y asiganción
print(ronaldo)
messi*=3 #Multiplicación y asignación
print(messi)
ronaldo/=2 #División y asignación
print(ronaldo)
messi&=2 #Modulo y asignación
print(messi)
ronaldo**=2 #Exponente y asignación
print(ronaldo)
messi//=8 #División entera y asignación
print(messi)

#Operadores de Identidad
print("###Operadores de Indentidad###","\n")
print("messi = ronaldo")
messi = ronaldo
print(f"messi is ronaldo es {messi is ronaldo}")
'''
Mientras las variables apunten hacia la misma dirección 
el resultado del is sera true, de lo contrario sera un 
false
'''

print(f"messi is not ronaldo es {messi is not ronaldo}")

#Operadores de pertenecia
print("###Operadores de Pertenencia###","\n")
print(f"'u' in 'you' = {'u' in 'you'}")
print(f"'z' not in 'Cristhian' = {'z' not in 'Cristhian'}")

#Estructuras de control
#Estructura if
#Ejemplo

print("""
#Estructuras de control
#Estructura if
#Ejemplo
""")
lista = [3,'a',3,36,"mes",554,True]
if 36 in lista:
    lista.pop(lista.index(36))
print(lista)



if len(lista)==lista.index(True)+1:
    print(len(lista))
    print(lista.index(True)+1)
    lista.clear()
print(lista)

print("""
#Estructura for
#Ejemplo
""")

string="bucle for in phyton"
print("string= bucle for in phyton")
for i in range(len(string)): 
    contar=1
if 'e' in string:
    print("hay ",contar,"La letra 'e' en tu string" )
    contar+=1
#Manejo de expeciones
#ZeroDivisionError: division by zero


try:
    print(10/0) 
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print("Continuamos")

try:
    int(input("Ingresa un numero: "))
except ValueError:
    print("Solo valores enteros")
    





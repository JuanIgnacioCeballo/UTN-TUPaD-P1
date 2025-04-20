# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un número entero: "))
digitos = 0 

while num % 2 != 0:
    num = int(input("Por favor, ingrese un número entero: "))
original = num

while num > 0:
    digitos += 1
    num = num // 10 #se obtiene división entera


print(f"El número {original} tiene {digitos} dígitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número del conjunto: "))
num2 = int(input("Ingrese el segundo número del conjunto: "))
suma = 0

for i in range(num1+1, num2):
    suma += i;

print(f"La suma de los números en el conjunto ({num1}, {num2}) es igual a {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

def isInt(value):
    try:
        if value[0] == "-":
            return True
        int(value)
        return True
    except ValueError:
        return False

numero_secuencia = 0
numero_secuencia2 = 0

numero_secuencia = int(input("Ingrese un número entero a sumar (0 si quiere finalizar la operación): "))
if numero_secuencia != 0:

    numero_secuencia2 = input("Ingrese otro número entero a sumar (0 si quiere finalizar la operación): ")
    while not isInt(numero_secuencia2) or "." in numero_secuencia2:
        numero_secuencia2 = input("Por favor, ingrese un número entero a sumar (0 si quiere finalizar la operación): ")
    numero_secuencia2 = int(numero_secuencia2)

    sumatoria = numero_secuencia + numero_secuencia2


    if numero_secuencia2 != 0:
        sumatoria = numero_secuencia + numero_secuencia2
        while numero_secuencia2 != 0:
            numero_secuencia2 = input("Ingrese otro número entero a sumar (0 si quiere finalizar la operación): ")
            while not isInt(numero_secuencia2) or "." in numero_secuencia2:
                numero_secuencia2 = input("Por favor, ingrese un número entero a sumar (0 si quiere finalizar la operación): ")   
            numero_secuencia2 = int(numero_secuencia2)
            sumatoria += numero_secuencia2

else:
    sumatoria = numero_secuencia + numero_secuencia2

print(f"La sumatoria es de {sumatoria}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_random = random.randint(0, 9)
intentos = 1

print("Bienvenido, debe adivinar el número entre 0 y 9")
num_user = int(input("Ingrese su número: "))
if num_user not in range(0, 10):
    num_user = int(input("Por favor solo puede ingresar un número del 0 a 9: "))
    intentos += 1
while num_user != num_random:
    num_user = int(input("Ingrese otro número: "))
    if num_user not in range(0, 10):
        num_user = int(input("Por favor, solo puede ingresar un número del 0 a 9: "))
    intentos += 1

print(f"Felicitaciones ha adivinado que el número era {num_random} en {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

def isNatural(numero):
    try:
        if numero[0] == "-":
            return False
        int(numero)
        return True
    except ValueError:
        return False



sumatoria_limit = 0
num_limit = input("Ingrese el número limite del conjunto del cual quiere hacer la sumatoria de sus elementos: ")
while not isNatural(num_limit) or "." in num_limit:
    num_limit = input("Por favor, el número limite del conjunto debe ser natural: ")
num_limit = int(num_limit)

for i in range(0, num_limit+1):
    sumatoria_limit += i

print(f"La sumatoria de los números del conjunto [0, {num_limit}] es de {sumatoria_limit}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

impar = 0
par = 0
positivo = 0
negativo = 0
for i in range(0, 100):
    num_100 = input(f"Ingrese el número nº{i+1}: ")
    while not isInt(num_100) or "." in num_100:
        num_100 = input(f"Por favor el número nº{i+1} debe ser entero: ")
    num_100 = int(num_100)

    if num_100 % 2 == 0 and num_100 != 0:
        par += 1
    elif num_100 % 2 != 0:
        impar += 1

    if num_100 >= 0:
        positivo += 1
    elif num_100 < 0:
        negativo += 1

print(f"En el conjunto hay {positivo} números positivos, {negativo} números negativos, {par} números pares y {impar} números impares")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).


sumatoria_media = 0
for i in range(0, 100):
    num_media = input(f"Ingrese el número entero nº{i+1} : ")
    while not isInt(num_media) or "." in num_media:
        num_media = input(f"Por favor el nº{i+1} debe ser un número entero: ")
    num_media = int(num_media)
    sumatoria_media += num_media
media_aritmetica = sumatoria_media/100
print(f"La media aritmetica de los números ingresados es {media_aritmetica}")


# # 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

to_inverse = input("Ingrese un número entero para invertirlo: ")
while not isInt(to_inverse) or "." in to_inverse:
    to_inverse = input("Por favor, ingrese un número entero: ")

# num_toInverse = []

# for i in range(0, len(to_inverse)+1):
#         num_toInverse.append(to_inverse[i+1])
negativo = False
num_toInverse = list(to_inverse)

if num_toInverse[0] == "-":
    negativo = True
    num_toInverse.pop(0)

num_inversed = []
for i in range(len(num_toInverse)):
    num_inversed.insert(0, num_toInverse[i])

if negativo:
    num_inversed.insert(0, "-")

inversed = int("".join(map(str,num_inversed)))

print(f"El número {to_inverse} invertido es {inversed}")

    











        
    



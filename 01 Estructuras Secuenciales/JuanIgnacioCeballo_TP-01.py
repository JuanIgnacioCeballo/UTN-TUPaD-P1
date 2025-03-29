# Juan Ignacio Ceballo

import math

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

first = str(input("Ingrese su nombre: "))
sur = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
nac = str(input("Ingrese su país de origen: "))

print(f"Soy {first} {sur}, tengo {edad} años y nací en {nac}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

r = float(input("Ingrese el radio del circulo: "))

A = math.pi * r ** 2
P = math.pi * 2 * r

print(f"El área del circulo es de {A} cm cuadrados y su perímetro es de {P} cm")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

sec = int(input("Ingrese la cantidad de segundos: "))

hs = sec/3600

print(f"{sec} segundos equivalen a {hs} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese el número del cuál quiere saber su tabla: "))

print(num, " x 1 =", num * 1, "\n ", num, " x 2 = ", num * 2, "\n ", num, " x 3 = ", num * 3, "\n ", num, " x 4 = ", num * 4, "\n ", num, " x 5 = ", num * 5, "\n ", num, " x 6 = ", num * 6, "\n ", num, " x 7 = ", num * 7, "\n ", num, " x 8 = ", num * 8, "\n ", num, " x 9 = ", num * 9, "\n ", num, " x 10 = ", num * 10, "\n ") 

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num2 = int(input("Ingrese el primer número entero: ")) 
num3 = int(input("Ingrese el segundo número entero: ")) 

sum = num2 + num3
rest = num2 - num3
mult = num2 * num3
div = num2 / num3

print(f"La suma entre {num2} y {num3} es igual a {sum}\n La resta entre {num2} y {num3} es igual a {rest}\n La multiplicación entre {num2} y {num3} es igual a {mult}\n La división entre {num2} y {num3} es igual a {div}\n ")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

height = float(input("Ingrese su altura: "))
weight = float(input("Ingrese su peso: "))

massIndex = weight / height**2

print(f"Su índice de masa corporal es de {massIndex}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

cel = float(input("Ingrese la temperatura en grados Celcius: "))

far = cel * 9/5 + 32

print(f"{cel}º Celcius equivale a {far}º Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

media = (n1 + n2 + n3)/3

print(f"El promedio de los números ingresados es {media}")

